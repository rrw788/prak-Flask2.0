class Product:
    def __init__(self, id, name, price, stock, image):
        self.id = id 
        self.name = name
        self.price = price
        self.stock = stock
        self.image = image

products = [
    Product(1, 'T-34', 10000, 10, 'images/T_34.jpg'),
    Product(2, 'Panther ausf B', 20000, 5, 'images/Panther.jpg'),
    Product(3, 'Strv 74', 15000, 8, 'images/Strv74.jpg'),
    Product(4, 'Cromwell', 20000, 9, 'images/cromwell.jpg'),
    Product(5, 'Tiger 1', 50000, 5, 'images/Tiger1.jpg'),
    Product(6, 'IS-2', 25000, 10, 'images/IS2.jpg')
]
        