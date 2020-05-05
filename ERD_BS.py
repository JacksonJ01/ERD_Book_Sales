# Jackson J
# 5.2.2020
# This file contain 4 tables that use the sqlite3 import.
# This program will allow the user to:
# -create(add) new customers and books
# -modify those tables
# -print the contents of the table
# -delete from that table
# These will all be in menu's presented to the user
# New editions to this program are the Order and OrderLineItems tables
# There will be a one to many relationship between the Person table and the Order table
# Likewise there will be a many to one relationship between the Order_Line_Item table and the Book table
import sqlite3
from sqlite3 import Error
from datetime import datetime


# Creates the database
def database(connection):
    connect = None
    try:
        connect = sqlite3.connect(connection)
        print('connection successful'.upper())
    except Error as oops:
        print('There has been an error:', oops)
    return connect


# Executes the table queries
# Takes the query as a parameter
def create_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"The query executed successfully")
    except Error as oops:
        print(f"There has been an error: {oops}")


# Executes the insert into queries
# Takes the query as a parameter
def read_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"There has been an error: {e}")


# Creates a separation between the menus
def partition():
    print("\n\n" +
          "__" * 70)
    return


# This variable holds the Person table
person_table = """
CREATE TABLE IF NOT EXISTS 
  customer (
  customer_id    INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name     TEXT    NOT NULL,
  last_name      TEXT    NOT NULL,
  street_address TEXT    NOT NULL,
  zip_code       INTEGER NOT NULL,
  city           TEXT    NOT NULL,
  state          TEXT    NOT NULL
);
"""

# This variable holds the Book table
book_table = """
CREATE TABLE IF NOT EXISTS
  book (
  book_id   INTEGER PRIMARY KEY AUTOINCREMENT,
  title     TEXT    NOT NULL,
  author    TEXT    NOT NULL,
  isbn      TEXT NOT NULL,
  edition   INTEGER NOT NULL,
  price     TEXT NOT NULL,
  publisher TEXT    NOT NULL
);
"""

# This variable holds the Order table which uses the customer_id from the customer table
# I spent an 1 on this table because for some reason the create_table definition didn't like order and the name of the table
order_table = """
CREATE TABLE IF NOT EXISTS
  ordering (
  order_number INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date   TEXT,
  order_total  TEXT,
  customer_id  INTEGER,
  CONSTRAINT order_fk_customer
  FOREIGN KEY (customer_id)
  REFERENCES customer (customer_id)
);
"""

# This variable holds the Order_Line_Item table which uses the Order and Book table
order_line_item = """
CREATE TABLE IF NOT EXISTS
  order_line_item (
  order_number INTEGER,
  book_id      INTEGER,
  quantity     INTEGER,
  PRIMARY KEY (order_number, book_id),
  CONSTRAINT oli_fk_order
  FOREIGN KEY (order_number)
  REFERENCES ordering (order_number),
  CONSTRAINT oli_fk_book
  FOREIGN KEY (book_id)
  REFERENCES book (book_id)
);  
"""

input("press enter".upper())
connecting = database("myDatabase")

print("\nWhy hello there."
      "\nI'm going to keep this short and quick:"
      "\nToday I have a program for you that utilizes a cool thing called sqlite3."
      "\nThere are menu's you can use to explore the program as you wish."
      "\nYou will only need to use the numbers on your keyboard."
      "\nWhen entering information, be weary of any spaces")

# If the user wishes to the tables they can
# In testing I wanted a fresh start so I would manually clear, but then I added this in to make it easier for and users
# In a practical use, there would probably have to be 'key' or pin number, for those with the authority, to clear these tables
clear = input("\nWould you like to clear all or some of the information in the database? (Y or N)"
              "\n>>>").title()
