import discord
import json

bot_token = open('.token').read().strip()

intents = discord.Intents().default()
intents.members = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

members = []
@client.event
async def on_message(message):
    if message.content.startswith('!member'):
        print(client.guilds)
        for guild in client.guilds:
            print(guild)
            for member in guild.members:
                # print(member)
                members.append(str(member))
        print(len(members))
        json.dump(members, open('members.json', 'w'))
client.run(bot_token)
