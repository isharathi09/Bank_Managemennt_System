# Data Encapsulation, Single-level Inheritance and Exception Handling

# Flask
from flask import Flask, render_template, request, Blueprint
BankDeposit = Blueprint('BankDeposit', __name__, static_folder='static',template_folder='templates')


# Connecting to MongoDB
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["RMA_BANK"]
myfd = mydb["FixedDeposits"]
myrd = mydb["RecurringDeposits"]


# Base Class
class BankDeposits:
    
    # Constructor
    def __init__(self, name):
        self.__name = name

    # get-set method
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value


# Child Class of 'BankDeposits'
class FixedDeposit(BankDeposits):

    # Constructor
    def __init__(self, name, duration, amount, rateOfInterest):
        super().__init__(name)      # Parent Constructor Called
        self.__accountNumber = myfd.find().count() + 2001
        self.__duration = duration
        self.__amount = amount
        self.__rateOfInterest = rateOfInterest

    def get_account_number(self):
        return self.__accountNumber

    def get_duration(self):
        return self.__duration

    def get_amount(self):
        return self.__amount

    def get_rate_of_interest(self):
        return self.__rateOfInterest

    def set_account_number(self, value):
        self.__accountNumber = value

    def set_duration(self, value):
        self.__duration = value

    def set_amount(self, value):
        self.__amount = value

    def set_rate_of_interest(self, value):
        self.__rateOfInterest = value


# Child Class of 'BankDeposits'
class RecurringDeposit(BankDeposits):

    # Constructor
    def __init__(self, name, duration, monthlyPayment, rateOfInterest):
        super().__init__(name)  # Parent Constructor Called
        self.__accountNumber = myrd.find().count() + 3001
        self.__duration = duration
        self.__monthlyPayment = monthlyPayment
        self.__rateOfInterest = rateOfInterest

    def get_account_number(self):
        return self.__accountNumber

    def get_duration(self):
        return self.__duration

    def get_monthly_payment(self):
        return self.__monthlyPayment

    def get_rate_of_interest(self):
        return self.__rateOfInterest

    def set_account_number(self, value):
        self.__accountNumber = value

    def set_duration(self, value):
        self.__duration = value

    def set_monthly_payment(self, value):
        self.__monthlyPayment = value

    def set_rate_of_interest(self, value):
        self.__rateOfInterest = value


# Global Variables
name = ""
duration = ""
amount = ""
rateOfInterest = ""
monthlyPayment = ""


# Python Decorator for linking Fixed Deposit Page
@BankDeposit.route('/readWriteFixedDeposit', methods=['GET','POST'])
def readWriteFixedDeposit():
    global name
    global duration
    global amount
    global rateOfInterest

    if request.method == 'POST':
        name = request.form['fname']

    j = 0
    while(j == 0):
        try:
            if request.method == 'POST':
                duration = request.form['duration']
            j = 1
        except:
            #print("Please try again")
            j = 0
    j = 0
    while(j == 0):
        try:
            if request.method == 'POST':
                amount = request.form['amount']
            j = 1
        except:
            #print("Please try again")
            j = 0

    j = 0
    while(j == 0):
        try:
            if request.method == 'POST':
                rateOfInterest = request.form['interest']
            j = 1
        except:
            #print("Please try again")
            j = 0
    if(name == ""):
        pass
    else:
        fd = FixedDeposit(name, duration, amount, rateOfInterest)

        mydict = {"AccountNumber": fd.get_account_number(), "AccountHolderName": fd.get_name(),
                  "Duration": fd.get_duration(), "Amount": fd.get_amount(),
                  "RateOfInterest": fd.get_rate_of_interest()}
        x = myfd.insert_one(mydict)
    
    return render_template('fixed.html')


# Python Decorator for linking for Recurring Deposit Page
@BankDeposit.route('/readWriteRecurringDeposit', methods=['GET','POST'])
def readWriteRecurringDeposit():
    global name
    global duration
    global monthlyPayment
    global rateOfInterest

    if request.method == 'POST':
        name = request.form['fname']

    j = 0
    while(j == 0):
        try:
            if request.method == 'POST':
                duration = request.form['duration']
            j = 1
        except:
            #print("Please try again")
            j = 0

    j = 0
    while(j == 0):
        try:
            if request.method == 'POST':
                monthlyPayment = request.form['amount']
            j = 1
        except:
            #print("Please try again")
            j = 0

    j = 0
    while(j == 0):
        try:
            if request.method == 'POST':
                rateOfInterest = request.form['interest']
            j = 1
        except:
            #print("Please try again")
            j = 0

    if(name == ""):
        pass
    else:
        rd = RecurringDeposit(name, duration, monthlyPayment, rateOfInterest)

        mydict = {"AccountNumber": rd.get_account_number(), "AccountHolderName": rd.get_name(),
                  "Duration": rd.get_duration(), "MonthlyPayment": rd.get_monthly_payment(),
                  "RateOfInterest": rd.get_rate_of_interest()}
        x = myrd.insert_one(mydict)

    return render_template('recurring.html')

myclient.close()
