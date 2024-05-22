import time
import datetime

ENEMY_NAME = "Мстислав"
PLAYER_NAME = "Marina"
OWNER_NAME = "Lucas"


def speak(sentence, sleep):
    type(sentence, sleep)
    print("", flush=True)

    if sleep:
        time.sleep(1.5)


def enemy_speak(sentence):
    print(get_time_now() + " [" + get_enemy_name() + "]: ", end="", flush=True)
    speak(sentence, True)


def enigma_speak(sentence, number):
    print(get_time_now() + " [" + get_cyan_text("ENIGMA" + str(number)) + "]: ", end="", flush=True)
    speak(sentence, True)


def system_speak(sentence):
    print(get_time_now() + " [" + get_green_text("SYSYEM") + "]: ", end="", flush=True)
    speak(sentence, False)


def player_input():
    print(get_time_now() + " [" + get_yellow_text(PLAYER_NAME) + "]: ", end="", flush=True)

    while True:
        try:
            answer = str(input(""))
            return answer
        except ValueError:
            system_speak("Digite uma resposta válida!")
            continue


def player_speak(sentence, player):
    if player:
        print(get_time_now() + " [" + get_yellow_text(PLAYER_NAME) + "]: ", end="", flush=True)
    else:
        print(get_time_now() + " [" + get_purple_text(OWNER_NAME) + "]: ", end="", flush=True)

    speak(sentence, True)


def type(sentence, sleep):
    for letter in sentence:
        print(letter, end="", flush=True)

        if sleep:
            time.sleep(0.05)


def get_time_now():
    time_now = datetime.datetime.now()
    time_format = time_now.strftime("%H:%M:%S")
    return time_format


def get_red_text(text):
    return "\033[91m" + text + "\033[0m"

def get_purple_text(text):
    return "\033[95m" + text + "\033[0m"

def get_cyan_text(text):
    return "\033[96m" + text + "\033[0m"

def get_green_text(text):
    return "\033[92m" + text + "\033[0m"

def get_yellow_text(text):
    return "\033[93m" + text + "\033[0m"


def get_enemy_name():
    return get_red_text(ENEMY_NAME)
