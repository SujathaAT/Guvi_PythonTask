# ======================================================================
# Question 1
# Base Class : Bank Account
# Subclass   : Savings Account and Current aAccount
# ======================================================================


class BankAccount:
    account_no = ""
    __balance = 100
    #
    def __init__(self, accountno, bal):
        self.account_no = accountno
        self.__balance = bal
        print(BankAccount.__balance)


    def deposit(cls, amount):
        if amount <= 0:
            raise ValueError("Deposit cannot be negative")
        else:
            cls.amount = amount
            currbalance = BankAccount.__balance

            currbalance+= cls.amount
            # print(f"Amount " {self.amount} "deposited and account balance is " {self.balance})
            print("Amount Deposited")
            print("Current Balance  : {currbalance}".format(currbalance=currbalance))
            BankAccount.__balance = currbalance
            return currbalance


    def withdraw(self, withdrawalamt):
        self.withdrawalamt = withdrawalamt
        min_balance = 100
        val_balance = BankAccount.__balance - withdrawalamt
        curr_balance= BankAccount.__balance
        if withdrawalamt <= curr_balance and val_balance >= min_balance:
            BankAccount.__balance-= withdrawalamt
            # print(f"Amount "{withdrawalamt} "withdarawn and account balance is " {self.balances})
            print("Amount Withdarawn")
            print("Current Balance  : {curr_balance}".format(curr_balance=curr_balance))
            return BankAccount.__balance
        else:
            # raise ValueError("Withdarawal cannot be done")
            print("====Withdarawal cannot be done=====")
            print("Current Balance  : {curr_balance}".format(curr_balance=curr_balance))
            print("withdrawal Amount:{withdrawalamt}".format(withdrawalamt=withdrawalamt))
            print('Minimum Balance to be maintained: {min_balance}'.format(min_balance=min_balance))
            print("====Withdarawal cannot be done=====")
            return BankAccount.__balance



class SavingsAccount(BankAccount):
    interest_Rate = 0.07
    def __init__(self, acctno,type):
        self.acctno = acctno
        self.type = type

        # super().__init__(acctno,type)

    def calculate_interest_rate(self, balanceamt):
        self.balanceamt = balanceamt
        if balanceamt != 0:
            intamt= self.balanceamt * SavingsAccount.interest_Rate
            self.balanceamt = self.balanceamt+intamt
            print("Interest applied")
            print('Interest Rate :7%"')
            netbal = self.balanceamt
            print("Balance <Interest Applied> : " + str(netbal))
            # return self.balanceamt

class CurrentAccount(BankAccount):

    min_balance = 100

    def verify_withdrawal(self, amt,balance):
        self.balance -= balance
        # if amt <= curr_balance and val_balance >= min_balance:
        if balance > min_balance:

            self.balance = withdrawamt(balance)
            return balance
        else:
            return balance
            print("Withdrawal cannot exceed account balance and minimum balance")


# createAccount("Joshy", "100")
bkacc = BankAccount("Tim",'0')

mybalance =BankAccount.deposit(bkacc,100)
print(mybalance)
balaftrwd = BankAccount.withdraw(bkacc, 150)
print(balaftrwd)
# BankAccount.withdraw(100)

svgacc =SavingsAccount("TIM","S")
svgaccbal= svgacc.calculate_interest_rate(balaftrwd)
print("Now")
print(svgaccbal)
# ======================================================================
# Question 2
# Base Classs ; Employee
# Subclass: RegularEmployee, Contract Emplyee, Manager
# ======================================================================

import random
import string


class Employee:
    # empid
    # empname
    # empsalary

    def __init(self, name, salary):
        self.name = name
        self.salary = salary

    def checkid(self,id):
        self.id = id
        if self.id == "":
            temp = string.ascii_letters
            id = temp.upper()[:3] + str(random.randint(0, 5))
            return(id)


    def calculate_salary(self):
        print(f"Base Salary - {self.salary}")
        return self.salary



class RegularEmployee(Employee):
    # salary

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

        if id == "":
            empid = super().checkid(id)

            # super().__init__(name, salary)
        # self.allow = allow
        # self.deds = deds

    def calculate_resalary(self,allow, deds):
        return (self.salary + allow) - deds



class ContractEmployee(Employee):
    # salary

    def __init__(self, id, name, salary, phrate):
        self.id = id
        self.name = name
        self.salary = salary
        self.phrate = phrate

    def calculate_salary(self):
        return self.salary * self.phrate


class Manager(Employee):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary


    def calculate_salary(self,bonus):
        return int(self.salary) + int(bonus)


name = "Fiona"
RegularEmployee("", name, 100).calculate_salary()
totcomp = RegularEmployee("","Fiona",100000).calculate_resalary(6000,1000)
print("Regular Employee - "+ name + " Salary :" + str(totcomp))

contractsal= ContractEmployee("","Diana", 2500,27).calculate_salary()
print("Contract Employee - Diana Salary : " + str(contractsal))

netsal = Manager("","Ema","101000").calculate_salary(1000)
print("Manager - Ema Salary : " + str(netsal))


# ======================================================================
# Question 3
# Base Class : Vehicle
# Subclasses : Car, Bike, Truck
# ======================================================================


class Vehicle:

    def __init__(self, model, rentratepd):
        self.model = model
        self.rentratepd = rentratepd
        print ("Model :" + model)
        print ("Rental rate :" + str(rentratepd))

    def calculaterent(self, duration):
        return self.rentratepd * duration


class Car(Vehicle):
    def __init__(self, model, rentratepd, noofseats):
        print("===================")
        print("Car Rental details")
        print("===================")
        super().__init__(model, rentratepd)
        self.noofseats = noofseats

    def calculaterent(self, duration):
        if self.noofseats > 4:
            fixedfee = 150
            return (self.rentratepd * duration) + 150
        else:
            return (self.rentratepd * duration)



class Bike(Vehicle):
    def __init__(self, model, rentratepd):
        print("===================")
        print("bike Rental details")
        print("===================")
        super().__init__(model, rentratepd)

    def calculaterent(self, phrusage):
        basefee = 50
        rent = super().calculaterent(phrusage)
        return rent + basefee


class Truck(Vehicle):
    def __init__(self, model, rentratepkm,load):  # load-F- Full, P - Part
        #super().__init__(model, rentratepkm)
        print("===================")
        print("Truck Rental details")
        print("===================")
        print("Model :" + model)
        print("Rental rate per k/m :" + str(rentratepkm))
        self.model = model
        self.rentratepkm = rentratepkm
        self.load = load

    def calculaterent(self, pkmusage):
        basecharge = ""
        try:
            if self.load == 'F':
                basecharge = 500
            else:
                basecharge = 100
            return  basecharge * self.rentratepkm
        except:
            print("Value Error. Per km usage can accept F or P")


bk = Bike("Royal Enfield",50)
bkrent = bk.calculaterent(10)
print("Bike Rent : " + str(bkrent))

cr = Car("Hundai",10,5)
crrent = cr.calculaterent(7)
print("Car rent : " + str(crrent))

tr = Truck("TIMBO",300, 'F' )
trkrent = tr.calculaterent(5)
print("Truck rent : " + str(trkrent))