if clear == "Y":
    # This is the menu presented to the user that allows them to clear tables of their choice
    while clear != "N":
        partition()
        clear = input("\n*PICK THE NUMBER NEXT TO YOUR DESIRED CHOICE*"
                      "\n1. CLEAR Customer Table"
                      "\n2. CLEAR Book Table"
                      "\n3. CLEAR Ordering Table"
                      "\n4. CLEAR Order Line Item Table"
                      "\n5. CLEAR ALL"
                      "\n6. Leave this menu"
                      "\n>>>")
        # Checks if the user entered a valid number in the menu
        while clear != "#If the user wants to delete some of the tables they can":
            try:
                clear = int(clear)
                if 7 > clear > 0:
                    break
                else:
                    int("#Force Fail")
            except ValueError:
                clear = input("Enter a number 1-6")

        # Clears the Customer table
        if clear == 1:
            drop_table = """
            DROP TABLE IF EXISTS
              customer"""
            create_table(connecting, drop_table)

        # Clears the Book table
        elif clear == 2:
            drop_table = """
            DROP TABLE IF EXISTS
              book"""
            create_table(connecting, drop_table)

        # Clears the Ordering table
        elif clear == 3:
            drop_table = """
            DROP TABLE IF EXISTS
              ordering"""
            create_table(connecting, drop_table)

        # Clears the Order Line Item table
        elif clear == 4:
            drop_table = """
            DROP TABLE IF EXISTS
              order_line_item"""
            create_table(connecting, drop_table)

        # Clears all of the tables
        elif clear == 5:
            clear = input("\nAre you sure? (Y or N)"
                          "\n>>>").title()

            if clear == "Y":
                drop_table = """
                DROP TABLE IF EXISTS
                 customer"""
                create_table(connecting, drop_table)

                drop_table = """
                DROP TABLE IF EXISTS
                 book"""
                create_table(connecting, drop_table)

                drop_table = """
                DROP TABLE IF EXISTS
                 ordering"""
                create_table(connecting, drop_table)

                drop_table = """
                DROP TABLE IF EXISTS
                 order_line_item"""
                create_table(connecting, drop_table)

            else:
                clear = "No"
        else:
            clear = "N"


input("\npress enter to connect the tables to the database\n".upper())

create_table(connecting, person_table)  # Adds the person table to the database
create_table(connecting, book_table)  # Adds the books table to the database
create_table(connecting, order_table)  # Adds the ordering table to the database
create_table(connecting, order_line_item)  # Adds the order_line_item tables to the database

print("\nNice! Have fun")

