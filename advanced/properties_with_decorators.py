# With properties and decorators
class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        self._price = new_price

    @price.deleter
    def price(self):
        del self._price


product = Product('Sandia', 100000)
product.name = 'Fresas'
product.price = 5000
del product.name
del product.price


# With properties and decorators, only reading
class PurchaseCase:
    def __init__(self, code: str, tax_fee: float):
        self._code = code
        self._tax_fee = tax_fee

    @property
    def code(self) -> str:
        return self._code

    @property
    def tax_fee(self) -> float:
        return self._tax_fee


purchase_case = PurchaseCase('CO123', 100000)


# With properties and decorators, only writen
class SellCase:
    def __init__(self, code: str, tax_fee: float):
        self._code = code
        self._tax_fee = tax_fee

    @property
    def code(self) -> str:
        raise AttributeError('Code is only writen')

    @code.setter
    def code(self, new_code: str) -> None:
        self._code = new_code

    @property
    def tax_fee(self) -> float:
        raise AttributeError('Tax fee is only writen')

    @tax_fee.setter
    def tax_fee(self, new_tax_fee: float) -> None:
        self._tax_fee = new_tax_fee


sell_case = SellCase('SE123', 100000)
sell_case.code = 'TY856'
sell_case.tax_fee = 4585


# Example
class Rectangle:
    def __init__(self, height: float, width: float):
        self._height = height
        self._width = width

    @property
    def area(self) -> float:
        return self._height * self._width


rectangle = Rectangle(10, 2)
print(rectangle.area)
