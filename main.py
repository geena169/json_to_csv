# Основной скрипт

# В указанной папке программа находит все файлы для обработки и по очереди их обрабатывает

import sys
import os
import json

from get_json_line import *
from get_title import get_title
from json_modify import json_modify
from str_replace import str_del_spec_symbols


file_path_in = 'In/LinkedIn/'
file_path_out_csv = 'In/LinkedIn_out/csv/'
file_path_out_keys = 'In/LinkedIn_out/keys/'
file_path_out_json = 'In/LinkedIn_out/json/'
file_in = ''
file_json = 'json_mod.json'
file_out = 'res.csv'


keys_sum = set() # Список всех уникальных ключей в файле


def del_trash():
    
    dirs_ = (file_path_out_csv, file_path_out_keys, file_path_out_json)

    for d in dirs_:
        files_ = os.listdir(d)
        if files_:
            for f in files_:
                os.remove(d+f)

def file_input():

    files_ = os.listdir(file_path_in)
    return files_


def json_format(fi):

    global keys_sum
    
    df = json_line_from_gz(file_path_in + fi)

    #Приведение json файла к виду списка без вложений#
    obj = [] # Обработанный файл
    
    
    i=0
    while (res := next(df,False)):

        if i == 10000:
            break
        
        keys = json_modify(res,file_path_out_json + 'json_mod_' + fi.split('.')[0] + '.json')
        
        keys_sum = keys_sum.union(keys)
        i+=1
        
    print(sorted(keys_sum))
    keys_str = ''
    for k in sorted(keys_sum):
        keys_str += k + '\t'
    
    with open(file_path_out_keys + 'keys_' + fi.split('.')[0] + '.txt','w',encoding='utf-8') as f:
        f.write(keys_str.rstrip('\t'))
        
    return print('\nФайл {file_in} успешно приведен к обрабатываему формату\n')

# Формирование конечного csv файла
def get_csv():

    jf = json_line(file_path_out_json + 'json_mod_' + fi.split('.')[0] + '.json')
    #Пропуск шапки файла#
    line = next(jf)
    
    while (line:= next(jf,False)):
        
        # Удаление спецсимволов ('\n' и тд)
        line = str_del_spec_sumbols(line)
        
        obj_json = json.loads(line)

        _str = ""
        # Приведение пустых значений к единому формату
        for id_, key in sorted(keys_sum.items()):
            s_ = str_del_spec_symbols(str(obj_json.get(key,'None')))
            if s_ in ('None','[]','',"''"):
                s_ = '""'
            _str += s_ + "\t"
        _str = _str.rstrip('\t')
        _str += "\n"

        
        with open(file_path_out_csv+'res_'+fi.split('.')[0]+'.csv','a', encoding='utf-8') as f:
            f.write(_str)
    
    return print('\nКонечный {res.csv} сформирован')


if __name__ == '__main__':
    # Удаление старых файлов обработки
    del_trash()
    
    files_ = file_input()
    print(files_)
    for fi in files_:
        keys_sum = set()
        json_format(str(fi))        
        #Формирование шапки .csv файла#
        keys_sum = get_title(file_path_out_csv+'res_'+fi.split('.')[0]+'.csv',keys_sum)
        #Формирование конечного csv файла#
        get_csv()


