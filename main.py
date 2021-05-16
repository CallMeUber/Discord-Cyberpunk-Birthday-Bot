import yaml
import discord
from datetime import datetime
from discord.ext.tasks import loop

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

COPY_PASTA = "I’ll have you cognize I graduated most elite in my division in the Navy Seals, and I’ve been enmeshed in multifarious undisclosed incursions on Al-Quaeda, and I have over 300 habituated executions. I am experienced in guerilla campaign and I’m the most qualigied sharpshooter in the full US armed forces. You are nothing to me but just an additional victim. I will obliterate you the copulate out with rigor the likes of which has at no time been seen previously on this macrocosm, indicate my fricking units of language. You assume you can be acquit with saying that fecal matter to me via the Information Superhighway? Acknowledge anew, undesirable person. At the time that we communicate I am influencing my covert organization of operatives crosswise the New World and your Internet Protocol is being pursued immediately so you better bolster for the assault, larval fly. The disturbance that annihilates the deplorable petty existence you refer to as your duration. You’re frigging late, child under the age of 18. I can be omnipresent, at any unspecified point in time, and I can annihilate you in surplus seven centum techniques, and that’s merely with my unequipped metacarpus. Not exclusively am I extensively qualified for hand-to-hand combat, but I have admittance to the total armory of the United States Marine Corps and I will handle it to its absolute breadth to decimate your wrethed derriere off the surface of the large landmass, you minuscule excrement. If only you could have been aware of what unhallowed comeuppance your smol “ingenious” statement was almost to bear downward upon you, perchance you bequest have refrained from unpleasantly speaking. However, you couldn’t, you didn’t, and now you’re reconciling, you accursed tomfool. I will excrete acrimony all over you and you will inundate in it. You’re flipping finito"

# general global variables
members_list = {}
special_members = []

# gonk/choom global variables
gonk_flag, choom_flag = True, True
gonk_list, choom_list = [], []

# cake day global variables
TIME_INTERVAL = 1
prev_execution_time = -1


def get_config():
    try:
        with open('./config.yml') as file:
            return yaml.full_load(file)
    except IOError:
        print("Could not read the file")
        return None


def get_auth_token():
    try:
        with open('./authToken.yml') as file:
            return yaml.full_load(file)['auth_token']
    except IOError:
        print("Could not read the file")
        return None


async def greet_cake_day(text_channel, person):
    if not text_channel or not person:
        return
    greeting = f"Happy Discord Cake Day {person.mention}! Allow me to add a little festive vibe to your message." \
               f" Type !birthday stop to end"
    await text_channel.send(greeting)


def get_general_text_channel(guild):
    for channel in guild.channels:
        if channel.name.lower() == "general" and type(channel) is discord.channel.TextChannel:
            return channel


@loop(hours=TIME_INTERVAL)
async def check_time():
    # This function runs periodically every two hours

    global prev_execution_time, special_members

    now = datetime.now()
    current_time = now.second

    # if execution happened already on the same day, skip this execution
    if current_time == prev_execution_time:
        return

    prev_execution_time = current_time

    # Check for person with discord cake day
    special_members = []
    for member in members_list:
        if member.created_at.day == now.day and member.created_at == now.month:
            special_members.append(member)

    # If someone has cake day, greet them
    if special_members:
        for member in special_members:
            for channel in members_list[member]:
                await greet_cake_day(channel, member)


@client.event
async def on_message(message):

    content = message.content.lower()
    author_name = message.author.name.lower()
    author_discriminator = message.author.discriminator

    global gonk_flag, choom_flag, special_members

    if content == "uber bad":
        await message.channel.send(COPY_PASTA)

    elif content == "!stop gonk":
        gonk_flag = False

    elif content == "!go gonk":
        gonk_flag = True

    elif content == "!stop choom":
        choom_flag = False

    elif content == "!go choom":
        choom_flag = True

    elif content == "!birthday stop":
        member_to_remove = None
        for member in special_members:
            if author_name == member.name.lower():
                member_to_remove = member
                break
        if member_to_remove:
            special_members.remove(member_to_remove)

    for choom in choom_list:
        if choom_flag and choom['name'] == author_name and choom['discriminator'] == author_discriminator:
            await react_choom(message)

    for gonk in gonk_list:
        if gonk_flag and gonk['name'] == author_name and gonk['discriminator'] == author_discriminator:
            await react_gonk(message)

    if special_members:
        for member in special_members:
            if author_name == member.name.lower():
                await message.add_reaction('🎂')
                await message.add_reaction('🕺')
                await message.add_reaction('🎉')


@client.event
async def on_ready():

    # list all members in the same server as bot
    for guild in client.guilds:
        general_text_channel = get_general_text_channel(guild)
        for member in guild.members:
            if member.bot:
                continue
            user_object = await client.fetch_user(member.id)
            if user_object in members_list:
                members_list[user_object].append(general_text_channel)
            else:
                members_list[user_object] = [general_text_channel]

    for key in members_list:
        print(f"{key} value: {members_list[key]}")

    check_time.start()


async def react_gonk(message):
    await message.add_reaction('🇬')
    await message.add_reaction('🇴')
    await message.add_reaction('🇳')
    await message.add_reaction('🇰')


async def react_choom(message):
    await message.add_reaction('🇨')
    await message.add_reaction('🇭')
    await message.add_reaction('🇴')
    await message.add_reaction('⭕')
    await message.add_reaction('🇲')


def main():

    token = get_auth_token()
    config = get_config()

    if config is None:
        return

    global choom_list, gonk_list

    choom_list = config['chooms']
    gonk_list = config['gonks']

    client.run(token)


if __name__ == "__main__":
    main()

