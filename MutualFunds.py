#Flask
from flask import Flask, render_template, request, Blueprint
MF = Blueprint('MF', __name__, static_folder='static', template_folder='templates')


#Connecting To MongoDB
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["RMA_BANK"]
myaccount = mydb["MutualFunds"]


#Class
class MutualFunds:
    
    #Constructor
    def __init__(self, name, address, pan, mobNo, dob, accNo,typee, branch, IPD, plan, opt, dividend):
        self.__name = name
        self.__address = address
        self.__pan = pan
        self.__mobNo = mobNo
        self.__dob = dob
        self.__accNo = accNo
        self.__typee = typee
        self.__branch = branch
        self.__IPD = IPD
        self.__plan = plan
        self.__opt = opt
        self.__dividend = dividend

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_pan(self):
        return self.__pan
    
    def get_mob(self):
        return self.__mobNo
    
    def get_dob(self):
        return self.__dob
    
    def get_accno(self):
        return self.__accNo
    
    def get_branch(self):
        return self.__branch
    
    def get_IPD(self):
        return self.__IPD
    
    def get_plan(self):
        return self.__plan
    
    def get_opt(self):
        return self.__opt
    
    def get_dividend(self):
        return self.__dividend


#Global Variables    
name = ""
address = ""
pan = ""
mobNo = ""
dob = ""
accNo = ""
typee = ""
branch = ""
IPD = ""
plan = ""
opt = ""
dividend = ""


#Python Decorator for linking Mutual Funds Page
@MF.route('/Mutualfund', methods=['GET', 'POST'])
def take_input():
    global name
    global address
    global pan 
    global mobNo
    global dob 
    global accNo
    global typee
    global branch 
    global IPD 
    global plan 
    global opt 
    global dividend

    if request.method == 'POST':   
        name = request.form['fname']

    if request.method == 'POST':   
        address = request.form['address']

    if request.method == 'POST':
        pan = request.form['pan']

    if request.method == 'POST':
        j=0
        while(j==0):    
            mobNo = request.form['phone']
            if(mobNo.isdigit()):
                j=1
            else:
                print("Please try again")
            if(len(mobNo) == 10):
                j=1
            else:
                print("Please try again")
                j=0

    if request.method == 'POST':
        dob = request.form['birthday']

    if request.method == 'POST':
        j=0
        while(j==0):
            try:
                accNo = request.form['accNum']
                j=1
            except:
                print("Please Try Again")

    if request.method == 'POST':
        typee = request.form['account']

    if request.method == 'POST':
        branch = request.form['branch']

    if request.method == 'POST':
        IPD = request.form['investment']
    
    if request.method == 'POST':
        plan = request.form['plan']
    
    if request.method == 'POST':
        opt = request.form['option']
    
    if request.method == 'POST':
        dividend = request.form['dividend']

    if(name == ""):
        pass
    else:
        fund = MutualFunds(name, address, pan, mobNo, dob, accNo, typee, branch, IPD, plan, opt, dividend)
        mydict = {"AccountNumber" : fund.get_accno(), "AccountHolderName" : fund.get_name(),
                "Branch" :fund.get_branch(),"DateOfBirth" : fund.get_dob(), 
                "Contact Number" : fund.get_mob(), "PAN NO" : fund.get_pan(),
                 "Address" : fund.get_address(), "Investment Payment Details" : fund.get_IPD(),
                "Plan" : fund.get_plan(), "Options" : fund.get_opt(), "Dividend" : fund.get_dividend()}
        x = myaccount.insert_one(mydict)
    
    return render_template('mutual.html')
  

myclient.close()