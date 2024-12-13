amt = int(input("Enter actual amount: "))
dep = 0
balance = amt


def val():
   p = '123'
   max_attempts = 3

   for attempt in range(max_attempts):
       pin = input("Enter pin: ")
       if pin == p:
           print("Correct pin")
           break
       else:
           remaining = max_attempts - attempt - 1
           print(f"Remaining attempts: {remaining}")
           if remaining == 0:
               print("Try again after 24 hours")
               return
   print("1. Deposit")
   print("2. Withdraw")
   print("3. Balance")
   print("4. EXIT")

   opt = int(input("Choose an option: "))
   if opt == 1:
       deposit()
   elif opt == 2:
       withdraw()
   elif opt == 3:
       balance_info()
   elif opt == 4:
       print("Exiting... Goodbye!")
   else:
       print("Invalid option. Please try again.")

def deposit():
  global dep
  dep= int(input("Enter deposit amount: "))
  if dep%100 == 0:
      if dep>=100 and dep<=50000:
           print("amount deposited")
      else:
          print("deposit amount less than 50k")
  else:
    print("Enter multiples of 100")

def withdraw():
   global wamt
   wamt = int(input("Enter withdrawal amount: "))
   if amt>=500:
       if wamt%100==0:
           if wamt>=100 and wamt<amt:
               if wamt<=20000:
                   print("deposited successfully")
               else:
                   print("transaction limit 20k")
           else:
               print("Enter amount should be greater than 100")
       else:
           print("Entered should be multiple of 100")
   else:
       print("enter amount should be greater than 500")

def balance_info():
   print(f"Current balance: {balance}")


val()