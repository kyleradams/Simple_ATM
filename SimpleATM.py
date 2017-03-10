# Kyler Adams
import bank as bk

class ATM(bk.Bank):
    
    def __init__(self, accounts):
        self._name = ''
        self._pin = ''
        self._accounts = accounts
        
    def run(self):
        while True:
            self._name = raw_input("Enter your name: ")
            if self._name == 'CloseItDown':
                return 'Shutting Down...'
            self._pin = raw_input("Enter your PIN: ")
            selectedAccount = self._accounts.get(str(self._pin))
            selection = '0'
        
            if selectedAccount == None or selectedAccount.getName() != self._name:
                print 'Error, unrecognized name'
            else:
                while selection != '4':
                    atmscreen = '1 View your balance \n'
                    atmscreen += '2 Make a deposit \n'
                    atmscreen += '3 Make a withdrawal \n'
                    atmscreen += '4 Quit \n'
                    print atmscreen
                    selection = raw_input("Enter a number: ")
            
                    if selection == '1':
                        print 'Your balance is $' + str(selectedAccount.getBalance())
                    elif selection == '2':
                        depAmount = raw_input("Enter the amount to deposit: ")
                        selectedAccount.deposit(int(depAmount))
                    elif selection == '3':
                        depAmount = raw_input("Enter the amount to deposit: ")
                        selectedAccount.deposit(int(depAmount))
                    elif selection != '4':
                        print 'Please make a valid selection \n'
                
                print 'Have a nice day!'

            
            
 
        

            