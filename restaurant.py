import mysql.connector
mydb=mysql.connector.connect(user='root',password='12345678',host='Localhost',database='restaurant',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
def main_menu():
    while True:
        print(" Hotel xyz")
        print("")
        print("1. Enter 1 IF you are ADMIN")
        print(" ")
        print("2. Enter 2 IF you are Customer")
        print(" ")
        print("3. Exit")
        print(" ")
        choice=int(input("Enter Your Choice"))
        if choice == 1:
            import mysql.connector

            mydb = mysql.connector.connect(user='root', password='12345678', host='localhost', database='restaurant')
            mycursor = mydb.cursor()

            while True:
                try:
                    mycursor.execute('CREATE TABLE IF NOT EXISTS ADMIN(adm_name CHAR(30), pssword CHAR(25))')
                    print("Table created successfully.")
                except mysql.connector.Error as err:
                    print("Failed creating table: {}".format(err))

                try:
                    m = "INSERT INTO ADMIN VALUES ('Admin', '2918')"
                    mycursor.execute(m)
                    mydb.commit()
                    print("Data inserted successfully.")
                except mysql.connector.Error as err:
                    print("Failed inserting data: {}".format(err))

                adm_name = input("Enter Your Name: ")
                pssword = input("Enter Password: ")

                a = 'SELECT * FROM ADMIN'
                mycursor.execute(a)
                m = mycursor.fetchall()

                for row in m:
                    if adm_name == row[0] and pssword == row[1]:
                        print("Welcome", adm_name)
                        break
                    else:
                        print("Wrong User Id / Password entered")

                while True:
                    print(" ")
                    print("To see customer details enter :1")
                    print(" ")
                    print("to see staff details enter :2 ")
                    print("")
                    print("Main Menu :3")
                    c2=int(input("Enter your choice "))
                    if c2==1:
                        mycursor=mydb.cursor()
                        mycursor.execute('select * from customer_details')
                        m=mycursor.fetchall()
                        count=mycursor.rowcount
                        print("No. of customers are ",count)
                        for row in m:
                            print(row)
                    if c2==2:
                        mycursor=mydb.cursor()
                        mycursor.execute('select * from Staff')
                        m=mycursor.fetchall()
                        print("Name ID no.")
                        for row in m:
                            print(row)
                    if c2==3:
                        main_menu()
                    if choice==3:
                        break
        if choice == 2:
            import mysql.connector

            mydb = mysql.connector.connect(user='root', password='12345678', host='localhost', database='restaurant')
            mycursor = mydb.cursor()

            while True:
                print(" xyz veg restaurant ")
                print(" ")
                print("1. Create your account ")
                print(" ")
                print("2. LOG in to your existing account")
                print(" ")
                print("3. Exit")
                print(" ")
                c3 = int(input("Enter Your Choice: "))

                if c3 == 1:
                    cust_name = input("Enter Your Name: ")
                    cust_id = int(input("Enter Your Customer ID in less than 10 digits: "))
                    E_mail_add = input("Enter your address: ")
            
                    while True:
                        password = input("Enter your password: ")
                        password2 = input("Enter your password again for confirmation: ")

                        if password == password2:
                            print("Successfully saved your password")

                            try:
                                mycursor.execute('CREATE TABLE IF NOT EXISTS customer_details (cust_name CHAR(30), cust_id INT NOT NULL PRIMARY KEY, email_add VARCHAR(30), password VARCHAR(25))')
                            except mysql.connector.Error as err:
                                print("Failed creating table: {}".format(err))
                    
                            n = "INSERT INTO customer_details VALUES (%s, %s, %s, %s)"
                            val = (cust_name, cust_id, E_mail_add, password)

                            try:
                                mycursor.execute(n, val)
                                mydb.commit()
                                print("ID Created")
                            except mysql.connector.Error as err:
                                print("Failed inserting data: {}".format(err))

                            break
                        else:
                            print("Wrong password entered. Try again!")


                if c3==3:
                    break
                if c3==2:
                    import mysql.connector
                    mydb=mysql.connector.connect(user='root',password='12345678',host='Localhost',database='restaurant')
                    print("To login enter the details")
                    print(" ")
                    print(" ")
                    v_cust_name=input("Enter your name")
                    v_cust_id=int(input("Enter you ID"))
                    v_password=input("Enter your password")
                    mycursor=mydb.cursor()
                    a='select * from customer_details'
                    mycursor.execute(a)
                    data=mycursor.fetchall()
                    u=mycursor.rowcount
                    for row in data:
                        if v_cust_name and v_cust_id in row:
                            print("Welcome", v_cust_name)
                        while True:
                            print("")
                            print("")
                            print("To see your details enter :1")
                            print("")
                            print("To update your details enter :2 ")
                            print(" ")
                            print("To delete your details enter 3: ")
                            print(" ")
                            print("To see the menu card enter 4: ")
                            print(" ")
                            print(" main menu enter 5:")
                            c4=int(input("Enter your choice"))
                            if c4==1:
                                cust_id=int(input("Enter your customer id"))
                                show='select * from customer_details where cust_id=%s'
                                mycursor.execute(show,(cust_id,))
                                for x in mycursor:
                                    print(x)
                            if c4==2:
                                cust_id=int(input("Enter your customer id"))
                                show='select * from customer_details where cust_id=%s'
                                mycursor.execute(show,(cust_id,))
                                print("Your details are:")
                                for x in mycursor:
                                    print(x)
                                while True:
                                    print("1:customer name ")
                                    print("2:Email address")
                                    print("3:password")
                                    print("4:Exit")
                                    ch=int(input("Enter a choice to update:"))
                                    if ch==1:
                                        cust_name=input("Enter your name to update")
                                        sin="update customer_details set cust_name=%s where cust_id=%s"
                                        mycursor.execute(sin,(cust_name,cust_id))
                                        mydb.commit()
                                        print("Updated data is:")
                                        show="select * from customer_details where cust_id=%s"
                                        mycursor.execute(show,(cust_id,))
                                        for x in mycursor:
                                            print(x)
                                    if ch==2:
                                        email_add=input("Enter your E_mail add")
                                        sin="update customer_details set email_add=%s where cust_id=%s"
                                        mycursor.execute(sin,(email_add,cust_id))
                                        mydb.commit()
                                        print("Updated data is:")
                                        show="select * from customer_details where cust_id=%s"
                                        mycursor.execute(show,(cust_id,))
                                        for x in mycursor:
                                            print(x)
                                    if ch==3:
                                        password=input("Enter your password")
                                        sin="update customer_details set password=%s where cust_id=%s"
                                        mycursor.execute(sin,(password,cust_id))
                                        mydb.commit()
                                        print("Updated data is:")
                                        show="select * from customer_details where cust_id=%s"
                                        mycursor.execute(show,(cust_id,))
                                        for x in mycursor:
                                            print(x)
                                    if ch==4:
                                         break
                            if c4==3:
                                cust_id=int(input("Enter your customer ID no."))
                                ans=input("ARE YOUSURE YOU WANT TO DEL YOUR DETAILS? y/n")
                                if ans=='y' or ans=='Y':
                                    six="delete from customer_details where cust_id=%s"
                                    mycursor.execute(six,(cust_id,))
                                    mydb.commit()
                                    print("DONE")
                                else:
                                    print("data has not been deleted")
                            
                            elif c4 == 4:
                                try:
                                    mycursor.execute('create table menu_card(Item_no int not null primary key , Name char(30) not null, Price float not null)')
                                    sin = "insert into menu_card(Item_no, Name, Price) values (%s, %s ,%s)"
                                    val = [(1, 'Regular Tea', 20.00),
                                   (2, 'Masala Tea', 25.00),
                                   (3, 'Coffee', 25.00),
                                   (4, 'Cold Drink', 25.00),
                                   (5, 'Bread Butter', 30.00),
                                   (6, 'Bread Jam', 30.00),
                                   (7, 'Veg. Sandwich', 50.00),
                                   (8, 'Veg. Toast Sandwich', 50.00),
                                   (9, 'Cheese Toast Sandwich', 70.00),
                                   (10, 'Grilled Sandwich', 70.00),
                                   (11, 'Tomato Soup', 110.00),
                                   (12, 'Hot & Sour', 110.00),
                                   (13, 'Veg. Noodle Soup', 110.00),
                                   (14, 'Sweet Corn', 110.00),
                                   (15, 'Veg. Munchow', 110.00),
                                   (16, 'Shahi Paneer', 110.00),
                                   (17, 'Kadai Paneer', 110.00),
                                   (18, 'Handi Paneer', 120.00),
                                   (19, 'Palak Paneer', 120.00),
                                   (20, 'Chilli Paneer', 140.00),
                                   (21, 'Matar Mushroom', 140.00),
                                   (22, 'Mix Veg', 140.00),
                                   (23, 'Jeera Aloo', 140.00),
                                   (24, 'Malai Kofta', 140.00),
                                   (25, 'Aloo Matar', 140.00),
                                   (26, 'Dal Fry', 140.00),
                                   (27, 'Dal Makhani', 150.00),
                                   (28, 'Dal Tadka', 150.00),
                                   (29, 'Plain Roti', 15.00),
                                   (30, 'Butter Roti', 15.00),
                                   (31, 'Tandoori Roti', 20.00),
                                   (32, 'Butter Naan', 20.00),
                                   (33, 'Plain Rice', 90.00),
                                   (34, 'Jeera Rice', 90.00),
                                   (35, 'Veg Pulao', 110.00),
                                   (36, 'Peas Pulao', 110.00),
                                   (37, 'Plain Dosa', 100.00),
                                   (38, 'Onion Dosa', 110.00),
                                   (39, 'Masala Dosa', 130.00),
                                   (40, 'Paneer Dosa', 130.00),
                                   (41, 'Rice Idli', 130.00),
                                   (42, 'Sambhar Vada', 140.00),
                                   (43, 'Vanilla', 60.00),
                                   (44, 'Strawberry', 60.00),
                                   (45, 'Pineapple', 60.00),
                                   (46, 'Butter Scotch', 60.00)]
                                    mycursor.executemany(sin, val)
                                    mydb.commit()
                                except:
                                    pass
                                r = 0
                                mycursor.execute('select * from menu_card')
                                menu_items = mycursor.fetchall()

                                print("-------------------------------------------------------------------------")
                                print("Hotel XYZ")
                                print("-------------------------------------------------------------------------")
                                print("Menu Card")
                                print("-------------------------------------------------------------------------")
                                print("\nBEVERAGES\n")
                                for item in menu_items:
                                    print("{:2} {:<25} {:.2f}".format(item[0], item[1], item[2]))
                                print("\nPress 0 to go back")

                                while True:
                                    ch = int(input(" -> "))
                                    if ch == 0:
                                        print("-------------------------------------------------------------------------")
                                        print("Hotel XYZ")
                                        print("-------------------------------------------------------------------------")
                                        print("CASH MEMO")
                                        print("-------------------------------------------------------------------------")
                                        print("Total amount:", r)
                                        print("\n MODE OF PAYMENT")
                                        print("__________________________________")
                                        print(" 1- Credit/Debit Card")
                                        print(" 2- Paytm/PhonePe")
                                        print(" 3- Using UPI")
                                        print(" 4- Cash")
                                        x = int(input("-> "))
                                        print("\n Amount:", r)
                                        print("\n Pay For xyz")
                                        print(" (y/n)")
                                        ch = input("-> ")
                                        if ch.lower() == 'y':
                                            print(" --------------------------------")
                                            print(" xyz ")
                                            print(" --------------------------------")
                                            print(" 1,Merchant Classic Building")
                                            print(" Plot No.3, Sec:48A ")
                                            print(" Seawoods, Navi Mumbai ")
                                            print(" Ph:27705001,27705009 ")
                                            print(" Mob:8657240260 ")
                                            print("-------------CASH MEMO-----------")
                                            from datetime import date, datetime
                                            today = date.today()
                                            now = datetime.now()
                                            current_time = now.strftime("%H:%M:%S")
                                            import random
                                            n = random.randint(0, 21)
                                            print("Date:", today, "Time:", current_time)
                                            print("Table No.", n, "Payment code:", x)
                                            print("---------------------------------")
                                            SGST = 0.025 * r
                                            CGST = 0.025 * r
                                            total = r + SGST + CGST
                                            print("Item no. Particulars Rate")
                                            print("-------------------------------")
                                            print("\n Sub total:", r, "/-")
                                            print("\n SGST @2.5%:", SGST, "/- ")
                                            print("\n CGST @2.5%:", CGST, "/- ")
                                            print("------------------------------------")
                                            print("\n Total:", total, "/-")
                                            print("------------------------------------")
                                            print(" Thank You")
                                            print(" Visit Again :)")
                                            print(" -----------------------------------")
                                            break
                                    elif ch in range(1, 47):
                                        sql = 'select * from menu_card where Item_no=%s'
                                        mycursor.execute(sql, (ch,))
                                        item = mycursor.fetchone()
                                        if item:
                                            print("Item: {}, Price: {}".format(item[1], item[2]))
                                            r += item[2]

                            elif c4 == 5:
                                break
main_menu()
