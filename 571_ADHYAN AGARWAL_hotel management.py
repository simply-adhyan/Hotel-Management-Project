


import random 
    
name = [] 
phno = [] 
add = [] 
room = [] 
price = [] 
rc = [] 
p = []
g={};h=[]
roomno = [] 
custid = []
days=[]
i = 0
hm=[]

def database():
    a=0;l=[]  
    '''
                PLEASE CHANGE HOST NAME AND OTHERS AS PER YOUR mysql account
                                THANK YOU Ma'am.
    '''

    import mysql.connector as c
    conn = c.connect(host='localhost',
                     user='root',
                     password='mysql')

    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        l.append(x)


    for i in list(l):
        if "('hotel_management',)" == str(i):
            a+=1


    if a==0:       
        cursor.execute("CREATE DATABASE hotel_management")
        print('DATABASE CREATED')
        cursor.execute("use hotel_management")
        cursor.execute('''CREATE TABLE table1
                       (customer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50) NOT NULL,phone VARCHAR(15) NOT NULL ,Address varchar(50) NOT NULL,Room_type VARCHAR(15) NOT NULL,Price int  NOT NULL);''')

        print('TABLE CREATED')
    else:
        print()
        
        
def Home():

      
    print('''\t\t\t _____________________________________
             \t\t|     WELCOME TO HOTEL PACIFIC        |
             \t\t|                                     |
             \t\t|1 Booking                            |
             \t\t|2 Restaurent(Menu Card)              |
             \t\t|3 Payment                            |
             \t\t|4 Record                             |
             \t\t|5 Export to .txt file                |
             \t\t|0 Exit                               |
             \t\t|                                     |        
             \t\t|                                     |
             \t\t|                                     |
             \t\t|                                     |
             \t\t|_____________________________________|''')
   
    ch=int(input("\n\nInput-> ")) 
      
    if ch == 1: 
        print(" ") 
        Booking() 
      
    elif ch == 2: 
        print(" ") 
        restaurant()
      
    elif ch == 3: 
        print(" ") 
        Payment() 
      
    elif ch == 4: 
        print(" ") 
        Record() 
      
    elif ch == 5: 
        print(" ") 
        export() 
      
    elif ch== 0: 
        exit()

    
  
