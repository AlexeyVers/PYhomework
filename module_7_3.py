class WordsFinder:
    def __init__(self, file_names):
        self.file_names = [file_names]
        if isinstance(file_names, list):
            for i in file_names:
                self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        cleaning = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                for line in file:
                    for i in cleaning:
                        line_clean = line.lower().replace(i, '').split()
                    if not all_words.get(name, False):
                        all_words[name] = line_clean
                    else:
                        all_words[name].extend(line_clean)
        return all_words

    def find(self, word):
        find_text = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    find_text[name] = i+1
                    break
        return find_text

    def count(self, word):
        find_text = {}
        count_words = 0
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    count_words += 1
            find_text[name] = count_words
        return find_text

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
