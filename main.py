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

    global gonk_flag,choom_flag,birthday_list

    content = message.content.lower()

    if content == "uber gay":
        await message.channel.send(
            "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo. ")

    elif content == "!stop gonk":
        gonk_flag = False

    elif content == "!go gonk":
        gonk_flag = True

    elif content == "!stop choom":
        choom_flag = False

    elif content == "!go choom":
        choom_flag = True

    elif "!birthday" in content:
        negator = content[10:13]
        print(f'negator: {negator}')
        if negator == "not":
            person = content[14:]
            if person in birthday_list:
                birthday_list.remove(person)
        else:
            person = content[10:]
            if person not in birthday_list:
                birthday_list.append(person)
            print(person)

    author_name = message.author.name.lower()
    author_discriminator = message.author.discriminator

    for choom in choom_list:
        if choom_flag and choom['name'] == author_name and choom['discriminator'] == author_discriminator:
            await react_choom(message)

    for gonk in gonk_list:
        if gonk_flag and gonk['name'] == author_name and gonk['discriminator'] == author_discriminator:
            await react_gonk(message)

    print(f'{birthday_list} is list, name: {author_name} ')
    if birthday_list and author_name.lower() in birthday_list:
        await message.add_reaction('🎂')
        await message.add_reaction('🕺')
        await message.add_reaction('🎉')



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

    global choom_list, gonk_list, gonk_flag, choom_flag, birthday_list

    gonk_flag = True
    choom_flag = True
    choom_list = config['chooms']
    gonk_list = config['gonks']
    birthday_list = config['birthdayBoy'] if config['birthdayBoy'] else []
    token = config['auth_token']

    client.run(token)


if __name__ == "__main__":
    main()