def Booking(): 
      
        global i 
        print(" BOOKING ROOMS") 
        print(" ") 
          
        while 1: 
            n = str(input("Name: ")) 
            phn = int(input("Phone No.: ")) 
            a = str(input("Address: "))
            c=phn
            aa=0
            while c:
                c=c//10
                aa+=1
            if n!="" and phn!="" and a!="" and aa==10: 
                name.append(n) 
                add.append(a) 
                break
                  
            else:
                if n=="" or phn=="" or  a=="":
                    print("\tName, Phone no. & Address are rquired and cannot be empty!!")
                elif aa!=10:
                    print("\tPhone no. must contain 10 digits..")
                else:
                    print("Error")
        d=1
        
        while d:

            print("----------------------------SELECT ROOM TYPE-----------------------------------") 
            print(" _____________________________________________________________________________ ")
            print("|                                                                             |")
            print("|                    ------ HOTEL ROOMS AMENITIES ------                      |")
            print("|                                                                             |") 
            print("| 1. TWIN                                                                     |") 
            print("|-----------------------------------------------------------------------------|") 
            print('| Room amenities include: 2 Single Bed, 40" Television,                       |')
            print("| Personal Highspeed Wi-Fi,Double-Door Cupboard, 1 Coffee table with 2 sofa,  |") 
            print("| Through-the-Wall AC.                                                        |")
            print("|                                                                             |")
            print("| 2. QUEEN                                                                    |") 
            print("|-----------------------------------------------------------------------------|") 
            print('| Room amenities include: 1 Queen Sized Bed,40" Television ,                  |') 
            print("| Personal Highspeed Wi-Fi, Double-Door Cupboard,                             |")
            print("| 1 Coffee table with 2 sofa,Balcony with an Accent table with 2 Chair        |") 
            print("| +Through-the-Wall AC.                                                       |")                                              
            print("|                                                                             |")
            print("| 3. TRIPLE                                                                   |")
            print("|-----------------------------------------------------------------------------|")
            
            print('| Room amenities include: 1 Double Bed + 1 Single Bed, 40" Television,        |') 
            print("| a Triple-Door Cupboard, 1 Coffee table with 2 sofa,Personal Highspeed       |") 
            print("| Wi-Fi,1 Work table, Balcony with an Accent table with 2 Chair + an          |") 
            print("| attached washroom with hot/cold water + Package Terminal AC.                |") 
            print("|                                                                             |")
            print("| 4. FAMILY                                                                   |") 
            print("|-----------------------------------------------------------------------------|") 
            print('| Room amenities include: 2 Double Bed , 40" Television,Personal              |') 
            print("| Highspeed Wi-Fi a Triple-Door Cupboard, 1 Coffee table with 2 sofa,         |") 
            print("| 1 Work table, Balcony with an Accent table                                  |") 
            print("| with 4 Chair and a Package Terminal AC                                      |") 
            print("|_____________________________________________________________________________|")
            print(("\n\t\t\tPress 0 for Room Prices"))   
            ch=input("->") 
            if ch=="0": 
                print("\t 1. TWIN   - Rs.  6500") 
                print("\t 2. QUEEN  - Rs.  7500") 
                print("\t 3. TRIPLE - Rs. 11500") 
                print("\t 4. FAMILY - Rs. 15000")
                
                ch=(input("->")) 
            if ch=="1": 
                room.append('TWIN') 
                print("Room Type- TWIN")   
                price.append(6500) 
                print("Price- 6500")
                d=0
            elif ch=="2": 
                room.append('QUEEN') 
                print("Room Type- QUEEN") 
                price.append(7500) 
                print("Price- 7500")
                d=0
            elif ch=="3": 
                room.append('TRIPLE') 
                print("Room Type- TRIPLE") 
                price.append(11500) 
                print("Price- 11500")
                d=0
            elif ch=="4": 
                room.append('FAMILY') 
                print("Room Type- FAMILY") 
                price.append(15000) 
                print("Price- 15000")
                d=0
                      
            else: 
                print(" Wrong choice..!!")
                

        print("Enter the no. of days you want to stay for -: ")
        z=int(input("--> "))
        days.append(z)


        
        rn = random.randrange(60)+600
        cid = random.randrange(60)+10
          
        while rn in roomno or cid in custid: 
            rn = random.randrange(99)+600
            cid = random.randrange(99)+10
              
        rc.append(0) 
        p.append(0) 
        if phn not in phno: 
            phno.append(phn) 
        elif phn in phno: 
            for n in range(0,i): 
                if phn== phno[n]: 
                    if p[n]==1: 
                        phno.append(phn) 
        elif phn in phno: 
            for n in range(0,i): 
                if phn== phno[n]: 
                    if p[n]==0: 
                        print("\tPhone no. already exists and payment yet not done..!!") 
                        name.pop(i) 
                        add.pop(i) 
                        Booking() 
        print("") 
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n") 
        print("\tRoom No. - ",rn) 
        print("\n\tCustomer Id - ",cid)
        print() 
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n") 
        
        roomno.append(rn) 
        custid.append(cid) 
        i=i+1
        if __name__ == '__main__':
            main()
            
        Home() 
        

