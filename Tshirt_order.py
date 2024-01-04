#NAME: NURUL IZZATY BINTI MAT NAZER
#ID STUDENT: 2022839016
#CLASS: KIM1443B
#PROGRAM TITTLE: T-SHIRT ORDER

import tkinter as tk
import mysql.connector


#Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tshirt_order"
)

#Create a cursor object to exercute SQL queries
mycursor = mydb.cursor()


#To enter the data 
def collect_data():
    #Funtion to calculate and database saving
    full_name = full_name_entry.get()
    phone_num = phone_num_entry.get()
    sleeve_type = sleeve_type_var.get()
    quantity = int(quantity_entry.get())
    size = size_var.get()
    

    #  the price below is to defined the value from your selections
    price = {
        "Short Sleeve": 45,
        "Long Sleeve": 50,
  
    }

    # Calculate the total price with discount provided. If user buy tshirt more than 5, user get discount 10%. 
    if quantity >= 5:
        total_price = (price[sleeve_type] * quantity * 90/100)

    else:
        total_price = (price[sleeve_type] * quantity)


    # To insert your Data to your database, As for this example, you have 3 attributes. (2 Attributes from your selection (Package, Pack) and another attributes that derived from your attributes (price))
    sql = "INSERT INTO user_order_details(Full_Name, Phone_Num, Sleeve_Type, Size, Quantity, Total_Price) VALUES (%s, %s,%s,%s,%s,%s)"
    val = (full_name, phone_num, sleeve_type, size, quantity, total_price)
    mycursor.execute(sql, val)
    mydb.commit()
    
    # To Print back The output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python. 
    output_label.config(text=f"Sleeve: {sleeve_type}, Quantity: {quantity}, Total Price: RM{total_price}")


root = tk.Tk()
root.title("Tshirt Order")

frame = tk.Frame(root)
frame.configure(bg='#ffd1dc')
frame.pack()


#Create a heading
orderheading = tk.Label(frame, text="T-SHIRT ORDER", font=('Algerian', 20), bg='#ffd1dc', fg='black')
orderheading.grid(row=0, column=0)

# User Detail Frame
customer_detail_frame =tk.LabelFrame(frame, text="Customer Details", font=('Britannic Bold',11), bg='#ffd1dc', fg='black')
customer_detail_frame.grid(row=1, column=0, padx=20, pady=10)

full_name_label = tk.Label(customer_detail_frame, text="Full Name", font=('Arial Nova', 10, 'bold'), bg='#ffd1dc', fg='black')
full_name_label.grid(row=0, column=0)
full_name_entry = tk.Entry(customer_detail_frame)
full_name_entry.grid(row=1, column=0)


matric_num_label = tk.Label(customer_detail_frame, text= "ID Student", font=('Arial Nova', 10, 'bold'), bg='#ffd1dc', fg='black')
matric_num_label.grid(row=2, column=0)
matric_num_entry = tk.Entry(customer_detail_frame)
matric_num_entry.grid(row=3, column=0)


email_label = tk.Label(customer_detail_frame, text="Email", font=('Arial Nova', 10, 'bold'), bg='#ffd1dc', fg='black')
email_label.grid(row=0, column=1)
email_entry = tk.Entry(customer_detail_frame)
email_entry.grid(row=1, column=1)


phone_num_label = tk.Label(customer_detail_frame, text="Phone Number", font=('Arial Nova', 10, 'bold'), bg='#ffd1dc', fg='black')
phone_num_label.grid(row=2, column=1)
phone_num_entry = tk.Entry(customer_detail_frame)
phone_num_entry.grid(row=3, column=1)


for widget in customer_detail_frame.winfo_children():
    widget.grid_configure(padx=15, pady=5)


#Saving Order Detail
order_frame = tk.LabelFrame(frame, text="Order Details", font=('Britannic Bold',11), bg='#ffd1dc', fg='black')
order_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)


#Sleeve Type Dropdown (Label)
sleeve_type= tk.Label(order_frame, text="Choose Type of Sleeve", font=('Arial Nova', 9, 'bold'), bg='#ffd1dc', fg='black')
sleeve_type.grid(row=1, column=0)

#Sleeve Type Dropdown
sleeve_type_var = tk.StringVar()
sleeve_type_var.set("Sleeve Type")
sleeve_dropdown = tk.OptionMenu(order_frame, sleeve_type_var, "Short Sleeve", "Long Sleeve")
sleeve_dropdown.grid(row=1, column=1)

#Quantity
quantity_label = tk.Label(order_frame, text="Quantity", font=('Arial Nova', 9, 'bold'), bg='#ffd1dc', fg='black')
quantity_label.grid(row=2, column=0)
quantity_entry= tk.Entry(order_frame)
quantity_entry.grid(row=3, column=0)

#Size Dropdown (Label)
size_label = tk.Label(order_frame, text="Size", font=('Arial Nova', 9, 'bold'), bg='#ffd1dc', fg='black')
size_label.grid(row=2, column=1)

#Size Dropdown 
size_var = tk.StringVar()
size_var.set("Size")
size_dropdown = tk.OptionMenu(order_frame, size_var, "XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL", "5XL")
size_dropdown.grid(row=3, column=1)


for widget in order_frame.winfo_children():
    widget.grid_configure(padx=15, pady=5)

#Price
price_frame = tk.LabelFrame(frame, text="Price", font=('Britannic Bold',11), bg='#ffd1dc', fg='black')
price_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

#Output Label & Result
label = tk.Label(price_frame, text="Total Price", font=('Arial Nova', 9, 'bold'), bg='#ffd1dc', fg='black')
label.grid(row=2, column=0)
output_label = tk.Label(price_frame, text="" , bg='#ffd1dc', fg='black')
output_label.grid()

for widget in price_frame.winfo_children():
    widget.grid_configure(padx=15, pady=5)

#Button
submit_button = tk.Button(frame, text="Submit Order", font=('Britannic Bold',11), bg='#ffb7c3', fg='black', command=collect_data)
submit_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

root.mainloop ()