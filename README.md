# CasualDiscord

This was a quick project making a discord bot using Python using [an API wrapper](https://github.com/Rapptz/discord.py).

I use discord regularly, but not enough to want to get notifications all the time. This bot allows users like me to get notifications via direct message on channels they have messaged in recently. 

To begin, send a direct message to the bot with a time frame. Every time that user sends a message in the channel, the bot will forward all messages sent in that channel within that time frame.

### Usage / Development

Environment is managed using `pipenv`, with pip file included. The discord bot token needs to be entered in `token.txt`. 

```
pipenv install
pipenv run casual.py
```
