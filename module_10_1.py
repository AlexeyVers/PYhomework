from threading import Thread
from time import sleep
from datetime import datetime
def write_words(word_count, file_name):
    write_ = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        write_.write(f'Какое-то слово № {i+1}\n')
        sleep(0.1)
    write_.close()
    print(f'Заверщилкась запись в файл {file_name}')

now_ = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
before_ = datetime.now()

print(before_ - now_)



now_ = datetime.now()
first = Thread(target=write_words, args=(10,  'example1.txt',))
second = Thread(target=write_words,args=(30, 'example2.txt', ))
thid = Thread(target=write_words,args=(200, 'example3.txt', ))
fourth = Thread(target=write_words, args=(100, 'example4.txt', ))

first.start()
second.start()
thid.start()
fourth.start()

first.join()
second.join()
thid.join()
fourth.join()
before_ = datetime.now()

print(before_ - now_)
