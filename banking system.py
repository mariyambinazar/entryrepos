#ex1
class bankaccount:
   def __init__(self,accountno,accountholder,username,password,balance=0):
      self.an=accountno
      self.ah=accountholder
      self.bl=balance
      self.p=password
      self.us=username
   def login(self):
      ac_no=int(input("Enter your Account no:"))
      usrnm = input("Enter your User name:")
      pswrd = input("PASSWORD:")
      if ac_no==self.an and usrnm==self.us and pswrd==self.p:
          print(f"welcome{self.ah}")
          while True:
              print("Press 1 for Deposit")
              print("Press 2 for Withdraw")
              print("Press 3 for Check balance")
              print("Press 0 for Logout")
              option=int(input("Enter your choice:"))
              if option==1:
                 Account.deposit()
              elif option==2:
                 Account.withdraw()
              elif option == 3:
                Account.balance_check()
              elif option == 0:
                 print("logged out")
                 break
              else:
                 print(int(input("Enter a valid option")))
      else:
        print("login id is wrong")
   def deposit(self):
      amount=int(input("Enter amount to deposit"))
      self.bl +=amount
      print(f"your account credited by rs{amount} and your balance is{self.bl}")
   def withdraw(self):
      amount=int(input("Enter amount to withdraw"))
      if self.bl >= amount:
        self.bl -= amount
        print(f"your account debited by rs{amount} and your balance is{self.bl}")
      else:
        print("you have no sufficient balance in your account")
   def balance_check(self):
     print(f"your balance is{self.bl}")

Account=bankaccount(12345,"Aban","ABAN@SDD","1234@345",2500)
Account.login()

