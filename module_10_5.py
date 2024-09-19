#12
import multiprocessing
import datetime

def read_info(name):
    all_data = []
    read_ = open(name, 'r', encoding='utf-8')
    while True:
        if read_.readline():
            all_data += read_.readline()
        else:
            break
    read_.close()
if __name__ == '__main__':
    now_ = datetime.datetime.now()
    for i in range(4):
        read_info(f'file {i+1}.txt')
    before_ = datetime.datetime.now()
    print(f'slow - {before_ - now_}')


    file_name = []
    for i in range(4):
        file_name.append(f'file {i + 1}.txt')


    with multiprocessing.Pool(processes=6) as pool:
        now_2 = datetime.datetime.now()
        pool.map(read_info, file_name)
        before_2 = datetime.datetime.now()
        print(f'fast - {before_2 - now_2}')
