
"""
def str_del_spec_symbols (_str : str):
    while (x := _str.find("\n")) != -1:
        _str = _str.replace('\n','')
        
    while (x := _str.find("\r")) != -1:
        _str = _str.replace('\r','')
        
    while (x := _str.find("\t")) != -1:
        _str = _str.replace('\t','')
            

    return _str
"""


def str_del_spec_symbols (_str : str):
    replace_values = {"\n": "", "\t": "", "\r": ""}
    for i, j in replace_values.items():
        _str = _str.replace(i, j)

    return _str

