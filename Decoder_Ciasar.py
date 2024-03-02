"""Декодирование Цезаря"""

alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у",
            "ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"] # список алфавит

STEP = 30 

phraze = str(input()) # запрос фразы 
result = "" # переменная результат 

for item in phraze:
    try:
        current_index = alphabet.index(item.lower())
        if current_index + STEP > len(alphabet):
            new_index = current_index + STEP - len(alphabet)
        else: 
            new_index = current_index + STEP 
        result += alphabet[new_index]
    except ValueError:
        result += item
print(f"Result:{result}")
word = result

#табуретка


def get_char(hashed_char,to_the_left):
    current_index = alphabet.index(hashed_char.lower())
    new_char_index = current_index - to_the_left
    return alphabet[new_char_index]

for index in range(1 , len(alphabet)):
    result = ""
    for hashed_char in word:
        result += get_char(hashed_char , index)
    print(result)





