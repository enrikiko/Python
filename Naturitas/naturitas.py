# definir objetos
class Stock(object):
    total = []

def new_stock():
    product = Stock()
    product.total = []
    return product

class Product(object):
    price = 0
    title = ''
    quatity = 15

def new_product(price, title):
    product = Product()
    product.price = price
    product.title = title
    product.quantity = 15
    return product

# crear los objetos
stock = new_stock()
patatas = new_product(3,'papatas')
stock.total.insert(0,patatas)
peras = new_product(2,'peras')
stock.total.insert(0,peras)
manzanas = new_product(4,'manzanas')
stock.total.insert(0,manzanas)

# Funciones:
def sell_product(product):
    product.quantity = product.quantity - 1
    print('Se ha realizado una compra')
    print('El stock actual es de: ',product.quantity)
    check_stock(product)
def check_stock(product):
    if product.quantity <= 10:
        product.quantity = product.quantity + 5
        print('El stock ha sido incrementado')
def valor_product(product):
    print('El valor de ',product.title,' es de:',product.price,'euros')

def stocktotal_stock(stock):
    print('El stock actual es el siguente:')
    for element in range(len(stock.total)):
        print(stock.total[element].title, stock.total[element].quantity)
def valortotal_stock(stock):
    total=0
    for element in range(len(stock.total)):
        total = total + stock.total[element].price * stock.total[element].quantity
    print('El valor del stock es de ',total, 'euros')

# interacion con usuario

print('Bienvenido a Naturitas,')
print('Teclee  "venderpatatas"  para vender patatas  ')
print('Teclee  "valorpatatas"  para ver el valor de las patatas  ')
print('Teclee  "vendermanzanas"  para vender manzanas  ')
print('Teclee  "valormanzanas"  para ver el valor de las manzanas  ')
print('Teclee  "venderperas"  para vender peras ')
print('Teclee  "valorperas"  para ver el valor de las peras ')
print('Teclee  "stocktotal"  para ver el stock total en el almacen ')
print('Teclee  "valortotal"  para ver el valor del stock total en el almacen ')
response=" "
while response !="":
    response = raw_input("Que desea hacer ")
    if response == "venderpatatas":
        sell_product(patatas)
    if response == "valorpatatas":
        valor_product(patatas)
    if response == "venderperas":
        sell_product(peras)
    if response == "valorperas":
        valor_product(peras)
    if response == "vendermanzanas":
        sell_product(manzanas)
    if response == "valormanzanas":
        valor_product(manzanas)
    if response == "stocktotal":
        stocktotal_stock(stock)
    if response == "valortotal":
        valortotal_stock(stock)