# This is the menu that runs the whole program
# It is somewhat sophisticated, including try statements to keep the users from crashing the program.
# However this program is 'long' so it may have failures in places I never thought #PeopleBreakThings
# It includes a Main Menu, three sub menu's, and 2 more sub menu's from there
# The reason the Order and Order Line Item table don't have a sub menu for modification is because the user can delete that order and place another one
# I feel like there would be too many errors otherwise#
menu = "ONWARD"
while menu != "END":
    partition()
    input("\npress enter".upper())
    # This is the main menu of the program. It is in a while loop and allows the user to choose to what they want to do
    choice = input("\nWould you like to do?" +
                   "\n*press the number next to your desired choice*".upper() +
                   "\n\n1. Go to the Customers Menu"
                   "\n2. Go to the Books Menu"
                   "\n3. Go to the Ordering Menu"
                   "\n4. Leave this program"
                   "\n>>>")
    # Checks if the choice they entered is valid
    while choice != "A Long And Random String Of Text":
        try:
            choice = int(choice)
            if 5 > choice > 0:
                break
            else:
                int("# Forces this try statement to fail if the choice isn't 1, 2, 3, or 4")
        except ValueError:
            choice = input("Enter 1, 2, 3, or 4"
                           "\n>>>")

    # If the user chooses 1 in the main menu they will be take to another menu for customers
    if choice == 1:
        menu = "ONWARD"
        while menu != "END":
            partition()
            input("\npress enter".upper())
            # This menu allows the user to add, modify, delete, and print the customers
            choice = input("\nWhat would you like to do?"
                           "\n1. ADD new customer"
                           "\n2. MODIFY a customer"
                           "\n3. DELETE a customer"
                           "\n4. Print the customer table"
                           "\n5. Leave this menu"
                           "\n>>>")
            # Checks if the user entered a choice on the menu
            while choice != "A Long And Random String Of Text":
                try:
                    choice = int(choice)
                    if 6 > choice > 0:
                        break
                    else:
                        int("# Forces this try statement to fail if the choice isn't 1, 2, 3, 4, or 5")
                except ValueError:
                    choice = input("Enter 1, 2, 3, 4, or 5"
                                   "\n>>>")

            # This part of the program gets the information for a new customer, then saves the information in variables
            if choice == 5:
                print("Back to the main menu it is.")
                break

            elif choice == 1:
                first_name = input("\nWhat is the customer's First Name?"
                                   "\n>>>").title()

                last_name = input("\nLast Name?"
                                  "\n>>>").title()

                street_address = input("\nWhat is the Street Address of this customer?"
                                       "\n>>>").title()

                zip_code = input("\nWhat Zip Code is that?"
                                 "\n>>>")
                # Zip codes are 5 digits long, so I put a try statement to check if the user put 5 numbers
                while zip_code != "A Long And Random String Of Text":
                    try:
                        if len(zip_code) == 5:  # This checks the length. I found out that len() can't count integers
                            zip_code = int(zip_code)
                            break
                        else:
                            int("# Forces this try statement to fail if the value doesn't contain a proper zip code")
                    except ValueError:
                        zip_code = input("Enter a valid Zip Code please"
                                         "\n>>>")

                city = input("\nWhat City does this customer live in?"
                             "\n>>>").title()

                state = input("\nAnd the State? (2 letter abbreviation is fine)"
                              "\n>>>").title()

                # This variable contains the string to add this new person using the variables
                add_person = f"""
                INSERT INTO
                  customer (first_name, last_name, street_address, zip_code, city, state)
                VALUES
                ('{first_name}', '{last_name}', '{street_address}', '{zip_code}', '{city}', '{state}')"""

                create_table(connecting, add_person)

            # This section allows the user to modify information in the person table excluding the ID. That could be bad
            elif choice == 2:
                menu = "ONWARD"
                category = input("\nAlright, which category of the customer would you like to modify? (The Customer ID will remain unchanged)" +
                                 "\n*type the number next to the desired choice*".upper() +
                                 "\n1. First Name"
                                 "\n2. Last Name"
                                 "\n3. Street Address"
                                 "\n4. Zip Code"
                                 "\n5. City"
                                 "\n6. State"
                                 "\n>>>")
                # Checks if the user entered a valid choice
                while category != "A Long And Random String Of Text":
                    try:
                        category = int(category)
                        if 7 > choice > 0:
                            break
                        else:
                            int("# Forces this try statement to fail if the choice isn't 1, 2, 3, 4, 5, or 6")
                    except ValueError:
                        category = input("Enter 1, 2, 3, 4, 5, or 6"
                                         "\n>>>")
                if category == 1:
                    category = "first_name"
                elif category == 2:
                    category = "last_name"
                elif category == 3:
                    category = "street_address"
                elif category == 4:
                    category = "zip_code"
                elif category == 5:
                    category = "city"
                elif category == 6:
                    category = "state"

                cat = category.replace("_", " ").title()  # cat was supposed to be short for category.
                                                          # I did this so i could maintain the data in category, while also interacting with the user
                                                          # It just replaces the underscores with spaces, then keeps the title case trend

                # asks for the current value
                value = input(f"What does the current {cat}?"
                              f"\n>>>").title()

                # A zip code contains 5 digits. This it the only category I can check here
                if category == "zip_code":
                    while category != "A Long And Random String Of Text":
                        try:
                            if len(value) == 5:
                                value = int(value)
                                break
                            else:
                                int("# Forces this try statement to fail if the value doesn't contain a proper zip code")
                        except ValueError:
                            value = input("Enter a valid Zip Code please"
                                          "\n>>>")

                # Asks for the new value
                new_val = input(f"What do you want to change {cat} to?"
                                f"\n>>>").title()

                # Same deal as before
                if category == "zip_code":
                    while category != "A Long And Random String Of Text":
                        try:
                            if len(value) == 5:
                                value = int(value)
                                break
                            else:
                                int("# Forces this try statement to fail if the value doesn't contain a proper zip code")
                        except ValueError:
                            value = input("Enter a valid Zip Code please"
                                          "\n>>>")

                # Asks for the Customer ID because without it, it would modify everyone's value
                # The ID also can't change
                value1 = input("\nWhat is the Customer ID of the customer you wish to modify?"
                               "\n>>>")
                # Checks if the user entered an integer with another try statement
                while value1 != "Random Words":
                    try:
                        int(value1)  # but i didn't want to make it an integer because i would have to typecast the variable
                        break
                    except ValueError:
                        value1 = input("\nEnter the ID of the Customer you wish to delete"
                                       "\n>>>")

                # This variable holds the query to update a person using the variables
                update_person = f"""
                UPDATE
                  customer
                SET
                  {category} = '{new_val}'
                WHERE
                  {category} = '{value}' AND customer_id = {value1}
                """
                create_table(connecting, update_person)

            elif choice == 3:
                value = input("\nWhat is the Customer ID of the person you want to remove?"
                              "\n>>>")
                # I wanted to check if the user actually entered an integer so i used another try statement
                while value != "Random Words":
                    try:
                        int(value)  # but i didn't want to make it an integer because i would have to typecast the variable
                        break
                    except ValueError:
                        value = input("\nEnter the ID of the Customer you wish to delete"
                                      "\n>>>")
                # I also asked for the customers last name, sort of as a fail safe
                value1 = input("\nAlright, what is the Last Name of that customer?"
                               "\n>>>\n").title()
                delete_person = f"""
                DELETE FROM 
                  customer
                WHERE
                  customer_id = '{value}' AND last_name = '{value1}'
                """

                create_table(connecting, delete_person)
                print("\nMenu time")

            # This simple prints the list of people in the database
            elif choice == 4:
                every_one = "SELECT * FROM customer"
                people = read_table(connecting, every_one)

                for peeps in people:
                    print(f'\nCUSTOMER ID: {peeps[0]} | FIRST NAME: {peeps[1]} | LAST NAME: {peeps[2]} | ADDRESS: {peeps[3]}'
                          f' | ZIP CODE: {peeps[4]} | CITY: {peeps[5]} | STATE: {peeps[6]}')

            print("\nAlright, I'm taking you back you the menu")

    # This section of the program is for the book menu
    elif choice == 2:
        menu = "ONWARD"
        while menu != 'END':
            partition()
            input("\npress enter".upper())
            # Allows the user to choose what they want to do
            choice = input("\nWhat would you like to do?"
                           "\n1. ADD new book"
                           "\n2. MODIFY a book"
                           "\n3. DELETE a book"
                           "\n4. Print the books table"
                           "\n5. Leave this menu"
                           "\n>>>")
            # Checks to see if the user enter a valid value
            while choice != "A Long And Random String Of Text":
                try:
                    choice = int(choice)
                    if 6 > choice > 0:
                        break
                    else:
                        int("# Forces this try statement to fail if the choice isn't 1, 2, 3, 4, or 5")
                except ValueError:
                    choice = input("Enter 1, 2, 3, 4, or 5"
                                   "\n>>>")

            if choice == 5:
                print("Back to the main menu it is.")
                break

            elif choice == 1:
                title = input("\nWhat is the Book Title?"
                              "\n>>>").title()  # Finally, the .title() is where it belongs

                author = input("\nWho is the Author of the book?"
                               "\n>>>").title()

                isbn = input("\nWhat is the ISBN of the book? (dashes(-) are included)"
                             "\n>>>")
                # The isbn contains - in between some of the numbers, so i will replace them with "" to check it using another variable,
                while isbn != "How did this code get so long":
                    try:
                        checking = isbn.replace("-", "")
                        int(checking)
                        break
                    except ValueError:
                        isbn = input("\nPlease enter a valid ISBN"
                                     "\n>>>")

                edition = input("\nWhat Edition is the book? (Only numbers: 4th = 4) "
                                "\n>>>")
                # Checks if the user entered a digit
                while edition != "Take a guess for how long this will get":
                    try:
                        edition = int(edition)
                        break
                    except ValueError:
                        edition = input("\nPlease enter the number of the Edition. No text"
                                        "\n>>>")

                price = input("\nWhat is the Price of the book? (dollar signs($) and dots(.) are included)"
                              "\nIf the cost is $12, put $12.00"
                              "\n>>>")
                # Uses the same method as the ISBN variable
                while price != "Late night coding":
                    try:
                        cost = price.replace("$",'').replace(".", '')
                        int(cost)
                        try:
                            if price[-3] == ".":
                                if price[0] != "$":
                                    price = "$" + price
                                break
                            else:
                                int("#Force fail")
                        except IndexError:
                            print("\nYou did not enter 2 numbers after a decimal.")
                            int('#Force fail')
                    except ValueError:
                        price = input("\nEnter the Price of the book. (For example: $12.70)"
                                      "\n>>>")

                publisher = input("\nAnd the Publisher is?"
                                  "\n>>>").title()

                # This variable contains the string to add this new person using the variables
                add_book = f"""
                INSERT INTO
                  book (title, author, isbn, edition, price, publisher)
                VALUES
                ('{title}', '{author}', '{isbn}', '{edition}', '{price}', '{publisher}')"""

                create_table(connecting, add_book)

            elif choice == 2:
                partition()
                category = input("\nAlright, which category of the book would you like to modify? (The Book ID and ISBN will remain unchanged)" +
                                 "\n*type the number next to the desired choice*".upper() +
                                 "\n1. Title"
                                 "\n2. Author"
                                 "\n3. Edition"
                                 "\n4. Price"
                                 "\n5. Publisher"
                                 "\n>>>")
                # Checks if the user entered a valid choice
                while category != "Oof":
                    try:
                        category = int(category)
                        if 6 > category > 0:
                            break
                        else:
                            int("# Forces this try statement to fail if the choice isn't 1, 2, 3, 4, 5, or 6")
                    except ValueError:
                        category = input("Enter 1, 2, 3, 4, 5, or 6"
                                         "\n>>>")

                if category == 1:
                    category = "title"
                elif category == 2:
                    category = "author"
                elif category == 3:
                    category = "edition"
                elif category == 4:
                    category = "price"
                elif category == 5:
                    category = "publisher"

                # This variable will contain the information I need to change the data. This has the old data
                value = input(f"What does the current value for the {category.title()} say?"
                              f"\n>>>").title()

                if category == "edition":
                    # Checks if the user entered a digit
                    while value != "Blah":
                        try:
                            value1 = int(value)
                            break
                        except ValueError:
                            value = input("\nPlease enter the number of the current Edition. No text"
                                          "\n>>>")

                if category == 'price':
                    # Uses the same method as the ISBN variable
                    while value != "Brain loading":
                        try:
                            cost = value.replace("$",'').replace(".", '')
                            int(cost)
                            try:
                                if value[-3] == ".":
                                    if value[0] != "$":
                                        value = "$" + value
                                    break
                                else:
                                    int("#Force fail")
                            except IndexError:
                                print("\nYou did not enter 2 numbers after a decimal.")
                                int('#Force fail')
                        except ValueError:
                            value = input("\nEnter the Price of the book. (For example: $12.50)"
                                          "\n>>>")

                # This variable will hold the new data
                value1 = input(f"What is the {category} you want to change it to?"
                               f"\n>>>").title()

                if category == "edition":
                    # Checks if the user entered a digit
                    while value1 != "Blah Blah":
                        try:
                            value1 = int(value1)
                            break
                        except ValueError:
                            value1 = input("\nPlease enter the number of the Edition. No text"
                                           "\n>>>")

                if category == 'price':
                    # Uses the same method as the ISBN variable
                    while value1 != "Brain still loading":
                        try:
                            cost = value1.replace("$",'').replace(".", '')
                            int(cost)
                            try:
                                if value1[-3] == ".":
                                    if value1[0] != "$":
                                        value1 = "$" + value1
                                    break
                                else:
                                    int("#Force fail")
                            except IndexError:
                                print("\nYou did not enter 2 numbers after a decimal.")
                                int('#Force fail')
                        except ValueError:
                            value1 = input("\nEnter the Price of the book. (For example: $12.75)"
                                           "\n>>>")

                value2 = input("\nAlright, what is the ISBN of that book?"
                               "\n>>>")
                # Still the same ISBN checks as before
                while value2 != "Next day":
                    try:
                        checking = value2.replace("-", "")
                        int(checking)
                        break
                    except ValueError:
                        value2 = input("\nPlease enter a valid ISBN"
                                       "\n>>>")

                # This variable holds the string to modify book information
                update_book = f"""
                UPDATE
                  book
                SET
                  {category} = '{value1}'
                WHERE
                  {category} = '{value}' AND isbn = '{value2}'
                """
                create_table(connecting, update_book)
                print("\nOkay, now back to the menu.")

            # This section allows the user to delete a book from the table
            elif choice == 3:
                value = input("\nWhat is the Book ID of the book you want to remove?"
                              "\n>>>")
                # I wanted to check if the user entered an integer so i used another try statement
                while value != "Randoms":
                    try:
                        int(value)  # but i didn't want to save it as an integer
                        break
                    except ValueError:
                        value = input("\nEnter the ID of the Book you wish to delete"
                                      "\n>>>")

                # I also asked for the isbn, as a back up
                value1 = input("\nAlright, what is the ISBN of that book?"
                               "\n>>>")
                # Still the same ISBN checks as before
                while value1 != "I'm starting to get tired now":
                    try:
                        checking = value1.replace("-", "")
                        int(checking)
                        break
                    except ValueError:
                        value1 = input("\nPlease enter a valid ISBN"
                                       "\n>>>")

                delete_book = f"""
                DELETE FROM 
                  book
                WHERE
                  book_id = '{value}' AND isbn = '{value1}'
                """

                create_table(connecting, delete_book)

            elif choice == 4:
                all_books = "SELECT * FROM book"
                books = read_table(connecting, all_books)

                for book in books:
                    print(f'\nBOOK ID: {book[0]} | TITLE: {book[1]} | AUTHOR: {book[2]}'
                          f' | ISBN: {book[3]} | EDITION: {book[4]} | PRICE: {book[5]} | PUBLISHER: {book[6]}')

            print("\nI'm taking you back you the menu.")

    elif choice == 3:
        menu = "ONWARD"
        while menu != "END":
            partition()
            menu = input("\nWhat do you want to do?"
                         "\n1. Order book(s)"
                         "\n2. Print Orders"
                         "\n3. Print Order Line Items"
                         "\n4. Delete an Order"
                         "\n5. Leave this menu"
                         "\n>>>")
            while menu != "END":
                try:
                    menu = int(menu)
                    if 6 > menu > 0:
                        break
                    else:
                        int("#Fails on purpose")
                except ValueError:
                    menu = input("\nPlease enter 1, 2, 3, 4, or 5"
                                 "\n>>>")

            if menu == 1:
                iN = input("\nAre you a customer in this database? (Y or N)"
                           "\n>>>").title()
                if iN == "Y":
                    print("Let us proceed then")
                else:
                    print("\nI will take you the previous menu."
                          "\nFrom there go to the Customer Menu"
                          "\nYou can be entered there")
                    break

                first_name = input("\nWhat is your First Name?"
                                   "\n>>>").title()
                last_name = input("\nWhat is your Last Name?"
                                  "\n>>>").title()
                customer_id = f"""
                SELECT 
                  customer_id
                FROM
                  customer           
                WHERE
                  first_name = '{first_name}' AND last_name = '{last_name}'
                """
                try:
                    customer_id = read_table(connecting, customer_id)
                    customer_id = int(f'{customer_id[0]}'.replace(',', '').replace('(', '').replace(')', '').replace("'", ''))
                except IndexError:
                    print("\nIt seems you are not in the database."
                          "\nPlease enter ADD yourself from the Customer Menu"
                          "\nIf you are sure you are, check for unwanted spacing, or accidental spacing in the database"
                          "\nIf the latter occurs you can always MODIFY your Name in our system")
                    break

                order_number_placeholder = 0
                order_num = 0
                multiple_orders = 0
                order_total_placeholder = 0
                date_placeholder = 0
                while menu != "STOP":
                    while menu != "END":
                        print("\nHere is the list of all books in the database:")
                        book = "SELECT * FROM book"
                        all_books = read_table(connecting, book)
                        for books in all_books:
                            print(f'\nBOOK ID: {books[0]} | TITLE: {books[1]} | AUTHOR: {books[2]}'
                                  f' | ISBN: {books[3]} | EDITION: {books[4]} | PRICE: {books[5]} | PUBLISHER: {books[6]}')

                        book_id = input("\nWhat is the Book ID of the book you want to buy?"
                                        "\n>>>")
                        while book_id != int:
                            try:
                                book_id = int(book_id)
                                break
                            except ValueError:
                                book_id = input("\nWhat is the Book ID of the book??"
                                                "\n>>>")
                        checking = 0
                        if multiple_orders > 0:
                            print("\nAllow me to do a quick check...")
                            checking = f"""
                            SELECT book_id
                            FROM order_line_item
                            WHERE book_id = {book_id} AND order_number = {order_number_placeholder}
                            """
                            check = read_table(connecting, checking)
                            for checks in check:
                                checks = int(f"{checks}".replace(',', '').replace('(', '').replace(')', '').replace("'", ''))
                                if book_id == checks:
                                    print("\nYou can't order this book again in this order."
                                          "\nI will take you to the menu to place new order"
                                          "\nYou can get this book again there.")
                                    checking = 1
                                    break
                            if checking == 1:
                                menu = "STOP"
                                break

                            print("Alright, good to go")

                        price = f"""
                        SELECT
                          price
                        FROM
                          book
                        WHERE
                          book_id = {book_id}
                        """
                        try:
                            price = read_table(connecting, price)
                            price = int(f'{price[0]}'.replace(',', '').replace('(', '').replace(')', '').replace('$', '').replace(".", "").replace("'", ''))

                        except IndexError:
                            print("\nThat is not a Book ID in this database"
                                  "\n____")
                            break

                        quantity = input("\nHow many do you want to purchase?"
                                         "\n>>>")
                        while quantity != int:
                            try:
                                quantity = int(quantity)
                                break
                            except ValueError:
                                quantity = input("\nHow many would you like to purchase?"
                                                 "\n>>>")

                        order_total = 0
                        if multiple_orders > 0:
                            order_total = f"${str(order_total_placeholder + ((quantity * price) / 100))}"
                            order_total_placeholder += (quantity * price) / 100
                            try:
                                if order_total[-2] == ".":
                                    order_total = order_total + '0'
                                if order_total[-3] != '.':
                                    order_total = order_total + ".00"
                            finally:
                                print("Your total is", order_total)
                            update_order_total = f"""
                            UPDATE
                              ordering
                            SET
                              order_total = '{order_total}'
                            WHERE
                              order_number == {order_number_placeholder}
                            """
                            create_table(connecting, update_order_total)
                        else:
                            order_total = f"${str((quantity * price) / 100)}"
                            order_total_placeholder = (quantity * price) / 100
                            try:
                                if order_total[-2] == ".":
                                    order_total = order_total + '0'
                                if order_total[-3] != '.':
                                    order_total = order_total + ".00"
                            finally:
                                print("Your total is", order_total)

                        date_time = 0
                        if multiple_orders == 0:
                            date_time = datetime.now().strftime('%x at %H:%M')
                            date_placeholder = date_time
                        else:
                            date_time = date_placeholder

                        if multiple_orders == 0:
                            add_order = f"""
                            INSERT INTO
                              ordering (order_date, order_total, customer_id)
                            VALUES
                              ('{date_time}', '{order_total}', '{customer_id}')
                            """
                            try:
                                create_table(connecting, add_order)
                            except ValueError:
                                print("Something went wrong :(")
                                break

                        if multiple_orders == 0:
                            order_number = f"""
                            SELECT
                              order_number
                            FROM
                              ordering
                            WHERE
                              order_date = '{date_time}' AND customer_id = {customer_id}
                            """
                            order_num = read_table(connecting, order_number)
                            order_num = int(f'{order_num[0]}'.replace(',', '').replace('(', '').replace(')', '').replace("'", ''))
                            order_number_placeholder = order_num

                        else:
                            order_num = order_number_placeholder

                        add_order_line_item = f"""
                        INSERT INTO
                          order_line_item (order_number, book_id, quantity)
                        VALUES
                          ('{order_num}', '{book_id}', '{quantity}')
                        """
                        create_table(connecting, add_order_line_item)

                        again = input("\nWould you like to place another order? (Y or N)"
                                      "\n>>>").title()

                        if again == "Y":
                            "\nAlright"
                            multiple_orders += 1
                        else:
                            print("Okay")
                            menu = "STOP"
                            break

            elif menu == 2:
                order = 'SELECT * FROM ordering'
                orders = read_table(connecting, order)
                for order in orders:
                    print(f'\nORDER NUMBER: {order[0]} | DATE OF ORDER: {order[1]}'
                          f' | ORDER TOTAL: {order[2]} | CUSTOMER ID: {order[3]}')

            elif menu == 3:
                oli = 'SELECT * FROM order_line_item ORDER BY order_number'
                oli_s = read_table(connecting, oli)
                for oli in oli_s:
                    print(f'\nORDER NUMBER: {oli[0]} | BOOK ID: {oli[1]} | QUANTITY: {oli[2]}')

            elif menu == 4:
                iN = input("\nAre you a customer in this database? (Y or N)"
                           "\n>>>").title()
                if iN == "Y":
                    print("Let us proceed then")
                else:
                    print("\nI will take you the previous menu."
                          "\nFrom there go to the Customer Menu"
                          "\nYou can be entered there")
                    break

                first_name = input("\nWhat is your First Name?"
                                   "\n>>>").title()
                last_name = input("\nWhat is your Last Name?"
                                  "\n>>>").title()
                customer_id = f"""
                SELECT 
                  customer_id
                FROM
                  customer           
                WHERE
                  first_name = '{first_name}' AND last_name = '{last_name}'
                """
                try:
                    customer_id = read_table(connecting, customer_id)
                    customer_id = int(f'{customer_id[0]}'.replace(',', '').replace('(', '').replace(')', '').replace("'", ''))
                except IndexError:
                    print("\nIt seems you are not in the database."
                          "\nPlease enter ADD yourself from the Customer Menu"
                          "\nIf you are sure you are, check for unwanted spacing, or accidental spacing in the database"
                          "\nIf the latter occurs you can always MODIFY your Name in our system")
                    break
                delete = input("\nWhat the the Order Number, of an order placed by you, that you wish to delete?"
                               "\n>>>")
                while delete != int:
                    try:
                        delete = int(delete)
                        break
                    except ValueError:
                        delete = input("\nWhat the the Order Number, of an order placed by you, that you wish to delete?"
                                       "\n>>>")

                print("Let me do a quick check...")
                delete_order = f"""
                DELETE FROM
                  ordering
                WHERE
                  order_number = {delete} AND customer_id = {customer_id}
                """
                if create_table(connecting, delete_order) is True:
                    create_table(connecting, delete_order)
                    delete_order_line_item = f"""
                    DELETE FROM
                      order_line_item
                    WHERE
                      order_number = {delete}
                    """
                    if create_table(connecting, delete_order_line_item) is True:
                        create_table(connecting, delete_order_line_item)
                        print("Everything was successful!")
                    else:
                        print("Something went wrong :(")
                else:
                    print("\nHmm. It doesn't look like an order with that Order Number and Customer ID was placed"
                          "\nPrint the Order table to check and try again")

            elif menu == 5:
                print('Alright')
                break

    elif choice == 4:
        print("Bye, hope you enjoyed")  # because this was work XD
        menu = "END"
