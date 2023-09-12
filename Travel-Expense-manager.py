# asks to user how many days will travel and the budget he has, with try/except statement that assure the correctness of user's input
check = False
while check == False:
    try:
        day_of_travel = int(input('How many days is the trip? '))
        check = True
    except ValueError:
        print('Please enter an integer')
check_01 = False
while check_01 == False:
    try:
        budget = float(input('What\'s your budget in euros? '))
        check_01 = True
    except ValueError:
        print('Please enter a float number')

# defines variables for expenses totals 
lodging_total = 0
food_total = 0
transportation_total = 0 
entertainment_total = 0


# defines variables where store strings with the single expense of each day, for each category
lodging_list = '_'
food_list = '_'
transportation_list = '_'
entertainment_list = '_'

# for loop that run many times as user's day's travel
for day in range(1,int(day_of_travel) + 1):
    print(f'Day {day}')
# asks to user daily lodging's expense, with a try/except statement to assure that user type a float
    check_02 = False
    while check_02 == False:
        try:
            lodging = float(input(f'how much do you want to pay for lodging in day {day} ? '))
            check_02 = True
        except ValueError:
            print('Please enter a float number')
# adds to specific variable the expense as string separating it to the next with an underscore
    lodging_list += f'{lodging}_'
# asks to user daily food's expense, with a try/except statement to assure that user type a float
    check_03 = False
    while check_03 == False:
        try:
            food = float(input(f'how much do you want to pay for food in day {day} ? '))
            check_03 = True
        except ValueError:
            print('Please enter a float number')
# adds to specific variable the expense as string separating it to the next with an underscore
    food_list = f'{food}_'
# asks to user daily transportation's expense, with a try/except statement to assure that user type a float
    check_04 = False
    while check_04 == False:
        try:
            transportation = float(input(f'how much do you want to pay for transportation in day {day} ? '))
            check_04 = True
        except ValueError:
            print('Enter a float number')
# adds to specific variable the expense as string separating it to the next with an underscore
    transportation_list = f'{transportation}_'
# asks to user daily entertainment's expense, with a try/except statement to assure that user type a float
    check_05 = False
    while check_05 == False:
        try:
            entertainment = float(input(f'how much do you want to pay for entertainment in day {day} ? '))
            check_05 = True
        except ValueError:
            print('Please enter a float number')
# adds to specific variable the expense as string separating it to the next with an underscore
    entertainment_list = f'{entertainment}'
# adds day by day the expenses to relative toatal variable
    lodging_total += lodging
    food_total += food
    transportation_total += transportation
    entertainment_total += entertainment
# while loop to let user modify the expenses of previous days and updates the relative total variable for each category,with try/except statements that check and assure the correctness of user's input
    answer = 'yes'
    while answer == 'yes':
        answer = input('Do you want to make some change? (Type "yes" to accept or something else to continue) ').replace(' ', '')
        if answer != 'yes':
            continue
# asks to user wich expense's category wants to update
        charge_category = input('Enter the category of charge you want to make a change: (lodging,food,transportation,entertainment) ').replace(' ', '')
# if statement for lodging's expenses choose, and asks day to modify and the new value, with try/except statements to assure correctness of user input  
        if charge_category == 'lodging':
            check_06 = False
            while check_06 == False:
                try:
                    new_day_lodging = int(input('Enter the day: '))
                    check_06 = True
                except ValueError:
                    print('Please enter a whole number')
            check_07 = False
            while check_07 == False:
                try:
                    new_charge_lodging = float(input('Enter new value: '))
                    check_07 = True
                except ValueError:
                    print('Please enter a float number')
# for loop that iterates the string, count the underscore to find the one that corresponds to the day choosed by user and slice the string before
            counter_lodging = 0
            for char_index_lodging in range(0, len(lodging_list)):
                if lodging_list[char_index_lodging] == '_':
                    counter_lodging += 1
                    if counter_lodging == new_day_lodging:
                        sliced_lodging_list = lodging_list[char_index_lodging + 1:]
# for loop that iterates the new string to find the first underscore and slice after it getting the expense choosed by user, then store it in a variable
            second_counter_lodging = 0
            for char_ind_lodging in range(0, len(sliced_lodging_list)):
                if sliced_lodging_list[char_ind_lodging] == '_':
                    second_counter_lodging +=1
                    if second_counter_lodging == 1:    
                        old_charge_lodging = sliced_lodging_list[:char_ind_lodging]
# substracts the old expense from the total and then adds the new one
            lodging_total -= float(old_charge_lodging)
            lodging_total += new_charge_lodging
# if statement for food's expenses choose, and asks day to modify and the new value, with try/except statements to assure correctness of user input
        if charge_category == 'food':
            check_08 = False
            while check_08 == False:
                try:    
                    new_day_food = int(input('Enter the day: '))
                    check_08 = True
                except ValueError:
                    print('Please enter a whole number')
            check_09 = False    
            while check_09 == False:
                try:
                    new_charge_food = float(input('Enter new value: '))
                    check_09 = True
                except ValueError:
                    print('Please enter a decimal number')
