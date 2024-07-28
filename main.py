# Initialize data set
AllowedVehicleList = [
    'Ford F-150', 'Chevolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra',
    'Nissan Titan'
]
#print menu
def print_menu():
  print("********************************")
  print("AutoCountry Vehicle Finder v0.4")
  print("********************************")
  print(" Please Ender the following number below from the following menu:")
  print()
  print("1. PRINT all Allowed Vehicles")
  print("2. SEARCH for Authorized Vehicle")
  print("3. ADD Authorized Vehicle")
  print("4. DELTE Authorized Vehicle")
  print("5. EXIT")
  print("20240728_LeeAnthony_Project0-4")
  print("********************************")
#print Allowed Vehicles
def print_AllowedVehicles():
  print("AllowedVehicleList:")
  for vehicle in AllowedVehicleList:
    print(vehicle)
#search function
def search_AllowedVehicles():
  search_term = input("Please Enter the full Vehicle Name: ")
  if search_term in AllowedVehicleList:
    print(f"{search_term} is an authorized vehicle")
  else:
    print(f"{search_term} is not an authorized vehicle, if you received this in error please check the spelling and try again:")
#add function
def Add_AllowedVehicle():
  newVehicle = input("Please Enter the full Vehicle Name you would like to add: ")
  if newVehicle in AllowedVehicleList:
    print("This Vehicle is already in the list")
  else:
    AllowedVehicleList.append(newVehicle)
    print(f"You have added {newVehicle} as an authorize vehicle")
#delete function
def delete_AllowedVehicle():
  print("Please Enter the full vehicle name you would like to remove")
  deletedVehicle = input()
  if deletedVehicle in AllowedVehicleList:
    print(f"are you sure you want to remove {deletedVehicle}  from the Authorized Vehicles List")
    choice = input()
    if choice == "yes":
      AllowedVehicleList.remove(deletedVehicle)
      print(f"You have REMOVED {deletedVehicle} as an authorized vehicle")
    elif choice == "no":
      print_menu()
  else :
      print(f"{deletedVehicle} is not on the Authorized Vehicles List")
def main():
  print_menu()  #print menu on program start
  #loop to display vehicles on 1 or close on 2
  while True:
    choice = input("Enter your choice: ")
    if choice == "1":
      print(
          "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
      )
      print_AllowedVehicles()  #function to print vehicles
      print_menu()  #function to print menu
    elif choice == "2":
      search_AllowedVehicles()  #function to search for vehicles
      print_menu()  #function to print menu
    elif choice == "3":
      Add_AllowedVehicle()
      print_menu()
    elif choice == "4":
      delete_AllowedVehicle()
      print_menu()
    elif choice == "5":
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      break
    else:
      print("Invalid choice, Enter a valid choice")
      print_menu()

if __name__ == "__main__":
  main()
