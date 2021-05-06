#Flask
from flask import Flask, flash, render_template, request, redirect, url_for, Blueprint


#Importing other Flask Applications
from BankDeposit import BankDeposit
from MutualFunds import MF
from BankAccount import BankAcc

#Register them with main app
App = Flask(__name__)
App.register_blueprint(BankDeposit)
App.register_blueprint(MF)
App.register_blueprint(BankAcc)

#Home Page
@App.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


#FixedDeposit Page
@App.route('/fixeddeposit', methods=['GET','POST'])
def fixeddeposit():
    if request.method == "GET":
        return render_template('fixed.html')
    else:
        return render_template('index.html')


#RecurringDeposit Page
@App.route('/recurdeposit', methods=['GET','POST'])
def recurdeposit():
    if request.method == "GET":
        return render_template('recurring.html')
    else:
        return render_template('index.html')


#Insurance Page
@App.route('/insurance', methods=['GET','POST'])
def insurance():
    if request.method == "GET":
        return render_template('insurance.html')
    else:
        return render_template('index.html')


#MutualFunds Page
@App.route('/mutualfund', methods=['GET','POST'])
def mutualfund():
    if request.method == "GET":
        return render_template('mutual.html')
    else:
        return render_template('index.html')


#AccountCreation Page
@App.route('/savings', methods=['GET','POST'])
def savings():
    if request.method == "GET":
        return render_template('savings.html')
    else:
        return render_template('index.html')

#Modify Details Page
@App.route('/modifyD', methods=['GET','POST'])
def modifyD():
    if request.method == "GET":
        return render_template('modifyDetails.html')
    else:
        return render_template('index.html')

#Balance Enquiry Page
@App.route('/balance', methods=['GET','POST'])
def balance():
    if request.method == "GET":
        return render_template('balance.html')
    else:
        return render_template('index.html')


#Branch Transfer Page
@App.route('/transfer', methods=['GET','POST'])
def transfer():
    if request.method == "GET":
        return render_template('transfer.html')
    else:
        return render_template('index.html')

#Type Change Page
@App.route('/type', methods=['GET','POST'])
def ttype():
    if request.method == "GET":
        return render_template('type.html')
    else:
        return render_template('index.html')
    
#AmountDeposit Page
@App.route('/amtdeposit', methods=['GET','POST'])
def amtdeposit():
    if request.method == "GET":
        return render_template('amtdeposit.html')
    else:
        return render_template('index.html')


#AmountWithdrawal Page
@App.route('/amtWithdrawal', methods=['GET','POST'])
def amtWithdrawal():
    if request.method == "GET":
        return render_template('amtWithdrawal.html')
    else:
        return render_template('index.html')


#Close Account Page
@App.route('/close', methods=['GET','POST'])
def close():
    if request.method == "GET":
        return render_template('close.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    App.run(debug=True)