
from telethon import TelegramClient

api_id = 1633358
api_hash = 'afce4fe5707b69508bfc66cbe116ed73'
client = TelegramClient('+380951112154', api_id, api_hash)


async def main():
    me = await client.get_me()
    print(me.stringify())

    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

with client:
    client.loop.run_until_complete(main())