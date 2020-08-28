print("hello   2222")

from telethon import TelegramClient, events

api_id = 1633358
api_hash = 'afce4fe5707b69508bfc66cbe116ed73'
client = TelegramClient('+380951112154', api_id, api_hash)


listen_for_ids = (
    1073702594,
)

forward_to_ids = (
    -1001243390227,
)


@client.on(events.NewMessage)
async def my_event_handler(message):
    if message.sender_id in listen_for_ids:
        for receiver_id in forward_to_ids:
            sender = await message.get_sender()
            await client.send_message(
                receiver_id,
                f'Отримано сигнал. Канал: {sender.username} (id: {sender.id})!\nВМІСТ: (лише текст)\n{message.raw_text}'
            )

client.start()
print(f'Started. Listening for IDs: {listen_for_ids}')
print(f'Forwarding to IDs: {forward_to_ids}')
client.run_until_disconnected()