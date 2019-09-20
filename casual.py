import discord, re
from datetime import datetime
import prompts

validRegex = re.compile('(\d{1,2})([smhd])')

# For now just using api token in text file, later config file
with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

CONVERT = {'s': 1, 'm': 60, 'h': 3600}

def stringToTime(match: 're.match') -> int:
    # returns time in ms from stringed match in SECONDS
    try:
        time = int(match.group(1))
        assert time != 0

        return time * CONVERT[match.group(2)]
    except (ValueError, AssertionError):
        return 0

class CasualDiscord(discord.Client):

    async def on_ready(self):
        self.config = dict()
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if type(message.channel) == discord.channel.DMChannel:
            await self.handle_pm(message)

        if message.content == '$casual':
            await message.channel.send(prompts.INIT)
        elif message.author.id in self.config.keys():
            self.config[message.author.id]['channels'][message.channel.id] = datetime.now().timestamp()
        else:
            await self.handle_notif(message)

    async def handle_notif(self, message):
        for userId, config in self.config.items():
            if message.channel.id in config['channels']:
                start = datetime.fromtimestamp(config['channels'][message.channel.id])
                diff = datetime.now() - start
                if(diff.seconds < config['time']):
                    await self.get_user(userId).send(prompts.FWD.format(content = message.content, author = message.author, channel = message.channel))

    async def handle_pm(self, message):
        result = re.match(validRegex, message.content.lower())

        if(result):
            time = stringToTime(result)

            if(time == 0):
                await message.channel.send(prompts.INVALID_TIME)
            else:
                self.config[message.author.id] = {'time': time, "channels": dict()}
                await message.channel.send(prompts.CONFIRM.format(' '.join(result.groups())))
        else:
            await message.channel.send(prompts.INVALID_TIME)

client = CasualDiscord()
client.run(TOKEN)