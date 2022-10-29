# Построчное чтение файла с помощью генератора

from gzip import open as gz_open

def json_line(file_name):
    
    with open(file_name, encoding="UTF-8") as f:
        for line in f:
            yield line


def json_line_from_gz(file_name):

    with gz_open(file_name, 'rt', encoding="UTF-8") as f:
        for line in f:
            yield line
