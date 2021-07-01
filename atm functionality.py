def isatm():
  print('Welcome to Indian bank ATM')
  chances=3
  balance=78.45
  while chances>=0:
    pin=int(input('Please Enter you 4 Digit Pin:'))
    if pin==(1234):
       print('you have entered a valid pin\n')
         print('please press 1 to check your account balance\n')
         print('please press 2 to deposit amount in your account\n')
         print('please press 3 to withdraw amount from your account\n')
         print('please press 4 to change your pin\n')
         break
    elif pin!=(1234):
      print('incorrect password')
      chances=chances-1
      if chances==0:
         print('\n No more tries')
         break
    else:
       print('please enter a valid pin') 
