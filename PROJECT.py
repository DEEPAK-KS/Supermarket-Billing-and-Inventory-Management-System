import mysql.connector  
mysql=mysql.connector.connect(host="localhost",user="  root",password='de9900630a') mycursor=mysql.cursor()  mycursor.execute("use JJ_SUPER_MARCKET") def  add(sno):  
 product=(input("ENTER YOUR PRODUCT: "))  mycursor.execute("select price from STOCKS where  product ='{}' ".format(product)) 
price0=mycursor.fetchall() price0=price0[0]  price1=(1,) price3=price0+price1  
price=price3[0]  
 quantity=int(input("ENTER THE QUANTITY: "))  mycursor.execute("select available from STOCKS  where product ='{}' ".format(product))  
avai0=mycursor.fetchall() avai0=avai0[0]  avai1=(1,) avai3=avai0+avai1 avai=avai3[0]  while avai<quantity:  
 print("SORRY ONLY ",avai," is AVAILABLE")  quantity=int(input("ENTER THE QUANTITY: "))  new=avai-quantity  
 mycursor.execute("update stocks set available =  {} where product = '{}' ".format(new,product))  total=price*quantity  
 mycursor.execute("insert into customer  values({},'{}',{},{},{})  
".format(sno,product,price,quantity,total))  mysql.commit()  
import mysql.connector  
mysql=mysql.connector.connect(host="localhost",user="  root",password='de9900630a') mycursor=mysql.cursor()  mycursor.execute("use JJ_SUPER_MARCKET") def  deld():  
 product3=int(input("ENTER 1 TO REMOVE PRODUCT AND  2 TO CHANGE QUANTITY: "))  
if product3==2:  
 product=(input("ENTER YOUR PRODUCT: "))  quantity=int(input("ENTER THE QUANTITY: "))  mycursor.execute("select available from STOCKS  where product ='{}' ".format(product))  
avai0=mycursor.fetchall() avai0=avai0[0]  avai1=(1,) avai3=avai0+avai1  
avai=avai3[0] while avai<quantity:   print("SORRY ONLY ",avai," is AVAILABLE")  quantity=int(input("ENTER THE QUANTITY:  
"))  
 mycursor.execute("select quantity from  customer where product ='{}' ".format(product)) 
taken0=mycursor.fetchall()  
taken0=taken0[0] taken1=(1,)  
taken3=taken0+taken1 taken=taken3[0]  if taken>quantity: new=taken quantity new+=avai elif  quantity>taken: new=avai-quantity   mycursor.execute("update stocks set available  = {} where product = '{}' ".format(new,product))  #check above  
import mysql.connector from  
tabulate import tabulate  
import datetime  
mysql=mysql.connector.connect(host="localhost",user="root",pas  sword='de9900630a') mycursor=mysql.cursor()  
mycursor.execute("use JJ_SUPER_MARCKET") def  
bill (a,date):  
 now=datetime.datetime.today()  
print("DATE & TIME") print(now)   mycursor.execute("select * from customer order  by sno")  
 bill=mycursor.fetchall()  
  
h=["s/no","PRODUCT","PRICE","QUANTITY","TOTAL_PRICE"]  print(tabulate(bill, headers=h,tablefmt="psql"))   mycursor.execute("select sum(total_price) from  customer")  
 bill_amound0=mycursor.fetchall()  bill_amound0=bill_amound0[0] bill_amound1=(1,)   bill_amound3= bill_amound0+ bill_amound1  bill_amound= bill_amound3[0]  
 mycursor.execute("create table if not exists  customer_data (CUSTOMER_NAME varchar(30) not null primary key  ,FINAL_BILL int(3),DATE_OF_PURCHASE DATE)")  
 print("YOUR BILL AMOUND IS: ", bill_amound)  discount=(bill_amound/100)*15 print("SPECIAL  OFFER AND OTHER DISCOUNTS:  
",discount)  
 Fprice=bill_amound-discount  
 print(a,"YOUR FINAL PRICE IS :",int(Fprice))  mycursor.execute("insert into customer_data  
values('{}',{},'{}') ".format(a,Fprice,date))  
mysql.commit()  
 mycursor.execute("drop table customer") 
  
import mysql.connector from  
tabulate import tabulate  
mysql=mysql.connector.connect(host="localhost",user="root",pas  sword='de9900630a') mycursor=mysql.cursor()  
mycursor.execute("use JJ_SUPER_MARCKET") def  
stock():  
 mycursor.execute("select * from stocks")  
products=mycursor.fetchall()  
 h=["PRODUCT","PRICE","STOCKS AVAILABLE","EXP DATE"]  print(tabulate(products, headers=h,tablefmt="psql"))  a=int(input("ENTER 1 TO ADD NEW PRODUCTS OR 2 TO CHANGE  PRODUCT STOCK")) while a!=3: if a== 1:   product=input("ENTER THE PRODUCT NAME :" )  expdate=(input("ENTER THE EXP DATE IN YYYY/MM/DD FORMAT: "))  quantity=int(input("ENTER THE STOCK AVAILABLE :  "))  
 price=int(input("ENTER THE PRODUCT PRICE : "))  mycursor.execute("insert into stocks values('{}',{},{},'{}')  ".format(product,price,quantity,expdate))  
mysql.commit() elif a== 2:  
 product=(input("ENTER YOUR PRODUCT: "))  quantity=int(input("ENTER THE STOCKS AVAILABLE:  "))  
 mycursor.execute("select available from STOCKS  where product ='{}' ".format(product))  
avai0=mycursor.fetchall() avai0=avai0[0]  avai1=(1,) avai3=avai0+avai1  
avai=avai3[0] quantity+=avai  
 price=int(input("ENTER THE PRODUCT PRICE : "))  mycursor.execute("update stocks set available = {}  , price = {} ,EXP_DATE = '{}' where product = '{}'  ".format(quantity,price,expdate,product))  
mysql.commit() else:  
 print("PLEASE CHECK YOUR INPUT")  
print("ENTER 3 TO RETURN TO MAIN PAGE")  
a=int(input("ENTER 1 TO ADD NEW PRODUCTS OR 2 TO  CHANGE PRODUCT STOCK"))  
return()  
print("  
WELCOME TO JJ SUPER MARCKET 
")  
date=(input("ENTER TODAYS DATE IN YYYY/MM/DD FORMAT: "))  import mysql.connector import add import bill import  deld import stocks  
from tabulate import tabulate  
password=str(input("ENTER THE DATABASE PASSWORD"))  mysql=mysql.connector.connect(host="localhost",user="root",pas  sword=password) mycursor=mysql.cursor()  
mycursor.execute("create database if not exists  JJ_SUPER_MARCKET")  
mycursor.execute("use JJ_SUPER_MARCKET")  
# START HERE sno=0  
print("1.STOCKS")  
print("2.BILLING")  
print("3.EXIT")  
option=int(input("ENTER YOUR CHOICE: "))  
while option != 3: if option==1:  
 stocks.stock()  
print("1.STOCKS")  
print("2.BILLING")  
print("3.EXIT")  
 option=int(input("ENTER YOUR CHOICE: "))  elif option ==2:  
 customer=input("customer name")  
 mycursor.execute("create table if not exists customer  (sno int(2) ,PRODUCT varchar(30) not null primary key,PRICE  int(3),QUANTITY INT(2),TOTAL_PRICE INT(30))")  
mycursor.execute("select * from STOCKS")  
products=mycursor.fetchall()  
 h=["PRODUCT","PRICE","STOCK AVAILABLE","EXP DATE"]  print(tabulate(products, headers=h,tablefmt="psql"))  print("1.ADD PRODUCTS") print("2.REMOVE PRODUCTS")  print("3.CHECKOUT")  
 option2=int(input("ENTER YOUR CHOICE: "))  while option2 != 3: if option2 ==1:  sno+=1 add.add(sno)  
 elif option2 ==2:  
deld.deld() print("1.ADD  
PRODUCTS") print("2.REMOVE  
PRODUCTS")  
print("3.CHECKOUT")  
 option2=int(input("ENTER YOUR OPTION: "))  if option2==3:  
 bill.bill(customer,date)  
 print("  
THANKS FOR SHOPING  
")  
 option=3 print(" 
***************************************VISIT  AGAIN******************************************  ") 
