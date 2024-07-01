import src.accounts as acc

if __name__ == "__main__":      
    s_acc1 = acc.Savings_Account("martin", 123, 1000, 1.05)
    s_acc1.compound_interest_calculator(7)
    s_acc1.add_interest()


    
