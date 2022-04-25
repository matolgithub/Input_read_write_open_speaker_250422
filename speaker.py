import pyttsx3

def speaker(text):
    speaker = pyttsx3.init()  # инициализация движка

    # зададим свойства
    speaker.setProperty('rate', 150)  # скорость речи
    speaker.setProperty('volume', 0.9)  # громкость (0-1)

    speaker.say(f"{text}")  # запись фразы в очередь
    speaker.runAndWait()


# def speaker(speaker_name='Анджелина Джоли', user_name='Олег', number=2):
#     speaker = pyttsx3.init()  # инициализация движка
#
#     # зададим свойства
#     speaker.setProperty('rate', 150)  # скорость речи
#     speaker.setProperty('volume', 0.9)  # громкость (0-1)
#
#     # speaker.say(f"My name is {speaker_name}. I can speak, it's important for you, {user_name}!")  # запись фразы в очередь
#     speaker.say(f"Меня зовут {speaker_name}. Я могу говорить! Это важно для тебя, {user_name}.")  # запись фразы в очередь
#     speaker.say(f"Я умею хорошо считать до {number}дцати.")
#     for i in range(1, number*10 + 1):
#         speaker.say(f'{i}')
#         time.sleep(0.1)
#     # очистка очереди и воспроизведение текста
#     speaker.runAndWait()
#
# speaker()

