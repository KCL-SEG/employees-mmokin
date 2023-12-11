"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    def __init__(self, name, salary, commission=0, contracts=0, commission_per_contract=0):
        super().__init__(name)
        self.salary = salary
        self.commission = commission
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        if self.contracts > 0:
            return self.salary + self.contracts * self.commission_per_contract
        return self.salary + self.commission

    def __str__(self):
        if self.contracts > 0:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."
        if self.commission > 0:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}."
        return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate, commission=0, contracts=0, commission_per_contract=0):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.commission = commission
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        if self.contracts > 0:
            return self.hours_worked * self.hourly_rate + self.contracts * self.commission_per_contract
        return self.hours_worked * self.hourly_rate + self.commission

    def __str__(self):
        if self.contracts > 0:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."
        if self.commission > 0:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}."
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, contracts=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan', 150, 25, contracts=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel', 120, 30, commission=600)
