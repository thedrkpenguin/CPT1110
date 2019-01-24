import os
import sqlite3

#Set absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Inventory.db")

#Open connection to database
database_connection = sqlite3.connect(db_path)
cursor = database_connection.cursor()

#Add product to inventory
def addInventory():
	item_name = input("Name: ")
	item_quantity = int(input("Quantity: "))
	cursor.execute("INSERT INTO Inventory VALUES(?, ?)", (item_name.upper(), item_quantity))
	database_connection.commit()
	print("Item added successfully.")

	
#Delete product from inventory
def removeInventory():
	item_to_delete = input("Name: ")
	try:
		cursor.execute("DELETE FROM Inventory WHERE ITEM=?", (item_to_delete.upper(),))
		database_connection.commit()
		print("Item deleted.")
	except:
		print("No such record found.")


#Update product quantity that already exists
def updateInventory():
	item_to_update = input("Name: ")
	new_quantity = int(input("New quantity: "))
	cursor.execute("UPDATE Inventory SET QUANTITY=? WHERE ITEM=?", (new_quantity, item_to_update.upper()))
	database_connection.commit()
	print("Update successful.")
	
	
#Search inventory for item and display its info
def searchInventory():
	search_query = input("Name: ")
	try:
		cursor.execute("SELECT ITEM,QUANTITY FROM Inventory WHERE ITEM=?", (search_query.upper(),))
		results = cursor.fetchone()
		print(f'''ITEM: {results[0]}QUANTITY: {results[1]}''')
	except:
		print("No such record found.")


#Print contents of entire inventory
def printInventory():
	cursor.execute("SELECT * FROM Inventory")
	results = cursor.fetchall()
	if results == []:
		print("\nNo items in inventory.")
	else:
		for x in results:
			print(f'''{x[0]}: {x[1]}''')	


#Conditional that calls specified function
def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        updateInventory()
    elif CHOICE == 4:
        searchInventory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 99:
        exit()

#Boolean to set while loop
program_in_use = True

#Prints menu, prompts user for input to pass to menuSelection()
while program_in_use == True:
    print('\n=============================')
    print ('= Inventory Management Menu =')
    print ('=============================')
    print ('(1) Add New Item to Inventory')
    print ('(2) Remove Item from Inventory')
    print ('(3) Update Inventory')
    print ('(4) Search Item in Inventory')
    print ('(5) Print Inventory Report')
    print ('(99) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)
