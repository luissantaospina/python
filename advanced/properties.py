# Without properties
class User:
    def __init__(self, name: str, phone: float):
        self._name = name
        self._phone = phone

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def get_name(self) -> str:
        return self._name

    def set_phone(self, new_phone: float) -> None:
        self._phone = new_phone

    def get_phone(self) -> float:
        return self._phone


user = User('Luis', 3103830717)
user.set_name('Fernando')
user.set_phone(3127211873)
user.get_name()
user.get_phone()


# With properties
class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def get_name(self) -> str:
        return self._name

    def del_name(self):
        del self._name

    def set_price(self, new_price: float) -> None:
        self._price = new_price

    def get_price(self) -> float:
        return self._price

    def del_price(self):
        del self._price

    product_name = property(
        fget=get_name,
        fset=set_name,
        fdel=del_name,
        doc='The product name property'
    )

    product_price = property(
        fget=get_price,
        fset=set_price,
        fdel=del_price,
        doc='The product price property'
    )


product = Product('Proteina', 50000)
print(product.product_name)
print(product.product_price)
product.product_name = 'Fresas'
product.product_price = 5000
print(product.product_name)
print(product.product_price)
del product.product_name
del product.product_price
print(product.product_name)
print(product.product_price)
