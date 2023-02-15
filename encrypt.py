lang = input('Выберите язык (рус - 1/en - 2): ') # выбор языка для шифорвания/дешифрования текста
encrypt = input('Что будем делать: шифровать (1) или расшифровывать (2)?: ')
#step = int(input('Введите шаг сдвига: '))
print('Хорошо. Напишите текст для обработки: ')
text = input().split()
print(text)


def encryption_en(text):
    text_new = ''
    for j in range(len(text)):
        step = 0
        for k in text[j]:
            if k.isalpha():
                step += 1
        for i in text[j]:
            if 65 <= ord(i) <= (90 - step) or 97 <= ord(i) <= (122 - step):
                text_new += chr(ord(i) + step)
            elif ord(i) > (90 - step):
                text_new += chr(ord(i) - (26 - step))
            else:
                text_new += i
        text_new += ' '
    return text_new


def encryption_ru(step, text):
    text_new = ''
    for i in text:
        if 1040 <= ord(i) <= (1071 - step) or 1072 <= ord(i) <= (1103 - step):
            text_new += chr(ord(i) + step)
        elif ord(i) > (1071 - step):
            text_new += chr(1039 + (step - (1071 - ord(i))))
        else:
            text_new += i
    return text_new


def decryption_en(step, text):
    text_new = ''
    for i in text:
        if (65 + step) <= ord(i) <= 90 or (97 + step) <= ord(i) <= 122:
            text_new += chr(ord(i) - step)
        elif 64 < ord(i) < (65 + step) or 96 < ord(i) < (97 + step):
            text_new += chr((ord(i) + 26 - step))
        else:
            text_new += i
    return text_new


def decryption_ru(step, text):
    text_new = ''
    for i in text:
        if (1040 + step) <= ord(i) <= 1071 or (1072 + step) <= ord(i) <= 1103:
            text_new += chr(ord(i) - step)
        elif 1039 < ord(i) < (1040 + step) or 1071 < ord(i) < (1103 + step):
            text_new += chr((ord(i) + 32 - step))
        else:
            text_new += i
    return text_new


if lang == '2' and encrypt == '1':
    print(encryption_en(text))
if lang == '1' and encrypt == '1':
    print(encryption_ru(step, text))
if lang == '2' and encrypt == '2':
    print(decryption_en(step, text))
if lang == '1' and encrypt == '2':
    print(decryption_ru(step, text))