# RESTAURANT FUNCTION  
def restaurant(): 
    ph=int(input("Customer Id: ")) 
    global i 
    f=0
    r=0
    for n in range(0,i): 
        if custid[n]==ph and p[n]==0: 
            f=1
            print("_____________________________________________________________________________") 
            print("                                                                             ")
            print("                              Hotel PACIFIC                                  ") 
            print("_____________________________________________________________________________") 
            print("                                Menu Card                                    ") 
            print("_____________________________________________________________________________") 
            print(" BEVARAGES                                                                   ") 
            print("__________________________________        34 Chana Masala............(150.00)")
            print(" 1  Regular Tea............. (20.00)      35 Panner Tikka............(150.00)") 
            print(" 2  Masala Tea.............. (35.00)      36 Dal Butter Fry..........(150.00)") 
            print(" 3  Coffee.................. (35.00)      37 Dal Makhani.............(150.00)") 
            print(" 4  Cold Drinks(all flavors) (35.00)                                         ")  
            print(" 5  Masala Cold Drinks...... (60.00)      ROTI'                              ")
            print('                                         ____________________________________')
            print('SANDWICHS                                 38 Plain Roti.............. (35.00)')
            print("__________________________________        39 Butter Roti............. (35.00)") 
            print(" 6  Bread Butter............ (60.00)      40 Tandoori Roti........... (20.00)") 
            print(" 7  Bread Jam............... (60.00)      41 Butter Naan............. (20.00)") 
            print(" 8  Veg. Sandwich........... (50.00)      42 Masala Kulcha........... (40.00)") 
            print(" 9  Veg. Toast Sandwich..... (50.00)                                         ") 
            print(" 10 Cheese Toast Sandwich... (70.00)      RICE                               ") 
            print(" 11 Grilled Sandwich........ (70.00)      ___________________________________")  
            print("                                          43 Plain Rice.............. (90.00)") 
            print(" SOUPS                                    44 Jeera Rice.............. (90.00)") 
            print("__________________________________        45 Veg Pulao...............(110.00)")                                                                                              
            print(" 12 Tomato Soup.............(100.00)      46 Peas Pulao..............(110.00)") 
            print(" 13 Hot & Sour Soup.........(100.00)                                         ") 
            print(" 14 Veg. Noodle Soup........(100.00)      CHINESE                            ") 
            print(" 15 Sweet Corn..............(100.00)      ___________________________________") 
            print(" 16 Veg. Munchow............(100.00)      47 Veg Hakka Noodles....... (60.00)") 
            print("                                          48 Pan Fried Noodles....... (80.00)") 
            print(" TRAVELLING TO INDIAN STREETS             49 Chesse Pasta............ (50.00)")
            print("__________________________________                                           ")
            print(" 17 Chole Bhature...........(100.00)      SOUTH INDIAN                       ")         
            print(" 18 Pav Bhaji............... (90.00)      ___________________________________")
            print(" 19 Veg. Momos.............. (80.00)      50 Idli(2pcs).............. (60.00)")
            print(" 20 Veg. Burger............. (60.00)      51 Plain/Masala Dosa.......(110.00)")
            print(" 21 Samosa/Tikia Chaat...... (50.00)      52 Onion Masala Dosa.......(110.00)")
            print(" 22 Bhel puri............... (50.00)      53 But. Oni. Masala Dosa...(130.00)")            
            print(" 23 Papdi Chaat............. (40.00)      54 Shezwan Dosa............(130.00)")            
            print("                                          55 Salsa Noodles Dosa......(130.00)")
            print(" MAIN COURSE                              56 Paneer Dosa.............(130.00)") 
            print("__________________________________        57 Rice Idli...............(130.00)") 
            print(" 24 Shahi Paneer............(130.00)      58 Sambhar Vada............(130.00)") 
            print(" 25 Kadai Paneer............(130.00)                                         ") 
            print(" 26 Handi Paneer............(130.00)      DESSERT                            ") 
            print(" 27 Palak Paneer............(130.00)      ___________________________________") 
            print(" 28 Chilli Paneer...........(150.00)      59 Vanilla/Pineapple....... (60.00)") 
            print(" 29 Matar Paneer............(150.00)      60 Strawberry/BlueBerry.... (60.00)") 
            print(" 30 Mix Veg.................(150.00)      61 Chocalate Chip.......... (80.00)") 
            print(" 31 Malai Kofta.............(150.00)      62 Butter Scotch........... (60.00)") 
            print(" 32 Jeera Aloo..............(150.00)      63 Brownie with Vanilla....(100.00)") 
            print(" 33 Aloo Dum................(150.00)      64 Choco Lava Cake.........(130.00)")
            print("\n\t IF YOU WANT TO EXIT PRESS 0 \n" + "_" * 72)
            ch=1;rt=0
            r=0;z=0
            lst=["20","35","35","35","60","60","60","50","50","70","70","100","100","100","100","100","100","90","80","60","50","50","40","130","130","130","130","150","150","150","150","150","150","150","150","150","150","35","35","20","20","40","90","90","110","110","60","80","50","60","110","110","130","130","130","130","130","130","60","60","80","60","100","130"]
            l=["Regular Tea","Masala Tea","Coffee","Cold Drink","Masala Cold Drink","Bread Butter","Bread Jam","Veg Sandwich","Veg Toast Sandwich","Cheese Toast Sandwich","Grilled Sandwich","Tomato Soup","Hot & Sour","Veg Noodle Soup","Sweet Corn","Veg Munchow","Chole Bhature","Pav Bhaji","Veg Momos","Veg. Burger","Samosa/Tikia Chaat","Bhel puri","Papdi Chaat","Shahi Paneer","Kadai Paneer","Handi Paneer","Paalak Paneer","Chilli Paneer","Matar Paneer","Mix Veg","Malai Kofta","Jeera Aloo","Aloo Dum","Chana Masala","Panner Tikka","Dal Butter Fry","Dal Makhani","Plain Roti","Butter Roti","Tandoori Roti","Butter Naan","Masala Kulcha","Plain Rice","Jeera Rice","Veg Pulao","Peas Pulao","Veg Hakka Noodles","Pan Fried Noodles","Chesse Pasta","Idli(2pcs)","Plain Dosa","Onion Masala Dosa","But. Oni. Masala Dosa","Shezwan Dosa","Salsa Noodles Dosa","Paneer Dosa","Rice Idli","Sambhar Vada","Vanilla/Pineapple","Strawberry/BlueBerry","Choclate Chip","Butter Scotch","Brownie with Vanilla","Choco LAVA cake"]
            while(ch!=0):
                z=0
                
                ch=int(input("Input-> "))
                if ch==0:
                    break
                c= ch-1
                for a in g:
                    z+=1
                    if str(a)==str(l[c]):
                        
                        g.pop(str(a))
                        print("x"*80)            
                        print('Error....\nSame Data Entered Twice....\nupdating order...\n')
                        print("x"*80,"\n\n")
                        h.pop((z-1))
                        z=0
                        break
                        
                g[l[c]]=lst[c]
                print(l[c],"...........",lst[c],"\n")
                x=int(input("How Many You Want to Order?: "))
                print("_____________________________________________________________________________") 
                h.append(x)
                if ch==1 or ch==41 or ch==40: 
                    rs=20
                    r=r+(rs*x) 
                elif (ch<=7 and ch>=5) or (ch<=60 and ch>=59) or ch==62 or ch==50 or ch==47 or ch==20: 
                    rs=60
                    r=r+(rs*x) 
                elif (ch<=9 and ch>=8) or (ch<=22 and ch>=21)or ch==49 : 
                    rs=50
                    r=r+(rs*x) 
                elif ch<=11 and ch>=10: 
                    rs=70
                    r=r+(rs*x) 
                elif (ch<=17 and ch>=12) or ch==63: 
                    rs=100
                    r=r+(rs*x) 
                elif (ch<=46 and ch>=45) or  (ch<=52 and ch>=51): 
                    rs=110
                    r=r+(rs*x) 
                elif ch<=37 and ch>=28: 
                    rs=150
                    r=r+(rs*x) 
                elif (ch<=39 and ch>=38) or (ch<=4 and ch>=2): 
                    rs=35
                    r=r+(rs*x) 
                elif ch==45 or ch==44 or ch==18: 
                    rs=90
                    r=r+(rs*x)  
                elif (ch<=58 and ch>=53) or (ch<=27 and ch>=24) or ch==64 : 
                    rs=130
                    r=r+(rs*x) 
                elif ch==61 or ch==43 or ch==19 or ch==48: 
                    rs=80
                    r=r+(rs*x)
                elif ch==42 or ch==23:
                    rs=40
                    r=r+(rs*x)
                else: 
                    print("Wrong Choice..!!")  

            print("Total Bill: ",r)
            r=r+rc.pop(n) 
            rc.append(r)
            Home()
        else: 
            pass
    if f == 0: 
        print("Invalid Customer Id") 
        Home()
       
                   











            
