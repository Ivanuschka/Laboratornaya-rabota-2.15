def read_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Читаем первые три предложения из файла
        sentences = [file.readline().strip() for _ in range(3)]
    return sentences

def reverse_and_print(sentences):
    # Выводим предложения в обратном порядке
    for sentence in reversed(sentences):
        print(sentence)

if __name__ == "__main__":
    file_path = "C:\\Users\\ivana\\OneDrive\\Рабочий стол\\Иван\\Laboratornaya-rabota-2.15\\one.txt"

    try:
        # Читаем три предложения из файла
        sentences = read_sentences(file_path)

        # Выводим предложения в обратном порядке
        reverse_and_print(sentences)

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
