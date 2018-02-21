from main_module import contact_list


decorated =[(int(contact[1]),contact) for contact in contact_list]
decorated.sort()
sorted =[contact[1] for contact in decorated]
contact_list = [[contact[0]] for contact in sorted]

print (contact_list)