def Payment(): 
      
    ph=str(input("Phone Number: ")) 
    global i 
    f=0
      
    for n in range(0,i):

        if str(ph)== str(phno[n]) :
             if p[n]==0: 
                f=1
                rt=0
                z=0
                print(" Payment") 
                print("___________________________") 
                print("  MODE OF PAYMENT") 
                   
                print("  1- Credit/Debit Card") 
                print("  2- Paytm/PhonePe") 
                print("  3- Using UPI") 
                print("  4- Cash") 
                x=int(input("-> ")) 
                print("\n  Amount for R00M: ",(price[n]*days[n]))
                print("  food order is:")
                for x in g:
                    print(x,'.' * (25-len(str(x))) ,g[x]," " * (5-len(str(g[x]))),"*"," " * (2-len(str(h[z]))),h[z],'=',(int(g[x])*int(h[z])),'\n')
                    rt+=(int(g[x])*int(h[z]))
                    z+=1
                print("\n  Amount for FOOD: ",rt)
                print("\tTotal Bill : ",((price[n]*days[n])+rt))
                

                print("\n\t\tPAY FOR PACIFIC") 
                print("(y/n)") 
                ch=str(input("->")) 
                  
                if ch=='y' or ch=='Y': 
                    print("\n\n --------------------------------") 
                    print("           Hotel PACIFIC") 
                    print(" --------------------------------") 
                    print("              Bill") 
                    print(" --------------------------------") 
                    print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t") 
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*days[n],"\t") 
                    print(" Restaurant Charges: \t",rc[n]) 
                    print(" --------------------------------") 
                    print("\n Total Amount: ",(price[n]*days[n])+rt,"\t") 
                    print(" --------------------------------") 
                    print("          Thank You") 
                    print("          Visit Again :)") 
                    print(" --------------------------------\n") 
                    p.pop(n) 
                    p.insert(n,1) 
                    roomno.pop(n) 
                    custid.pop(n) 
                    roomno.insert(n,0) 
                    custid.insert(n,0) 
                      
             else: 
                  
                for j in range(n+1,i): 
                    if ph==phno[j] : 
                        if p[j]==0: 
                            pass
                          
                        else: 
                            f=1
                            print("\n\tPayment has been Made :)\n\n")  
    if f==0:     
        print("Invalid Customer Id") 
    Home() 
























