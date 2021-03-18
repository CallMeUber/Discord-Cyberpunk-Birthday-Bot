import discord
client = discord.Client()
intents = discord.Intents.default()
intents.members = True

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'

        )
        async for member in guild.fetch_members(limit=150):
            print(member.name)
#
#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')
    # print(f'{client.user} has connected to Discord!')
    # print(f'Connected to servers:')
    # print(client.guilds)
    # for guild in client.guilds:
    #     print(f'Guilds are: {guild}')
    #     print(f'Current Guild: {guild}')
    #     print(f'Members are: {guild.members}')

@client.event
async def on_message(message):
    if (message.author.name == 'KrizhanLewis' and message.author.discriminator == '3469'):
        # print(f'Message\'s author is: {message.author}')
        # print(f'Message is {message}')
        print(f'Prepare for text: ')
        await message.add_reaction('🇬')
        await message.add_reaction('🇴')
        await message.add_reaction('🇳')
        await message.add_reaction('🇰')
    else:
        print(message.author.discriminator)

client.run('NzY2NTAxNDM2OTYzOTQ2NDk3.X4kSFw.0oZrFEiFi4k-canLYa5v3iEGOtc')

