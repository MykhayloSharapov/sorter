contact_list = []

while True:
    name = input ('Input name and surname:')
    while True:
        try:
            age = int (input('Input age:'))
        except ValueError:
            print ('You have to input integer!')
            continue
        else:
            break
    while True:
        gender = input ('Input gender: M/F? ')
        if gender != 'M' and gender != 'F':
            print ('Input either capital M or capital F!')
            continue
        else:
            if gender == 'M':
                title = 'Mr'
            elif gender == 'F':
                title = 'Ms'
            break
    contact_list.append ([title,name,age])
    man_inp_finish = input ('Finished: Y/N?')
    if man_inp_finish == 'Y':
        break
    elif man_inp_finish == 'N':
        continue
    else:
        print ('Input either capital Y or capital N!')

print (contact_list)
