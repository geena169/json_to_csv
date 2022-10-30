# Поиск ключей со значениями в файле.

# Главная проблема заключалась в json объектах, заключенных в массивах, и в их "беспорядочности".
# Файл переписывается в json файл с простой структурой (раскрыты вложенные объекты и масcивы с объектами)
# Ex:

#{
#    "createdAt": "2020-05-24T20:26:39+00:00",
#    "customer": {
#      "id": 35786260,
#      "email": null,
#      "cookie": null,
#      "install": {
#        "id": null,
#        "deviceId": null,
#        "instanceId": null
#      },
#    }
#}

# Преобразовывается в вид:
#{"createdAt": "2020-05-24T20:26:39+00:00","customer_id": 35786260,"customer_email": null,"customer_cookie": null,"customer_install_id": null,"customer_install_deviceId": null,"customer_install_instanceId": null}

# На выходе получается файл из которого удобно и быстро формируется csv файл и список всех ключей в файле


import json

def json_modify(json_input,file_output_name : str):

    obj_res = json.loads(json_input)
    
    while True:
        obj = obj_res.copy()
        del_list = []
        for i in obj:
            if type(obj.get(i)) is dict:
                del_list.append(i)
                obj_res.update({str(i)+"_"+str(j): obj[i][j] for j in obj[i]})
            elif type(obj.get(i)) is list and len(obj.get(i)):
                if type(obj.get(i)[0]) is dict:
                    del_list.append(i)
                    for j in obj[i]:
                        last_key = ''
                        for k,v in j.items():
                            if not v in (None, [], False):
                                last_key = str(i)+"_"+str(k)
                                
                                if obj_res.get(last_key,True): # Если такого ключа нет
                                    obj_res.setdefault(last_key,'')
                                
                                if type(v) is dict:
                                    obj_res[str(i)+"_"+str(k)] = v
                            
                                else:
                                    if not obj_res[last_key]:  # Если объект пустой, то вписываем значение, иначе через запятую
                                        obj_res[last_key] = str(v)
                                    else:
                                        obj_res[last_key] = str(obj_res.get(last_key,'')) + ',' + str(v)
                                    obj_res[last_key] = str(obj_res[last_key]).replace('[','').replace(']','').replace("'",'')
                else:
                    obj_res[i] = str(obj_res[i])[2:-2]
                                    

        for i in del_list:
            del obj_res[i]
        
        out_ = True
        for i in obj_res:     
            if type(obj_res.get(i)) is (dict or list):
                out_ = False
                continue
        if out_:
            break


    str_ = "\n" + json.dumps(obj_res)
    
    
    with open(file_output_name,'a+', encoding="utf-8") as f:
        f.write(str_)

    return obj_res.keys()
