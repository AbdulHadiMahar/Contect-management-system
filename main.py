import os
contacts = {}
def load_contacts():
   if os.path.exists('conts.txt'):
      with open('conts.txt', 'r') as f:
         for line in f:
             line.strip()
             if line and ':' in line:
                key,value = line.split(':', 1)
                contacts[key.strip()] = value.strip()
load_contacts()                
def menu():
     try:
         return int(input("\nPress 1 to view all contact list \n" 
         "press 2 to add a new contact\n"
         "press 3 to edit a contact \n" 
         "press 5 to search a contact\n"
         "press 9 to delete a contact\n" 
         "0 to exit a contact : "))
     except ValueError:
         print("Entre a value integer : ") 
         return menu()  
def ex():
    try:
        return int(input("press 1 to open menu and 0 to exit :  "))
    except ValueError:
        print("Entre a valid integer : ")
        return ex()
def edit():
    return input('Entre the name of contact you want to edit : ')
u = menu()
while True:
     match u:
        case 1:
            if len(contacts)== 0:
               print("You have 0 contacts")
               n= ex()
               if n==1:
                  u = menu()
               else:
                  u=0
                  print("You are out")
                  n= ex()
                  if n==1:
                     u = menu()
                  else:
                     u = 0
                  
            else:
               print(f"You have {len(contacts)} contacts")
               for keys,values in contacts.items():
                  print(f"{keys} : {values}") 
                  break     
        case 2:
           name1=input("Ente the name of contact : ")
           number1 = input("Entre the number of contact : ")
           if len(number1) < 11 or len(number1)>11:
               print("Entre a number of 11 digits") 
               number1 = input("Entre the number of contact : ")
           else:
             contacts[name1] = number1
             print('Contact is succesfully added see it in contact list')
             n= ex()
             if n==1:
                 u = menu()
             else:
                  u = 0    
        case 3:
             e = edit()
             if e in contacts:
                 print(contacts[e])
                 e0 = input("If you want to edit its name press 'a' and press 'b' to edit its number : ")
                 match e0:
                     case 'a':
                         enam=input(f"Entre the name to change with {e} : ")
                         contacts[enam] = contacts[e]
                         del contacts[e]
                         print("The contact is succusfully edited")
                         n = ex()
                         if n==1:
                          u = menu()
                         else:
                           print("You are out")
                           u = 0
                     case 'b' :
                         ename=input(f"Entre the number you want to change with {e}")
                         contacts[e] = ename
                         print("The contact is succusfully edited")
                         n= ex()
                         if n==1:
                          u = menu()
                         else:
                           print("You are out")
                           u = 0    
                     case _:
                         print("Entre a walid choice")       
             else:
                 print(f"{e} is not a existed contact")
                 n= ex()
                 if n==1:
                  u = menu()
                 else:
                  
                  u = 0 
        case 5:
           s1 = input("Entre the name of contact you want to search : ")
           if s1 in contacts:
              print(contacts[s1])
              n= ex()
              if n==1:
                  u = menu()

              else:
                  u = 0
           else:
              print(f"there is no contact existed with name {s1}")
              n= ex()
              if n==1:
                  u = menu()
              else:
                  u = 0
                  print("You are out")    
        case 9:
           del1= input('Entre the name of contact you want to delete : ')
           if del1 in contacts:
             del contacts[del1]
             print(f'The {del1} is deleted fron contactlist')
             n= ex()
             if n==1:
                  u = menu()
             else:
                  u = 0
                  print("You are out")
           else:
              print("Contact does not exist")
              n= ex()
              if n==1:
                  u = menu()
              else:
                  u = 0
                  print("You are out")    
        case 0:
            print("Saving to : ", os.path.abspath('conts.txt'))
            with open('conts.txt', 'w') as f:
               for keys,values in contacts.items():
                    f.write(f"{keys} : {values}\n") 
               print(contacts)
               f.write("\n")
            print("You are out")
            break
        case _:
            print("entre a valid choice : ")
            u = menu()
