
from telethon import TelegramClient

api_id = 1584723
api_hash = '332a33d701c3740a65ec9d77377fb434'
client = TelegramClient('+380994430922', api_id, api_hash)


async def main():
    me = await client.get_me()
    print(me.stringify())

    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

with client:
    client.loop.run_until_complete(main())