def Record():
    b=0
    import mysql.connector
    from mysql.connector import Error


    
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                               database='hotel_management',
                               user='root',
                               password='mysql')
        if conn.is_connected():
            print('FULL SCREEN')

    except Error as e:
        print(e)



    cursor = conn.cursor()
    
    cursor.execute("select * from table1")
    lz=["Id","Name","Phone_no","Address","Room_Type"]
    z=["Price"]
    print(' ',"_" * 14,' ',"_" * 14,' ',"_" * 14,' ',"_" * 14,' ',"_" * 14,' ',"_" * 6,' ')

    for i in lz:
        c=str(i)
        print('|',i,end=str(' '* (15-len(c))),flush=True)
    print('|',str(z[0]),' |')

        
    for x in cursor:
        a=0
        b+=1
        
        for i in x:
            
            a=a+1
            if str(a)!='6':
                c=str(i)
                print('|',i,end=str(' ' * (15-len(c))),flush=True)
            else:
                print('|',i," " * (5-len(str(i))),'|')
    print('|',"_" * 14,'|',"_" * 14,'|',"_" * 14,'|',"_" * 14,'|',"_" * 14,'|',"_" * 6,'|')
    if b>=1:
        Home() 

    else: 
        print("No Records Found")
        Home()
    


def run (Name,Phone_no,Address,Room_Type,Price):
    import mysql.connector

    query = "INSERT INTO table1(Name,Phone,Address,Room_Type,Price) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (Name,Phone_no,Address,Room_Type,Price)

    conn = mysql.connector.connect(host='localhost',
                               database='hotel_management',
                               user='root',
                               password='mysql')
 
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    cursor.close()
    conn.close()

def main():
    for n in range(0,i):
        run(name[n],phno[n],add[n],room[n],price[n])
   



def export():
    import mysql.connector
    from mysql.connector import Error
    import os
    import pickle
    l=[]


    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                               database='hotel_management',
                               user='root',
                               password='mysql')
    except Error as e:
        print(e)



    cursor = conn.cursor()

    cursor.execute("select * from table1")


    phn = int(input("Phone No.: "))
    c=phn
    aa=0
    j=1
    while j: 
        while c:
            c=c//10
            aa+=1
            a=0
        if  aa==10:
            for x in cursor:

                z=eval(x[2] * 1)

                
                if phn == z:
                    a+=1
                    for f in x:
                        l.append(f)
                    print("\tCustomer Id Confirmed")
                    phn=0
            if a>=1:
                f=open("records.dat","wb")
                with open("records.dat","wb") as f:
                    pickle.dump(list(l),f)

                x=input("Do you want to read the file y/n")
                if x=="y" or x=="Y":
                    f=open("records.dat","rb")
                    r=pickle.load(f)                
                    print(r)
                else:
                    break
            else:
                print("\tCustomer Id Was Wrong")
                break    
            if phn != z and a==0:
                print("\tCustomer Id Was Wrong")
                break

        
        elif str(phn)== "":
            print("\tPhone no. is required ")
        elif aa!=10:
            print("\tPhone no. must contain 10 digits..")
        else:
            print("Error")
            break



database()
Home()