# for loop that iterates the string, count the underscore to find the one that corresponds to the day choosed by user and slice the string before
            counter_food = 0
            for char_index_food in range(0, len(food_list)):
                if food_list[char_index_food] == '_':
                    counter_food += 1
                    if counter_food == new_day_food:
                        sliced_food_list = food_list[char_index_food + 1:]
# for loop that iterates the new string to find the first underscore and slice after it getting the expense choosed by user, then store it in a variable 
            second_counter_food = 0
            for char_ind_food in range(0,len(sliced_food_list)):
                if sliced_food_list[char_ind_food] == '_':
                    second_counter_food += 1
                    if second_counter_food == 1:
                        old_charge_food = sliced_food_list[:char_ind_food]
# substracts the old expense from the total and then adds the new one
            food_total -= float(old_charge_food)
            food_total += new_charge_food
# if statement for transportation's expenses choose, and asks day to modify and the new value, with try/except statements to assure correctness of user input
        if charge_category == 'transportation':
            check_10 = False
            while check_10 == False:
                try:    
                    new_day_transportation = int(input('Enter the day: '))
                    check_10 = True
                except ValueError:
                    print('Please enter a whole number')
            check_11 = False
            while check_11 == False:
                try:
                    new_charge_transportation = float(input('Enter new value: '))
                    check_11 = True
                except ValueError:
                    print('Please enter a decimal number')
# for loop that iterates the string, count the underscore to find the one that corresponds to the day choosed by user and slice the string before
            counter_transportation = 0
            for char_index_transportation in range(0, len(transportation_list)):
                if transportation_list[char_index_transportation] == '_':
                    counter_transportation += 1
                    if counter_transportation == new_day_transportation:
                        sliced_transportation_list = transportation_list[char_index_transportation + 1:]
# for loop that iterates the new string to find the first underscore and slice after it getting the expense choosed by user, then store it in a variable
            second_counter_transportation = 0
            for char_ind_transportation in range(0, len(sliced_transportation_list)):
                if sliced_transportation_list[char_ind_transportation] ==  '_':
                    second_counter_transportation += 1 
                    if second_counter_transportation == 1:
                        old_charge_transportation = sliced_transportation_list[:char_ind_transportation]
# substracts the old expense from the total and then adds the new one
            transportation_total -= float(old_charge_transportation)
            transportation_total += new_charge_transportation
# if statement for entertainment's expenses choose, and asks day to modify and the new value, with try/except statements to assure correctness of user input
        if charge_category == 'entertainment':
            check_12 = False
            while check_12 == False:
                try:    
                    new_day_entertainment = int(input('Enter the day: '))
                    check_12 = True
                except ValueError:
                    print('Please enter a whole number')
            check_13 = False
            while check_13 == False:
                try:
                    new_charge_entertainment = float(input('Enter new value: '))
                    check_13 = True
                except ValueError:
                    print('Please enter a decimal number')
# for loop that iterates the string, count the underscore to find the one that corresponds to the day choosed by user and slice the string before
            counter_entertainemet = 0
            for char_index_enetertainment in range(0, len(entertainment_list)):
                if entertainment_list[char_index_enetertainment] == '_':
                    counter_entertainemet += 1
                    if counter_entertainemet == new_day_entertainment:
                        sliced_entertainment_list = entertainment_list[char_index_enetertainment + 1:]
# for loop that iterates the new string to find the first underscore and slice after it getting the expense choosed by user, then store it in a variable
            second_counter_entertainment = 0
            for char_ind_entertainment in range(0, sliced_entertainment_list):
                if sliced_entertainment_list[char_ind_entertainment] == '_':
                    second_counter_entertainment += 1
                    if second_counter_entertainment == new_charge_entertainment:
                        old_charge_entertainment = sliced_entertainment_list[:char_ind_entertainment]
# substracts the old expense from the total and then adds the new one
            entertainment_total -= float(old_charge_entertainment)
            entertainment_total += new_charge_entertainment

# defines a variable for grand total and calculate it using a for loop that iterate trought the totals of each category
grandtotal = 0

for total in (lodging_total,food_total,transportation_total,entertainment_total):
    grandtotal += total

# prints a message with the totals expenses for each category, the grand total and if it exceed the initial budget extimation

print(f'The total expense for lodging is {lodging_total:.2f} €, for food is {food_total:.2f} €, for transportation is {transportation_total:.2f} €, for entertainment is {entertainment_total:.2f} €. The grand total of your travel is {grandtotal:.2f} €.')

if grandtotal > budget:
    print(f'Attention, the whole expense of your travel exceeded the initial budget estimated.')


