seals_tower_height = 443 # meters
one_dollar_width = 0.11 * 0.001 # meters
day = 1
nbr_bills = 1
while nbr_bills * one_dollar_width < seals_tower_height:
    print('Day: ', day, ' Hieght: ', nbr_bills * one_dollar_width, ' Nbr of bills: ', nbr_bills)
    day += 1    
    nbr_bills *= 2
print('Number of days:', day)
print('Number of bills:', nbr_bills)

