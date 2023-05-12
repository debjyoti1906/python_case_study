import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rps@12345",database="debjyoti_ericsson")

mycursor=mydb.cursor()

#mycursor.execute("create table product_management(productid  int,productname varchar(15),productprice int,productcatagory varchar(15))");
#print("Table Created")

#Update value into table

#mycursor.execute("insert into product_management values(10,'iphone14',100000,'mobile')");
#mycursor.execute("insert into product_management values(11,'samsungm31',15000,'mobile')");
#mycursor.execute("insert into product_management values(12,'motoG51',18000,'mobile')");
#mycursor.execute("insert into product_management values(31,'waxpol',500,'bike_car')");
#mycursor.execute("insert into product_management values(32,'wd40',150,'bike_car')");
#mycursor.execute("insert into product_management values(41,'macbook',100000,'computer_acc')");
#mycursor.execute("insert into product_management values(42,'cromebook',100003,'computer_acc')");
#mycursor.execute("insert into product_management values(43,'HPmouse',500,'computer_acc')");
#mycursor.execute("insert into product_management values(55,'sanku',350,'book')");
#mycursor.execute("insert into product_management values(56,'feluda',800,'book')");
#mydb.commit();

# update product:

#mycursor.execute("update product_management set productprice='850' where productid=56");
#mycursor.execute("update product_management set productprice='860' where productname='feluda'");
#mydb.commit();

# delete product

#mycursor.execute("delete from product_management where productid=12");
#mydb.commit();


# search product based on product id

#id=int(input('Please enter product id : ')) 
#mycursor.execute(f"SELECT * FROM product_management where productid={id}")
#myresult = mycursor.fetchone()
#print(myresult)


#search all product


#mycursor.execute("select * from product_management")
#data =mycursor.fetchall()
#print(data)
 
#for row in data:
#        print("Product Id:",row[0])
#        print("Product name:",row[1])
#        print("product price:",row[2])
#        print("product catagory:",row[3])

# select based on product productcatagory

#mycursor.execute("SELECT productcatagory from product_management")
#data =mycursor.fetchall()

#for row in data:
 #       print("Product catagory:",row)


# select based on product name

#mycursor.execute("SELECT productname from product_management")
#data =mycursor.fetchall()
#for row in data:
 #       print("Product name:",row)