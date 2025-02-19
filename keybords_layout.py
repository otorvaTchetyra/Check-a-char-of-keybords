def detect_keyboard_layout(char):
    russian_layout = {
        'ф': 'a', 'и': 'b', 'с': 'c', 'в': 'd', 'у': 'e',
        'а': 'f', 'п': 'g', 'р': 'h', 'о': 'i', 'ш': 'j',
        'д': 'k', 'ж': 'l', 'э': 'm', 'я': 'n', 'ч': 'o',
        'с': 'p', 'м': 'q', 'т': 'r', 'ь': 's', 'б': 't',
        'ю': 'u', 'г': 'v', 'ё': 'w', 'л': 'x', 'х': 'y',
        'ц': 'z', 'щ': 'A', 'ъ': 'B', 'Й': 'C', 'Ц': 'D',
        'У': 'E', 'К': 'F', 'Е': 'G', 'Н': 'H', 'Г': 'I',
        'Ш': 'J', 'щ': 'K', 'З': 'L', 'Х': 'M', 'Ъ': 'N',
        'Ф': 'O', 'Ы': 'P', 'В': 'Q', 'А': 'R', 'П': 'S',
        'Р': 'T', 'Л': 'U', 'Д': 'V', 'Ж': 'W', 'Э': 'X',
        'Я': 'Y', 'Ч': 'Z'
    }
    
    english_layout = {
        'a': 'ф', 'b': 'и', 'c': 'с', 'd': 'в', 'e': 'у',
        'f': 'а', 'g': 'п', 'h': 'р', 'i': 'о', 'j': 'ш',
        'k': 'д', 'l': 'ж', 'm': 'э', 'n': 'я', 'o': 'ч',
        'p': 'с', 'q': 'м', 'r': 'т', 's': 'ь', 't': 'б',
        'u': 'ю', 'v': 'г', 'w': 'ё', 'x': 'л', 'y': 'х',
        'z': 'ц'
    }
    
    if char in russian_layout:
        return "Русская раскладка"
    elif char in english_layout:
        return "Английская раскладка"
    else:
        return "Неизвестный символ"

# Пример использования
char_input = input("Введите символ: ")
layout = detect_keyboard_layout(char_input)
print(f"Раскладка клавиатуры: {layout}")