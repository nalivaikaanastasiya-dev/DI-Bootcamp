import sys

class BankAccount:
    def __init__(self, username, password, initial_balance=0):
        self.username = username
        self.password = password
        self.balance = initial_balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False

    def _is_positive(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Transaction amount must be a positive number.")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to perform deposit.")
        
        self._is_positive(amount)
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to perform withdrawal.")
            
        self._is_positive(amount)
        if self.balance < amount:
            raise Exception("Insufficient funds.")
            
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

    def __repr__(self):
        return f"BankAccount(User: {self.username}, Balance: {self.balance:.2f})"

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, initial_balance=0, minimum_balance=0):
        super().__init__(username, password, initial_balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required to perform withdrawal.")
            
        self._is_positive(amount)
        
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Withdrawal denied. Balance must remain above minimum balance of {self.minimum_balance}.")
            
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

    def __repr__(self):
        return f"MinBalanceAccount(User: {self.username}, Balance: {self.balance:.2f}, Min: {self.minimum_balance:.2f})"

class ATM:
    def __init__(self, account_list, try_limit):
        
        if not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("account_list must contain only BankAccount or MinimumBalanceAccount instances.")
        
        self.account_list = account_list
        
        try:
            if not isinstance(try_limit, int) or try_limit <= 0:
                raise ValueError
            self.try_limit = try_limit
        except ValueError:
            print("Invalid try_limit input. Setting try_limit to default (2).")
            self.try_limit = 2
            
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Log In")
            print("2. Exit")
            choice = input("Select an option (1 or 2): ").strip()

            if choice == '1':
                print("--- Login ---")
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                self.log_in(username, password)
            elif choice == '2':
                print("Thank you for using the ATM. Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")

    def log_in(self, username, password):
        
        while self.current_tries < self.try_limit:
            
            for account in self.account_list:
                if account.authenticate(username, password):
                    print(f"\nLogin successful for user {username}.")
                    self.current_tries = 0
                    self.show_account_menu(account)
                    account.authenticated = False
                    return
            
            self.current_tries += 1
            print(f"Login failed. Tries remaining: {self.try_limit - self.current_tries}")
            
            if self.current_tries >= self.try_limit:
                print("Maximum login attempts reached. System shutting down.")
                sys.exit()
                
            print("\n--- Try Again ---")
            username = input("Enter Username: ")
            password = input("Enter Password: ")

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu ({account.username}) ---")
            print(f"Current Balance: {account.balance:.2f}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Log Out")
            choice = input("Select an option: ").strip()

            try:
                if choice == '1':
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == '2':
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == '3':
                    print(f"Logging out user {account.username}.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    
    acc1 = BankAccount("user1", "pass1", 500)
    acc2 = MinimumBalanceAccount("user2", "pass2", 200, 50)
    
    accounts = [acc1, acc2]
    
    atm = ATM(accounts, 3)