import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses

# Load token

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str):
    if not user_message:
        print('(Mesage was empty because Intent were not enable probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


# Handle startup for the bot

@client.event
async def on_ready():
    print(f'{client.user} is connected')


# Handling incoming messages

@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# MAIN ENTRY
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
