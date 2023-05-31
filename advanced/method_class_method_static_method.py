class Client:
    def method(self):
        return self

    @classmethod
    def class_method(cls):
        return cls

    @staticmethod
    def static_method():
        return None


client = Client()

# print(client.method())
# print(client.class_method())
# print(client.static_method())


class Employee:
    raise_percentage = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary *= self.raise_percentage

    @classmethod
    def set_raise_percentage(cls, percentage):
        cls.raise_percentage = percentage

    @staticmethod
    def is_salary_high(salary):
        return salary > 50000


# Uso de los métodos en la clase Employee
emp1 = Employee("John Doe", 50000)

# Método de instancia
print(emp1.name)  # Imprime "John Doe"
print(emp1.salary)  # Imprime 50000
emp1.apply_raise()
print(emp1.salary)  # Imprime 52500 (50000 * 1.05)

# Método de clase
Employee.set_raise_percentage(1.1)
emp2 = Employee("Jane Smith", 60000)
emp2.apply_raise()
print(emp2.salary)  # Imprime 66000 (60000 * 1.1)

# Método estático
print(Employee.is_salary_high(70000))  # Imprime True
print(Employee.is_salary_high(40000))  # Imprime False
