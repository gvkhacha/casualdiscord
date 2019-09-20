import discord
import prompts
# For now just using api token in text file, later config file

with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

print(TOKEN)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '$casual':
            await message.channel.send('PM this bot to enable casual discord notifications')

client = MyClient()
client.run(TOKEN)