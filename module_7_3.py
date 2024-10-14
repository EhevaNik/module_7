class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    # подготовительный метод, который возвращает словарь следующего вида:
    # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    # Где: 1. 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    # 2. ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
    def get_all_words(self):
        all_words = {} # пустой словарь
        l = '' #
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punctuation:
                        line = line.replace(i, '')
                l = l + line
            all_words.update({self.file_names: l.split()})
            return all_words

    # метод find(self, word), где word - искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - позиция первого такого слова в списке слов этого файла.
    def find(self, word):
        dict1 = {}
        world = self.get_all_words()[self.file_names]
        for i in range(len(world)):
            if word.lower() == world[i]:
                dict1.update({self.file_names: i + 1})
                return dict1

    # метод count(self, word), где word - искомое слово. Возвращает словарь, где ключ - название файла,
    # значение - количество слова word в списке слов этого файла.
    def count(self, word):
        dict2 = {}
        n = 1
        world = self.get_all_words()[self.file_names]
        dict2.update({self.file_names: world.count(word.lower())})
        return dict2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
