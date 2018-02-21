contact_list = []

def det_title(y):
    if y =='M':
        title = 'Mr'
    elif y=='F':
        title = 'Ms'
    else:
        title = 'smb'
    return title

with open ('contactlist.txt','r') as f:
    for line in f.readlines():
        x=line.split(',')
        try:
            contact_list.append([det_title(x[1])+' '+x[0],int(x[2])])
        except Exception:
            pass


       
        
