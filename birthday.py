#bday=dict()
bday={'lela':'07/09','mum':'09/05','dad':'29/12','erin':'01/10'}
who=None
print("---------------------------------- ")
print('Welcome to the birthday dictionary')
print(" ")
print("Enter a name to look up a birthday or type 'done' to quit")
print("To add a new birthday type 'add'")

while who!=('done'):
    who=input(">>")
    who=who.lower()
    if who in bday.keys():
        print(who.title(),'s birthday is',bday[who])
    elif who=='done': break
    elif who=='add':
        friend=input('Enter the name of the friend you want to add ')
        bdate=input('Enter',friend,'birthday')
        newtup=(friend,bdate)
        if newtup in bday:
            print(friend,'birthday already known',bday[friend])
        else:
            bday.append(newtup)
            print('friend, has been added')
    else: print('No entry for',who)
    #continue

exit()
