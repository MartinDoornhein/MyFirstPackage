import src.accounts as acc
import src.bank as bank


b = bank.Bank("md_bank")

acc1 = b.create_savings_account("John", 4000)
acc2 = b.create_savings_account("berth", 2000)
print(acc1._created)
print(acc1.balance)
print(acc1.withdraw(200))
print(acc1.balance)

print(b.list_accounts())

# if __name__ == "__main__":      
#     s_acc1 = acc.Savings_Account("martin", 123, 1000, 1.05)
#     s_acc1.compound_interest_calculator(7)
#     s_acc1.add_interest()


    
