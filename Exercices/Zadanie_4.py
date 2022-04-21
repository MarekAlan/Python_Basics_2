class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name.title() # aby było ładnie i pierwsza litera duża
        self.last_name = last_name

    def set_salary(self, salary):
        if (type(salary) == int or type(salary) == float) and salary >= 0:
        #if isintance(salary, (float, int)) and salary >= 0: #jeżeli salary jest albo float albo int to true
            self._salary = salary

    def print_info(self):
        try: # po to że jak się bez try to się wywala jeżeli nie ma ustalonego salary
            print(f"Employee {self.first_name}, {self.last_name}, has a salary of {self._salary}")
        except AttributeError:
            print(f"Employee {self.first_name}, {self.last_name} doesn't have a set salary yet.")

employee = Employee(1, "John", "McClusky")
employee.set_salary(200)
employee.print_info()

