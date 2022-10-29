import os


file_path = 'In/LinkedIn_out/csv/'
files_ = os.listdir(file_path)
for fi in files_:
    with open(file_path+fi, encoding='utf-8') as f:
        i = 0
        a =[]
        b = {}
        stok = 0
        for line in f:
            x = len(line.split('\t'))
            if i == 0:
                stok = x
            if x != stok:
                b[i] = line
            i+=1
            
        if not b:
            print(f"Кривых строк в файле {fi} нет")
        else:
            print(b)

            f_out = f'bad_strs{fi}.txt'
            with open(f_out,'w',encoding='utf-8') as f:
                i = 0
                for k,v in b.items():
                    
                    s_ = f'{stok=} {len(b.keys())=}' + " <- " + str(k)+": "+str(v)
                    f.write(s_)
                    f.write('\n')

    
