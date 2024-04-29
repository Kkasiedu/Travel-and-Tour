
username_1="Kofi"
password_1="Password"
username= ""
password= ""

def Login_Screen():
  print("------------------")
  print("LOGIN")
  print("------------------")
  print("1. Login")
  print("2. Exit")
  print("Enter Choice:")
  choice=input()
  if choice == "1":
      Login()
      Main_menu()
  elif choice =="2":
     print("Exiting............")
  else :
     print("Invalid Option!!")
     Login_Screen()

def Login():
  username=input("Username: ")
  password=input("Password: ")
 
  if username != username_1 or password != password_1:
    print("Invalid Username or Password")
    Login_Screen()
  else:
   print("Login Successful!!")

def Main_menu():
  print("-----------------")
  print("MAIN MENU")
  print("------------------")
  print("1. Location")
  print("2. Reservation")
  print("3. Back")
  print("4. Exit")
  Input = input("Enter Option: ")
  if Input == '1':
     Location()
  elif Input == '2':
     print("Still under construction")
  elif Input == '3':
    Login_Screen()
  elif Input == '4':
    print("Exiting...........")
  else:
     print("Invalid Input!!!")
     Main_menu()


def Add_Location():
   Locations={}
   location_name=input("Name of location: ")
   city= input("Name of city: ")
   country=input("Name of country: ")

   Locations[location_name] = {'city': city, 'country': country}

   print(f"Added location: {location_name} - City: {city}, Country: {country}")
   print("Location Added successfully")
   print("Returning to Location Menu.....")
   Location()

def Location():
   Locations=[]
   print("----------------")
   print("LOCATION"   )
   print("----------------")
   print("1. Add Location")
   print("2. Remove Location")
   print("3. View all Locations")
   print("4. Back")
   print("5. Exit ")
   Choose=input(print("Enter Option: "))
   if  Choose=='1':
      Add_Location()
   elif  Choose=='2':
      print("Still under construction")
   elif  Choose=='3'and len(Locations) == 0:
      print("No Locations Avaliable")
   elif Choose == '3' and len(Locations) > 0:
      print(len(Locations))
   elif Choose ==  '4':
      Main_menu()
   elif Choose =='5':
     print("Exiting......")
   else :
    Location()


def Reservation():
 print("------------------")
 print("RESERVATION")
 print("------------------")
 print("1. Make reservation")
 print("2. Check reservation")
 print("3. Back")
 print("4. Exit")
 Res_Choice=input("Enter Choice :")
 if Res_Choice == '1':
    Make_Reservation()
 elif Res_Choice == '2':
    Check_Reservation()
 elif Res_Choice == '3':
    Main_menu()
 elif Res_Choice() == '4':
    print("Exiting.......")  
 else:
    Reservation()


def Make_Reservation():
   print("Still under construction")

def Check_Reservation():
   print("Still under construction")




Login_Screen()