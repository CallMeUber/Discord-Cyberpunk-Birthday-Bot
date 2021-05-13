import yaml
import discord
import threading
from datetime import datetime

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

COPY_PASTA = "I’ll have you cognize I graduated most elite in my division in the Navy Seals, and I’ve been enmeshed in multifarious undisclosed incursions on Al-Quaeda, and I have over 300 habituated executions. I am experienced in guerilla campaign and I’m the most qualigied sharpshooter in the full US armed forces. You are nothing to me but just an additional victim. I will obliterate you the copulate out with rigor the likes of which has at no time been seen previously on this macrocosm, indicate my fricking units of language. You assume you can be acquit with saying that fecal matter to me via the Information Superhighway? Acknowledge anew, undesirable person. At the time that we communicate I am influencing my covert organization of operatives crosswise the New World and your Internet Protocol is being pursued immediately so you better bolster for the assault, larval fly. The disturbance that annihilates the deplorable petty existence you refer to as your duration. You’re frigging late, child under the age of 18. I can be omnipresent, at any unspecified point in time, and I can annihilate you in surplus seven centum techniques, and that’s merely with my unequipped metacarpus. Not exclusively am I extensively qualified for hand-to-hand combat, but I have admittance to the total armory of the United States Marine Corps and I will handle it to its absolute breadth to decimate your wrethed derriere off the surface of the large landmass, you minuscule excrement. If only you could have been aware of what unhallowed comeuppance your smol “ingenious” statement was almost to bear downward upon you, perchance you bequest have refrained from unpleasantly speaking. However, you couldn’t, you didn’t, and now you’re reconciling, you accursed tomfool. I will excrete acrimony all over you and you will inundate in it. You’re flipping finito"
birthday_list ={}

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


def checkTime():
    # This function runs periodically every two hours
    threading.Timer(7200, checkTime).start()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    if(current_time == '02:11:00'):  # check if matches with the desired time
        print('sending message')

@client.event
async def on_message(message):

    global gonk_flag,choom_flag

    content = message.content.lower()

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

    elif "!birthday" in content:
        negator_string = content[10:13]
        if negator_string == "not":
            person = content[14:]
            if person in birthday_list:
                birthday_list.remove(person)
        else:
            person = content[10:]
            if person not in birthday_list:
                birthday_list.append(person)

    author_name = message.author.name.lower()
    author_discriminator = message.author.discriminator

    for choom in choom_list:
        if choom_flag and choom['name'] == author_name and choom['discriminator'] == author_discriminator:
            await react_choom(message)

    for gonk in gonk_list:
        if gonk_flag and gonk['name'] == author_name and gonk['discriminator'] == author_discriminator:
            await react_gonk(message)

    if birthday_list and author_name.lower() in birthday_list:
        await message.add_reaction('🎂')
        await message.add_reaction('🕺')
        await message.add_reaction('🎉')


@client.event
async def on_ready():
    for guild in client.guilds:
        for member in guild.members:
            if member.bot:
                continue
            user_object = await client.fetch_user(member.id)
            birthday_list[member.name] = user_object.created_at

    for key in birthday_list:
        print(f"{key} value: {birthday_list[key]}")


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

    global choom_list, gonk_list, gonk_flag, choom_flag

    gonk_flag = True
    choom_flag = True
    choom_list = config['chooms']
    gonk_list = config['gonks']
    # birthday_list = config['birthdayBoy'] if config['birthdayBoy'] else []

    client.run(token)


if __name__ == "__main__":
    main()

