#Автор https://github.com/vetprogs
#По вопросам и предложениям:  vetprogs(сoбakа)etlgr.com
#Внимание - использование подобных скриптов может привести к бану Вашего телеграмм аккаунта!

from telethon import TelegramClient, sync, events

api_id = 123
api_hash = 'qwe'   # получать тут: https://my.telegram.org/apps

client = TelegramClient('my_telega', api_id, api_hash)  #лучше запускать на зарубежных vds чтобы не было блокировок.

chat_to_spy = 'public_chat'       #название чата без @, для приватных чатов - id чата (цифры)
mychat_id = 12345                 #id или username своего чата/канала, Куда будем пересылать сообщения, для канала нужны права на постинг

@client.on(events.NewMessage(chats=(chat_to_spy)))  #фильтр по чату группы
async def mysend_handler(event):
    await event.message.forward_to(mychat_id)       #переслать себе  

 
print('Start load spy!')
client.start()
print('Press Ctrl+C to stop this')
client.run_until_disconnected()
