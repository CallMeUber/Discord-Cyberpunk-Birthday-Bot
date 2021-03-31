import yaml
import discord

client = discord.Client()


def get_config():
    try:
        with open('./config.yml') as file:
            return yaml.full_load(file)
    except IOError:
        print("Could not read the file")
        return None


@client.event
async def on_message(message):

    global gonk_flag,choom_flag

    if message.content.lower() == "uber gay":
        await message.channel.send(
            "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo. ")

    elif message.content == "!STOP GONK":
        gonk_flag = False

    elif message.content == "!GO GONK":
        gonk_flag = True

    elif message.content == "!STOP CHOOM":
        choom_flag = False

    elif message.content == "!GO CHOOM":
        choom_flag = True

    author = message.author
    for choom in choom_list:
        if choom_flag and choom['name'] == author.name and choom['discriminator'] == author.discriminator:
            await react_choom(message)

    for gonk in gonk_list:
        if gonk_flag and gonk['name'] == author.name and gonk['discriminator'] == author.discriminator:
            await react_gonk(message)


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
    config = get_config()

    if config is None:
        return

    global choom_list, gonk_list, gonk_flag, choom_flag

    gonk_flag = True
    choom_flag = True
    choom_list = config['chooms']
    gonk_list = config['gonks']
    token = config['auth_token']

    client.run(token)


if __name__ == "__main__":
    main()

