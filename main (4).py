price=1000000
good_credit=True

if good_credit:
    discount=0.1 * price #10% off
else:
    discount=0.2 * price #20% off
    
print(f"Price after discount: ${discount}")