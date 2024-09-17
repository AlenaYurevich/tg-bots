import telebot
from telebot.apihelper import ApiTelegramException

# Вставьте ваш токен, полученный от @BotFather
API_TOKEN = '7526041600:AAG0KoBYbo2hkhnAiB2UFR6-td3JRPI7ZNs'


# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш бот. Как я могу вам помочь?")


# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Я умею выполнять следующие команды:\n"
        "/start - начать работу с ботом\n"
        "/help - получить помощь\n"
        "/perevorot - перевернуть текст\n"
        "/caps - преобразовать текст в заглавные буквы\n"
        "/cut - удалить все гласные из текста\n"
        "/translit - преобразовать текст в транслит\n"
    )
    bot.reply_to(message, help_text)


# Обрабатываем команду /perevorot
@bot.message_handler(commands=['perevorot'])
def handle_perevorot(message):
    try:
        # Извлекаем текст после команды
        original_text = message.text[len('/perevorot '):]
        # Переворачиваем текст
        reversed_text = original_text[::-1]
        # Возвращаем перевернутый текст
        bot.reply_to(message, reversed_text)
    except ApiTelegramException:
        bot.reply_to(message, "Напиши текст после команды /perevorot в одном сообщениии")


# Обрабатываем команду /caps
@bot.message_handler(commands=['caps'])
def handle_caps(message):
    try:
        # Извлекаем текст после команды
        original_text = message.text[len('/caps '):]
        # Преобразуем текст в заглавные буквы
        caps_text = original_text.upper()
        # Возвращаем текст в заглавных буквах
        bot.reply_to(message, caps_text)
    except ApiTelegramException:
        bot.reply_to(message, "Напиши текст после команды /caps в одном сообщениии")


# Обрабатываем команду /cut
@bot.message_handler(commands=['cut'])
def handle_cut(message):
    try:
        # Извлекаем текст после команды
        original_text = message.text[len('/cut '):]
        # Определяем гласные буквы
        vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
# Удаляем гласные
        cut_text = ''.join(char for char in original_text if char not in vowels)
        # Возвращаем текст без гласных
        bot.reply_to(message, cut_text)
    except ApiTelegramException:
        bot.reply_to(message, "Напиши текст после команды /cut в одном сообщении")


# Функция для транслитерации
def translit(text):
    # Простейшая схема транслитерации
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
        'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }
    return ''.join(translit_dict.get(char, char) for char in text)


# Обрабатываем команду /translit
@bot.message_handler(commands=['translit'])
def handle_translit(message):
    try:
        # Извлекаем текст после команды
        original_text = message.text[len('/translit '):]
        # Преобразуем текст в транслит
        translit_text = translit(original_text)
        # Возвращаем транслитерированный текст
        bot.reply_to(message, translit_text)
    except ApiTelegramException:
        bot.reply_to(message, "Напиши текст после команды /translit в одном сообщении")


if __name__ == '__main__':
    # Запуск бота
    bot.polling(none_stop=True)
