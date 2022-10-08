import datetime
import json
info = [
    {
        'id': 1,
        'name': 'apple',
        'price': 22,
        # 'dt_now': datetime.datetime.now(),
        'discription': 'red apple',
        'status': True 
    }
]
with open ('info.json', 'w') as my_file:
    json.dump(info, my_file)



def post_product():
    max_id = max([i['id'] for i in info]) 
    new_info = {
        'id': max_id + 1,
        'name': input('Введите имя товара: '),
        'price': int(input('Введите цену: ')),
        'discription': (input('Описание:')),
        'status': True
    }
    info.append(new_info)
    return f'Вы добавли новый товар:\n {new_info}'
post_product()
with open ('info.json', 'w+') as my_file:
    json.dump(info, my_file)
# print(info)
print(post_product())

FILE_PATH  = 'info.json'
def get_data(ge_price = None, le_price = None):
    with open(FILE_PATH) as file:
        data = json.load(file)
    if ge_price:
        new_data = [ i for i in data if  i['price'] >= ge_price]
        return new_data
    if le_price:
        pass
    return data
    
print(get_data(ge_price = 100))