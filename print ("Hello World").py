import tkinter
import os
import sqlite3

connection = sqlite3.connect("bank.sqlite")
cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS bank_base (
                account_number INTEGER PRIMARY KEY,
                age TEXT,
                name TEXT,
                email TEXT,
                phone TEXT,
                pin TEXT,
                password TEXT,
                balance REAL
                );
                """)


connection.commit()
cur.fetchall()

def main_menu():
    print("1. Create Account")
    print("2. Login")
    print("3. Leave")
    choicing = input("Hello, welcome to Jebediah Banking, what would you like to do?: ")
    small = choicing.lower()
    if small == "create account":
        bank_age()
    elif small == "login":
        log_in()
    elif small == "leave":
        print("We hope to see you again!")
    else:
        print("That's an invalid response.")
        main_menu()

def log_in():
     print("---------------------------------------")
     user_pin_log = input("Insert 4 digit pin: ")
     user_login = input("Please insert password: ")
        
    
    

def bank_age():
    print("****Please note that we will ask you this information later, so please write it down****")
    print("---------------------------------------")
    edad = int(input("To begin, what's your age?: "))
    if edad< 16:
        print("We're sorry, you are too young to have a bank account.")
    elif edad >= 16:
        age_con = input("Are you sure you are " + str(edad) + " years old? (yes/no): ")
        banking_name()

def banking_name():
    print("---------------------------------------")
    naming = input("What is your name? (legal name only): ")
    for letters in naming:
        #Will check if your name has letters, and if so, will make you
        #try again, if all is good, then moves to email process.
        if letters.isdigit():
            print("Names should not have numbers, please try again.")
            print("-----------------------------------")
            banking_name()
    else:
            print("Thank you, " + (naming) + ", lets continue with your email")
            print("-------------------------------------------------")
            banking_email()

def banking_email():
    mail = input("Insert email here: ")
    confirming = input("So your email is " + (mail) + "? (yes/no):") 
    if confirming == "yes":
        print("Alright, lets go to the final step, your telephone.")
        print("-------------------------------------------------------")
        phone_number()
    if confirming == "no":
        print("Let's try to input this again.")
        print("------------------------------------------")
        banking_email()



def phone_number():
    phono = (input("Insert your phone number (No -): "))
    numeros = 0
    #Will check if your phone number is 10 characters, if not, will repeat, if yes, will ask to confirm and continue.
    for i in range(len(phono)):
        numeros = numeros + 1
    if numeros != 10:
        print("Phone numbers should only have 10 numbers, you may have added an unnecessary number or added the +1 at the beginning, please try again")
        print("------------------------------------------")
        phone_number()
    elif numeros == 10:
        confirm = input("So your phone number is " + str(phono) + "? (yes/no): ")
    if confirm == "yes":
        pin_number()
    else:
        print("Then try to input it again")
        print("---------------------------------------")
        phone_number()

def pin_number():
    print("--------------------------------------------")
    pinny = int(input("Insert your 4 digit pin number, this will be used to identify you when you use one of our many ATMs nationwide: "))
    pin_string = str(pinny)
    pinny_len = len(pin_string)
    if pinny_len == 4:
        pinny_q = input("Are you sure you wish to make " + str(pinny) + " your pin number? (yes/no): ")
        pinny_qu = pinny_q.lower()
        if pinny_qu == "yes":
            passing()
        elif pinny_qu == "no":
            print("---------------------------------------")
            print("Please input your new pin number")
            pin_number()
        else:
            print("You may have inserted something incorrectly, please try again.")
            pin_number()


def passing():
    print("---------------------------------------")
    passing = input("Please pick a password for your account: ")
    if len(passing) < 5:
        print("Your password is too short, please try something longer")
        passing()
    if len(passing) >= 6:
        len_con = input("Are you sure your password will be " + str(passing) + "? (yes/no): ")
        len_confirm = len_con.lower()
        if len_confirm == "yes":
            testing_user()
        elif len_confirm == "no":
            print("---------------------------------------")
            print("Then please try again")
            passing()


def after_pass():
    print("Account succesfully created, you can now login to your bank account.")
    main_menu()

def testing_user():
        age = input("Please reinsert your original age: ")
        name = input("Please insert your original name: ")
        email = input("Please insert your original email: ")
        phone = (input("Please insert your 10 digit phone number: "))
        pin = (input("Please insert your original 4 digit pin: "))
        password = input("Please insert your original password: ")
        balance = float(0.00)
        cur.execute(""" 
        INSERT INTO bank_base(age, name, email, phone, pin, password, balance) VALUES (?,?,?,?,?,?,?) 
         """, (age, name, email, phone, pin, password, balance))
        after_pass()
        
        
connection.commit()



def balance():
    bal_choice = input("What would you like to do with your balance? (withdraw/deposit): ")
    if bal_choice == "withdraw":
        withdrawing = int(input("How much would you like to with draw?: "))
        if balance - withdrawing < 0:
            print("You cannot have a negative number")
        else:
            balance == balance - depositing
    if bal_choice == "deposit":
        depositing = int(input("How much would you like to deposit"))
        balance == balance + depositing


main_menu()

