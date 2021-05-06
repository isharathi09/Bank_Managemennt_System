# Flask
import pymongo
from flask import Flask, flash, render_template, request, Blueprint
BankAcc = Blueprint('BankAcc', __name__, static_folder='static', template_folder='templates')


# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = myclient["RMA_BANK"]
myaccount = mydb["Accounts"]


class BankAccount:

    def get_accountNumber(self):
        return self.__accNo

    def get_account_holder_Name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_amount(self):
        return self.__amount

    def get_branch(self):
        return self.__branch

    def get_dob(self):
        return self.__dob

    def get_email(self):
        return self.__email

    def get_mobNo(self):
        return self.__mobNo

    def get_aadhar(self):
        return self.__aadhar

    def get_gender(self):
        return self.__gender

    def get_address(self):
        return self.__address

    def set_accountNumber(self):
        self.__accNo = myaccount.find().count() + 1001
        return

    def set_account_holder_Name(self, name):
        self.__name = name
        return

    def set_type(self, ttype):
        self.__type = ttype
        return

    def set_amount(self, amount):
        self.__amount = amount
        return

    def set_branch(self, branch):
        self.__branch = branch
        return

    def set_dob(self, dob):
        self.__dob = dob
        return

    def set_email(self, email):
        self.__email = email
        return

    def set_mobNo(self, mobNo):
        self.__mobNo = mobNo
        return

    def set_aadhar(self, aadhar):
        self.__aadhar = aadhar
        return

    def set_gender(self, gender):
        self.__gender = gender
        return

    def set_address(self, address):
        self.__address = address
        return

        

# Python Decorator for Create Account Page
@BankAcc.route('/CreateAccount', methods=['GET', 'POST'])
def CreateAccount():

    # AccountHolder Name
    if request.method == "POST":
        name = request.form['fname']

    # Address
    if request.method == "POST":
        address = request.form['address']

    # Type of Account
    if request.method == "POST":
        ttype = request.form['account']

    # Branch
    if request.method == "POST":
        branch = request.form['branch']

    # email
    if request.method == "POST":
        email = request.form['emailid']

    # DOB
    if request.method == "POST":
        dob = request.form['birthday']

    # Gender
    if request.method == "POST":
        gender = request.form['gender']

    # Contact Number
    j = 0
    while(j == 0):
        if request.method == "POST":
            mobNo = request.form['phone']
            if(mobNo.isdigit()):
                j = 1
            else:
                print("Please try again")
            if(len(mobNo) == 10):
                j = 1
            else:
                print("Please try again")
                j = 0

    # Verification Proof(Aadhar)
    j = 0
    while(j == 0):
        if request.method == "POST":
            aadhar = request.form['aadhar']
            if(aadhar.isdigit()):
                j = 1
            else:
                print("Please try again. Letters not allowed")
            if(len(aadhar) == 12):
                j = 1
            else:
                j = 0
                print("Please try again. Aadhar No cannot exceed 12 digits")

    # Initial Amount
    j = 0
    while(j == 0):
        try:
            if request.method == "POST":
                amount = request.form['amount']
                j = 1
        except:
            print("Please try again")

    Account = BankAccount()
    
    Account.set_accountNumber()
    Account.set_account_holder_Name(name)
    Account.set_address(address)
    Account.set_type(ttype)
    Account.set_branch(branch)
    Account.set_email(email)
    Account.set_dob(dob)
    Account.set_gender(gender)
    Account.set_mobNo(mobNo)
    Account.set_aadhar(aadhar)
    Account.set_amount(amount)

    mydict = {"AccountNumber": Account.get_accountNumber(), "AccountHolderName": Account.get_account_holder_Name(),
              "Address": Account.get_address(), "Type": Account.get_type(), "Branch": Account.get_branch(),
              "Email ID": Account.get_email(), "DateOfBirth": Account.get_dob(),
              "Gender": Account.get_gender(), "Contact Number": Account.get_mobNo(),
              "Aadhar Number": Account.get_aadhar(), "Amount": Account.get_amount()}

    x = myaccount.insert_one(mydict)
    #print("\n\nAccount Created\n")
    #print("Your Account Number is : ", )
    return render_template('savings.html')

