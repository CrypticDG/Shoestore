
#========The beginning of the class==========

# itertools.product() is used to find the cartesian product from the given iterator, 
# output is lexicographic ordered.
# The itertools.product() can used in two different ways:
# pip install tabulate
# pip install --upgrade tabulate

from itertools import product
from tabulate import tabulate

# Parent class
class Shoe:
    # inititialize objects
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    # Return the cost of the shoe
    def get_cost(self):
        return self.cost
               
    # Return the quantity of the shoe
    def get_quantity(self):
        return self.quantity
      
    # retrun string representation of a class
    def __str__(self):
        
        return f"Country: {self.country} , Code: {self.code}, Product: {self.product} , Cost: R{self.cost} , Quantity: {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
'''
# https://sparkbyexamples.com/python/read-a-text-file-into-a-string-and-strip-newlines-in-python/
    try:
        with open('inventory.txt', 'r') as file:
            next(file) # skip header
            for line in file:
                temp = line.strip()
                temp = line.split(",")
                # print(temp)
                shoe = Shoe(*temp)
                shoe_list.append(shoe)
        print("Inventory data has been read from txt file")
    except FileNotFoundError:
            print("The File you are tyring to read does not exist.")

def capture_shoes():
    
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # get user input for shoe object and append to shoe_list
    country = input("Enter the country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the shoe name: ")
    cost = input("Enter the cost of the shoe: ")
    quantity = input("Enter the quantity of the shoes vailable: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe data has been captured.")

def view_all():
    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    new_data = []
    for shoe in shoe_list:
        new_data.append([shoe.country, shoe.code, shoe.product, f"R{shoe.cost}", shoe.quantity])
    print(tabulate(new_data, headers=headers))

def re_stock():
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    lowest_qty_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"The shoe with the lowest quantity is: {lowest_qty_shoe}")
    add_qty = input("Do you want to add more quantity to this shoe? (y/n): ")
    if add_qty.lower() == "y":
        qty_to_add = input("Enter the quantity to add: ")
        lowest_qty_shoe.quantity += int(qty_to_add)
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        with open("inventory.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[1] == lowest_qty_shoe.code:
                    data[-1] = str(lowest_qty_shoe.quantity)
                    line = ",".join(data) + "\n"
                file.write(line)
        print("Quantity has been updated on the inventory file.")
    else:
        print("Quantity has not been updated.")

def search_shoe():
    
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter your shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"The shoe with code {code} is: {shoe}")
            break
    else:
        print(f"Shoe with code {code} not found.")

def value_per_item():
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

    headers = ["Product", "Total Value"]
    new_data = []
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        new_data.append([shoe.product, f"R{total_value}"])
    print(tabulate(new_data, headers=headers))


def highest_qty():
    
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    max_qty_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"Highest quantity shoe for sale is: {max_qty_shoe}")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''


while True: 

    print("Welcome to the Shoe inventory program.\n")

    menu = input('''Please select one of the following options below.\n               
rsd - Read the shoe data from list
ad - Add a new shoe to inventory.
va - View all, print details of shoes.
rs - Restock the shoe with the lowest quantity.
ss - Search shoe useing shoe code.
iv - View the values of all the shoes.                
hq - View shoe with highest quantity.
e  - Exit.
''').lower().strip()
    
    if menu == 'rsd':
        read_shoes_data()

    elif menu == 'ad':
        capture_shoes()

    elif menu == 'va':
        view_all()

    elif menu == 'rs':
        re_stock()

    elif menu == 'ss':
        search_shoe()

    elif menu == 'iv':
        value_per_item()

    elif menu == 'hq':
        highest_qty()

    elif menu == 'e':
        print("Goodbye, have a nice day.")
        exit()

    else:
        print("You have made the wrong selection, please try again.")