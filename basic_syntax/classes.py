class NumberOperations:

    def __init__(self, num):
        self.num=num

    def compare(self):
        if self.num > 0:
            print('El numero es positivo')
        elif self.num < 0:
            print('El nunmero es negativo')
        else: 
            print('El numero es cero')

    def cicle(self):
        while self.num <= 10:
            print(self.num)
            self.num += 1

callClass = NumberOperations(0)
callClass.compare()
callClass.cicle()