#Modify Personal Details
@BankAcc.route('/modify', methods=['GET','POST'])
def modifyDetails():
    if request.method == "POST":
        acc = request.form['accountNum']
    
    myquery = {"AccountNumber" : eval(acc)}
    
    if request.method == "POST":
        email = request.form['emailid']
    newemail = {"$set" : {"Email ID" : email}}
    myaccount.update_one(myquery, newemail)

    if request.method == "POST":
        phone = request.form['phone']
    newphone = {"$set" : {"Contact Number" : phone}}
    myaccount.update_one(myquery, newphone)

    return render_template('modifyDetails.html')

#Deposit Page
@BankAcc.route('/deposit', methods=['GET', 'POST'])
def depositAmount():
    if request.method == "POST":
        acc = request.form['accountNum'] 

    amount = int(myaccount.find_one({"AccountNumber": eval(acc)}).get("Amount"))
        
    if request.method == "POST":
        deposit = int(request.form['amount'])
        amount += deposit
    
    amount = str(amount)
    
    myquery = {"AccountNumber" : eval(acc)}
    newvalues = {"$set" : {"Amount" : eval(amount)}}
    myaccount.update_one(myquery, newvalues)
        
    #print("\nAmount Deposited Successfully\n")
    return render_template('amtdeposit.html')


#Withdrawal Page
@BankAcc.route('/withdraw', methods=['GET', 'POST'])
def withdrawAmount():
    if request.method == "POST":
        acc = request.form['accountNum'] 

    amount = int(myaccount.find_one({"AccountNumber": eval(acc)}).get("Amount"))
        
    if request.method == "POST":
        deposit = int(request.form['amount'])
        amount -= deposit
    
    amount = str(amount)
    
    myquery = {"AccountNumber" : eval(acc)}
    newvalues = {"$set" : {"Amount" : eval(amount)}}
    myaccount.update_one(myquery, newvalues)
        
    #print("\nAmount Deposited Successfully\n")
    return render_template('amtWithdrawal.html')


#Branch Change
@BankAcc.route('/branchchange', methods=['GET', 'POST'])
def branchChange():
    if request.method == "POST":
        acc = request.form['accountNum']
    
    if request.method == "POST":
        ch_branch = request.form['cbranch']
    
    myquery = {"AccountNumber" : eval(acc)}
    newvalues = {"$set" : {"Branch" : ch_branch}}
    myaccount.update_one(myquery, newvalues)

    return render_template('transfer.html')


#Type Change
@BankAcc.route('/typechange', methods=['GET','POST'])
def typeChange():
    if request.method == "POST":
        acc = request.form['accountNum']
    
    if request.method == "POST":
        ch_type = request.form['ch_account']
    
    myquery = {"AccountNumber" : eval(acc)}
    newvalues = {"$set" : {"Type" : ch_type}}
    myaccount.update_one(myquery, newvalues)

    return render_template('type.html')


#Balance Enquiry
@BankAcc.route('/bal_enq',methods=['GET', 'POST'])
def bal_enquiry():
    if request.method == "POST": 
        acc = request.form['accountNum']
    
    amount = int(myaccount.find_one({"AccountNumber": eval(acc)}).get("Amount"))
    amount = str(amount)

    return """Balance in your account is: """ + amount
    #print("\nBalance in your Account is : ")
    #print(myaccount.find_one({"AccountNumber": eval(acc)}).get("Amount"))

    


#Close Account
@BankAcc.route('/closeacc', methods=['GET','POST'])
def closeacc():
    if request.method == "POST":
        acc = request.form['accountNum']
    
    myquery = { "AccountNumber" : eval(acc)}
    myaccount.delete_one(myquery)

    return render_template('close.html')

myclient.close()
