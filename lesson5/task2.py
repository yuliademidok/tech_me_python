"""2
Дан словарь с кодированием строк азбуки Морзе
2.1 Реализовать функцию кодирующую текст в морзе строку на вход которой подается строка текста, в ответ возвращается
строка закодированная азбукой морзе. В качестве разделителя морзе символов использовать пробел.
Пробел кодируется тоже как пробел
2.2 Реализовать функцию декодирующую морзе строку обратно в читаемый текст.
Обратите внимание что используется только символы латинского Алфавита в lower case.
При этом строка должна всегда начинаться с заглавной буквы
"""

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def encode_morse(user_text, cipher=None):
    if cipher is None:
        cipher = MORSE

    reversed_cipher = {v: k for k, v in cipher.items()}
    result = ""

    for i in user_text.lower():
        if i in cipher.values():
            result += (reversed_cipher[i] + " ")
        else:
            result += i

    return result


print(encode_morse("Lorem Ipsum is simply dummy text"))


def decode_morse(user_text, cipher=None):
    if cipher is None:
        cipher = MORSE

    reversed_cipher = {v: k for k, v in cipher.items()}
    user_text_arr = user_text.split(' ')
    result = ""

    for i in user_text_arr:
        if i in reversed_cipher.values():
            result += cipher[i]
        else:
            result += ' '

    return result.capitalize()


print(decode_morse(".-.. --- .-. . --  .. .--. ... ..- --  .. ...  "
                   "... .. -- .--. .-.. -.--  -.. ..- -- -- -.--  - . -..- - "))
