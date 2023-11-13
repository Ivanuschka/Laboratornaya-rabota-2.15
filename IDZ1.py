def reverse_sentences(file_path):
    try:

        with open(file_path, 'r', encoding='utf-8') as file:
            sentences = file.read().split('.')

            sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

            for sentence in reversed(sentences[:3]):
                print(sentence)

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = "C:\\Users\\ivana\\OneDrive\\Рабочий стол\\Иван\\Laboratornaya-rabota-2.15\\one.txt"

reverse_sentences(file_path)
