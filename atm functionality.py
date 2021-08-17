def isatm():
  print('Welcome to Indian bank ATM')
  restart=('y')
  chances=3
  balance=1078.45
  while chances>=0:
    pin=int(input('Please Enter you 4 Digit Pin:'))
    if pin==(1234):
       print('you have entered a valid pin\n')
       print('please press 1 to check your account balance\n')
       print('please press 2 to deposit amount in your account\n')
       print('please press 3 to withdraw amount from your account\n')
       print('please press 4 to change your pin\n')
       break
    if option==1:
        print('your balance is ',balance)
        restart=input('would you like to go back?')
        if restart in('n','NO','no','N'):
           print('Thank You')
           break
    elif option==2:
         deposit=float(input('how much would you like to deposit'))
         balance=balance+deposit
         print('your balance is now',balance)
         restart=input('would you like to go back?')
         if restart in('n','NO','no','N'):
            print('Thank You')
            break
    elif option==3:
        withdrawl=float(input('how much would you like to withdrawl?'))
        if withdrawl<=balance
          balance=balance-withdrawl
          print('your balance is now',balance)
          restart=input('would you like to go back?')
          if restart in('n','NO','no','N'):
             print('Thank You')
             break
        elif withdrawl>balance
            print('invalid amount,please re-try\n')
            restart=('Y')
        elif withdrawl<10:
            withdrawl=float(input('please enter desired amount:'))
    elif option==4:
       print('please click here to change password\n')
       print('Thank You for your service')
    elif pin!=(1234):
      print('incorrect password')
      chances=chances-1
      if chances==0:
         print('\n No more tries')
         break
    else:
       print('please enter a valid pin') 
