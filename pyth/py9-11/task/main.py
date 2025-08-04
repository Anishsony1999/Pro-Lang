from ab import Bank,User
import sql


users = [
    User("Anisha","anishsony1999","123"),
    User("Anu","anussharv@gmail","123"),
    User("Anish","anishamony@gmail.com","12345")
    
]

bank = Bank()

# password = "12345"

# user = bank.check_password(users,password)
# bank.withdrow(user,10)
# print(bank.deposite(user,20))


for user in users:
    sql.insert_data(user)