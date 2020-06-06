# mortgage.py
#
# Exercise 1.7

debth = 500000
prc = 0.05
payment = 2684.11
total_paid = 0
month = 0

monthly_payment = 0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while debth > 0:    
    month += 1        
    if month >= extra_payment_start_month and month <= extra_payment_end_month:        
        monthly_payment = payment + extra_payment               
    else:        
        monthly_payment = payment       

    if debth - monthly_payment < 0:        
        monthly_payment = debth        
        debth = 0
    else:
        debth = debth * ( 1 + 0.05 / 12 ) - monthly_payment   

    total_paid += monthly_payment
    print(f'Month: {month:<5d} Payment: {monthly_payment:<10.2f} Debth: {debth:<10.2f}')

print('--------')    
print(f'{"Total paid:":<21s} {total_paid:<12.2f}')
print(f'{"Number of month:":<21s} {month:<12d}')
