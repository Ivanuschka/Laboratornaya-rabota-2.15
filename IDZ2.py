import re
def find_longest_word(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            words = re.findall(r'\S+', content)

            longest_length = max(len(word) for word in words)
            longest_words = [word for word in words if len(word) == longest_length]
            print(f"Длина самого длинного слова: {longest_length}")
            print(f"Слова такой длины: {', '.join(longest_words)}")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = "C:\\Users\\ivana\\OneDrive\\Рабочий стол\\Иван\\Laboratornaya-rabota-2.15\\two.txt"
# Вызываем функцию для нахождения самого длинного слова
find_longest_word(file_path)
