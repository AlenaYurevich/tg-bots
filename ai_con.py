from openai import OpenAI

client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)


def chat_with_ai():
    print("Добро пожаловать в чат с нейросетью! Введите 'exit' для выхода.")
    messages = []

    while True:
        user_input = input("Вы: ")
        if user_input.lower() == 'exit':
            print("До свидания!")
            break

        # Добавляем сообщение пользователя в список сообщений
        messages.append({"role": "user", "content": user_input})

        # Создаем запрос к API
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106", messages=messages
        )

        # Получаем ответ от модели
        ai_response = chat_completion.choices[0].message.content
        print(f"AI: {ai_response}")

        # Добавляем ответ модели в список сообщений
        messages.append({"role": "assistant", "content": ai_response})


if __name__ == "__main__":
    chat_with_ai()
