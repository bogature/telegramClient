print("hello")

from telethon import TelegramClient, events

api_id = 1584723
api_hash = '332a33d701c3740a65ec9d77377fb434'
client = TelegramClient('+380994430922', api_id, api_hash)

listen_for_ids = (
    -1001180528587,
)

forward_to_ids = (
    775862240,
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