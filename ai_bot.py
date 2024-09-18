import telebot
from openai import OpenAI
from access import My_key, My_token

# Инициализация OpenAI клиента
client = OpenAI(
    api_key=My_key,
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация Telegram бота
TOKEN = My_token
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения сообщений пользователей
user_messages = {}


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id

    # Инициализация списка сообщений для каждого пользователя
    if user_id not in user_messages:
        user_messages[user_id] = []

    # Добавляем сообщение пользователя в список сообщений
    user_messages[user_id].append({"role": "user", "content": message.text})

    # Создаем запрос к API
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106", messages=user_messages[user_id]
    )

    # Получаем ответ от модели
    ai_response = chat_completion.choices[0].message.content

    # Отправляем ответ пользователю
    bot.send_message(user_id, ai_response)

    # Добавляем ответ модели в список сообщений
    user_messages[user_id].append({"role": "assistant", "content": ai_response})


# Запуск бота
bot.polling()
