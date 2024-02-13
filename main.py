import requests
from functools import reduce
def get_info():
    req = requests.get('https://fakestoreapi.com/products/')
    res = req.json()
    return res

'''def summ (a,b):
    return a + b['price']
products = get_info()
result = reduce (summ, products, 0)
print (result)'''
products = get_info()
products_price = reduce(lambda x, y : x + y['price'], products, 0)
products_category= filter(lambda x : x['price'] <=20, products)
print(products_price)
print(list(products_category))