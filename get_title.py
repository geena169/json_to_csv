# Создание шапки csv файла и определение необходимых полей(отдельно для каждого csv файла)

# в файле 'title.tx' записываются поля
# Ex:
#   birth_date
#   birth_year
#   certifications
#   certifications_end_date
#   certifications_name

# Необходимые поля оставляем, ненужные удаляем из файла, можно поменять местами поля. Если необходимо поменять имя поля для БД напротив поля добавить ':name'
# Ex:
#   birth_year
#   birth_date
#   certifications_name:promo

# Если заранее известно, что ничего менять не нужно, комментируем 32 строчку

def get_title(file_name, keys_in):
    keys_out = {}
    keys_out_str = ""
    BD_keys = ""
    keys_str = ""
    for k in sorted(keys_in):
        #print(k)
        keys_str += str(k) + '\n'
    keys_str = keys_str.rstrip('\n')
    with open('title.txt','w') as f:
        f.write(keys_str)
    print("В файле 'title.txt' оставьте необходимые ключи следущием формале:\nKey1:Table key1\nKey2:Table key2\n.............\nKey999:Table key999\nгде Key - ключ из исходного файла,\nTable key - имя будущего поля в БД")
    
    input("Нажмите любую клавишу после обработки файла")

    #!!!!!!title1 для проверки!!!!!!#
    with open("title.txt",'r',encoding='utf-8') as f:
        i = 0
        for line in f:
            sep_ind = line.find(':')
            keys_out[i] = line[:sep_ind]
            keys_out_str += line[:sep_ind] + '\t'
            BD_keys += line[sep_ind+1:-1] + " VARCHAR2(300),\n"
            i+=1
    #print(BD_keys)
    keys_out_str = keys_out_str.rstrip('\t') + '\n'
    BD_keys = BD_keys.rstrip(",\n")
    sql_get = f"CREATE TABLE (table_name) (\n{BD_keys}\n)"
    with open("sql-запрос на формирование БД.txt",'w',encoding='utf-8') as f:
        f.write(sql_get)
    print("sql-запрос сформирован в файл 'sql-запрос на формирование БД.txt'")

    with open(file_name, 'w', encoding='utf-8') as f:
            f.write(keys_out_str)

    return keys_out


