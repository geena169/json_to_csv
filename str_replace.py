# Удаление спецсимволов из строки

def str_del_spec_symbols (_str : str):
    replace_values = {"\n": "", "\t": "", "\r": ""}
    for i, j in replace_values.items():
        _str = _str.replace(i, j)

    return _str

