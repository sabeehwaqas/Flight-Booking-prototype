#########################
'''

Done by: Muhammad Sabeeh Waqas      


'''

#Note : !!! this program ONLY works with 2 other text files, make sure that this program has access to them
#    files are:
#       "Flight passangers database.txt"
#       "FFF.txt"  


#########################

import os

class Node_F:    # flight class
    def __init__(self,d_i,name,ID,t,f,days,dur,d,a,dist):
        self.name=name
        self.ID=ID
        self.T_departure =t
        self.Freq =int(f)
        self.Days=days
        self.Type =d_i
        self.Dur=dur
        self.C_arrival =a 
        self.C_departure =d
        self.dist=float(dist)
        self.costB = self.cost(1)
        self.costA = self.cost(2)
        self.costE = self.cost(3)
        self.flights_per_week = Linkedlist()  # linked list of flights per week 
        self.next=None
        
    def cost(self,typ):   # fn to calculate cost of fligth with given distance
        if typ==1:
            return(self.dist*35)
        elif typ==2:
            return(self.dist*25)
        else:
            return(self.dist*15)
        
class Node_F_F:   # flight per week class
    def __init__(self,day):
        self.seats=200
        self.seat_B=10
        self.seat_A=20
        self.seat_E=170
        self.F_Day=day
        self.passangers=Linkedlist()  # linked list of passengers
        self.next=None
        self.Q = CQueue()  # queue of waiting list 

class Node_P:  # passengers class
    def __init__(self,Name,CNIC,Phone,Email,Age,Flight_ID,seat_type,time,date,day,Cost=0):
        self.Name=Name
        self.CNIC=CNIC
        self.Phone=Phone
        self.Email=Email
        self.Age=Age
        self.Flight_ID=Flight_ID
        self.seat_type=seat_type
        self.my_time=time
        self.my_date=date
        self.my_day=day
        self.B_no=None
        self.Cost=Cost
        self.seat_cost=None
        self.next=None

class CQueue:  # circular Queue class of 100 size, for waiting list
    def __init__(self, maxsize=100):
        self.items = [None]*100
        self.count=0
        self.rear=99
        self.front=0
	
    def is_empty(self):  # fn to check if Queue is empty
        return self.count == 0
    def isFull(self):  # fn to check if Queue is full
        return self.count==len(self.items)
	
    def length(self):  # fn to check the No. of items in the Queue
        return self.count
    def enqueue(self, item):  # fn to insert the element into the back of the Queue
        if self.isFull()!=True:
            self.rear=(self.rear+1)% 100
            self.items[self.rear]=item
            self.count=self.count+1
    def dequeue(self):  # fn to remove the front element from the Queue 
        if self.is_empty()!=True:
            i=self.items[self.front]
            self.front=(self.front+1)% 100
            self.count=self.count-1
            return i
	   
        
class Linkedlist:  # linkedlist class 
    def __init__(self):
        self.head=None
    def count(self):   # fn to count nodes in linked list
        temp=self.head
        c=0
        while temp!=None:
            c=c+1
            temp=temp.next
        return c

    def insert(self,x):   # fn to insert the data into head of linked list
        temp=self.head
        if self.head==None:
            self.head=x
        else:
            
            temp1=x
            temp1.next=temp
            self.head=temp1      
        
    def display_list(self):  # fn to display the whole linked list
        
        print("Sr.No   Flight      ID      Type               B/W                  duration        Time of Departure      Flights. per week     Days ")
        print("---------------------------------------------------------------------------------------------------------------------------------------------")
        
        temp=self.head
        i=1
        if self.head==None:  # if linked list is empty then this means no flight in list
            print("No flight Avaliable")
            return
        else:
            while temp!=None:
                print(i,")","  ",temp.name,"  ",temp.ID,"  ",temp.Type,"  ",temp.C_departure,"and",temp.C_arrival,"       ",temp.Dur,"    \t      ",temp.T_departure,"\t\t     ",temp.Freq," \t  \t ",temp.Days)
                i=i+1
                temp=temp.next
            return

def Delete_P(flight,flight1,P,op):  # fn to remove the passangers booking from the flight
    
    temp1=flight1.passangers.head       # getting the head of the passanger list
    if temp1==P:        # if head matches entered passangers booking no.
        temp2=temp1.next        # removing the passanger's booking
        temp1.next=None
        flight1.passangers.head=temp2
        if op==0:     # checking if deleted node (aka passangers data) is asked as return
            return temp1
        else:
            del temp1
            
    while temp1.next!=P:   # getting to the node with passangers booking
        temp1=temp1.next
            
    if P.next==None:    # if passangers booking is at the last of the list
        temp2=P
        temp1.next=None
        if op==0:
            return temp2
        else:
            del temp2
    else:       # if passangers booking is neither at the head nor at the last then deleting it
        temp2=P
        temp1.next=temp2.next
        if op==0:
            return temp2
        else:
            del temp2 
    
def simulation_booking():  # fn to call the database passangers 
    A=[]*50
    with open('Flight passangers database.txt','r') as file: # opening the database file
        line = file.readline()   #getting the line of the file
        
        for line in file:  #reading the line of the file
            
            for word in line.split():  #reading the word of the line
                
                A.append(word)   #adding the word into the list

            book_flight_simulation(A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8])  #calling the fn to add passanger into the list
            A.clear()  # emptying the list to ctore the next passanger

def intro():  # fn to display welcome
    
    print("----------------------------------")
    print("          WELCOME TO PIA ")
    print("----------------------------------")
def options_display():  #fn to display option to the user
    print("")
    print("----------------------------------")
    print(" Please! select an Option :")
    print("1)List of flights")
    print("2)Flights information")
    print("3)Book a flight")
    print("4)Cancel your flight")
    print("5)View Booking Details")
    print("6)Search flights")
    print("7)Search booking/ticket")
    print("8)Create a trip")
    print("9)Cancel trip")
    print("0)Exit :( ")
    print("")
    print("----------------------------------")
        
def list_flights(x=None):  # fn to display the list of flights 
    if x==None:
        print("")
        print("----------------------------------")
        print("         List of flights")
        print("----------------------------------")
        print(" Please! select an Option :")
        print("1) Domestics flights")
        print("2) International flights")
    if x!=None:
        op1=x   # getting the domestic or international option from where the fn is called 
    else:
        op1 = int(input("Enter the option:")) # getting the domestic or international option from the user directly 
    if op1==1:
        print("      Domestic Fligths")
        print("--------------------------------------------------------------------------------")
        Dom.display_list()  # calling fn to display the whole list of domestic flights
        print("--------------------------------------------------------------------------------")
    else:
        print("     International Flights")
        print("--------------------------------------------------------------------------------")
        Int.display_list() # calling fn to display the whole list of international flights
        print("--------------------------------------------------------------------------------")
    
def display(temp):  #fn displaying flight
        print("Flight      ID     Time of depature      Type        Duration      City of Arrival         City of Departure   Day")
        print("------------------------------------------------------------------------------------------------------------------------------")
        print(temp.name,"  ",temp.ID,"    ",temp.T_departure,"          ",temp.Type,"    ",temp.Dur,"         ",temp.C_arrival,"                    ",temp.C_departure,"     ",temp.Days)
        print("------------------------------------------------------------------------------------------------------------------ ------------")
        print("  ")

def display_F(temp1,temp11): #fn dispalying from flight per week
        
        
        print(temp1.name,"  ",temp1.ID,"    ",temp1.T_departure,"          ",temp1.Type,"    ",temp1.Dur,"         ",temp1.C_arrival,"                 ",temp1.C_departure,"         ",temp11.F_Day)
        
def R_flight_display(temp1,temp11):  # fn displaying the respective flight all detailes
    print("---------------------------------------")
    print("    Respective Flight details  ")
    print("---------------------------------------")
    
    print("Flight Name :",temp1.name)
    print("Flight ID :",temp1.ID)
    print("Time of Departure :",temp1.T_departure)
    print("Day of Departure :",temp11.F_Day)
    print("Domestic / international :",temp1.Type)
    print("Duration :",temp1.Dur)
    print("City of Arrival :",temp1.C_arrival)
    print("City of Departure :",temp1.C_departure)
    print("Seats booked :",200-int(temp11.seats))
    print("Total seats left :",temp11.seats)
    print("Business class seats left :",temp11.seat_B)
    print("    A    class seats left :",temp11.seat_A)
    print("Economy  class seats left :",temp11.seat_E)
    print("Business class seats charges :",int(temp1.costB)," Rs")
    print("    A    class seats charges :",int(temp1.costA)," Rs")
    print("Economy  class seats charges :",int(temp1.costE)," Rs")
    print("Flight distance :",temp1.dist," km")
    print("")
    print("------------------------------------------------------")

def flight_info():  # fn to display the flight information 
    print("----------------------------------")
    print("         Flights information")
    print("----------------------------------")
    list_flights()  # calling fn to display the whole list of flight 
    print("1)Enter name of Flight to see details")
    print("2)Enter ID of Flight to see details")

    op = int(input("Please select :"))  # by name or by ID
    print("----------------------------------------------------------------------------------------------------------------------")
    
    if op==1:   # if by name
        
        x = input("Use the name of flight :")  # getting flight name by user
        d = input("Enter the day : ")  # getting day of Flight
        print("")
        print("")
        print("Flight      ID     Time of depature      Type        Duration      City of Arrival         City of Departure   Day")
        print("------------------------------------------------------------------------------------------------------------------------------")
        
        temp1=Dom.head
        temp2=Int.head
            
        while temp1!=None:  # finding the flight in the domestic list 
            temp11=temp1.flights_per_week.head  # if found 
            
            if temp1.name==x:  
                while temp11!=None:  # finding the flight on entered day
                    if d == temp11.F_Day:  # if found
                        R_flight_display(temp1,temp11)   # calling fn to display the respective flight 
                    temp11=temp11.next
                return
            temp1=temp1.next
            
        while temp2!=None:   # finding the flight in the international list 
            temp22=temp2.flights_per_week.head
            if temp2.name==x:
                while temp22!=None:
                    if d == temp22.F_Day:
                        R_flight_display(temp2,temp22)
                    temp22=temp22.next
                return
            temp2=temp2.next
            
    else:    # if flight ID

        x = input("Use the ID of flight :")
        d = input("Enter the day : ")
        print("")
        print("")
        print("Flight      ID     Time of depature      Type        Duration      City of Arrival         City of Departure   Day")
        print("------------------------------------------------------------------------------------------------------------------------------")
        
        temp1=Dom.head
        temp2=Int.head
        
        while temp1!=None:
            temp11=temp1.flights_per_week.head
            
            if temp1.ID==x:
                while temp11!=None:
                    if d == temp11.F_Day:
                        R_flight_display(temp1,temp11)                   
                    temp11=temp11.next
               
                return
            temp1=temp1.next
            
        while temp2!=None:
            temp22=temp2.flights_per_week.head
            if temp2.ID==x:
                while temp22!=None:
                    if d == temp22.F_Day:
                        R_flight_display(temp2,temp22)
                    temp22=temp22.next
                return
            temp2=temp2.next
        
def SF_prev_booking_check(CNIC,new_flight):   # fn to check passengers booking in the exact same flight using CNIC
    temp=new_flight.passangers.head    # pointing to the passangers booking 
    found=False
    while temp!=None:
        if temp.CNIC==CNIC:  # if same CNIC found in the flight
            print("")
            print("----------------------------------------------------------")
            print("You Have already Booked this flight for ",CNIC, "CNIC no.")
            print("----------------------------------------------------------")
            search_booking(temp.B_no)   #calling fn to display the found matching flight booking details
            found=True
            break    
        temp=temp.next
    return found

def SD_prev_booking_check(CNIC,new_flight_day,new_flight):  # fn to check the passangers booking collsion with other flights under same CNIC
    day = new_flight_day.F_Day   # new flight day
    if new_flight.Type =="Domestic":  # domestic or international
        temp = Dom.head
    else:
        temp=Int.head
    while temp!=None:    
        temp1 = temp.flights_per_week.head  
        while temp1!=None:
            if temp1.F_Day == day:  # finding the flight day  
                temp3=temp1.passangers.head         
                while temp3!=None:
                    if temp3.CNIC == CNIC:  # if found the same CNIC flight 
                        T=time_gap2hr_check(new_flight,temp)        # calling fn to check the time gap 
                        T1 =time_gapsame_check(new_flight,temp)     # calling fn to check if time collsion

                        if T == True:
                            
                            if T1==False:
                                print("")
                                print("----------------------------------------------------------")
                                print(" !!! Warning  There Might exist a collision in flights !!!")      # if time gap of 2hours exist 
                                print("----------------------------------------------------------")
                                print("  Already Booked Flight : ")
                                print("")
                                search_booking(temp3.B_no)
                                print("")
                                pp = int(input(" If you still want to book this new Flight enter 1 : "))   # asking user to select if he can manage the flight 
                                if pp != 1:
                                    return True
                                else:
                                    return False
                                print("")
                            else:
                                print("")
                                print("----------------------------------------------------------")
                                print("          !!!  Warning collision in flights  !!!")
                                print("----------------------------------------------------------")      # if fligth time collsion exist
                                print("  Already Booked Flight : ")
                                print("")
                                search_booking(temp3.B_no)
                                print("")
                                print("    Sorry Can't Book this Flight , Please select another Flight ")
                                print("----------------------------------------------------------------")    # not possible to book the flight due to time collsion
                                print("")
                                return True
                    temp3=temp3.next       
            temp1=temp1.next    
        temp=temp.next
    return False

def time_gap2hr_check(new_flight,temp):  # fn to check the time gap
    
    flag=False
    T1 = int(new_flight.T_departure[0] + new_flight.T_departure[1])
    T2 = int(temp.T_departure[0] + temp.T_departure[1])

    if T1>T2:
        T=T1
        T1=T2
    else:
        T=T2
        T1=T1
    if T - T1 <= 2:   # if gap is equal to or greater than 2 hours 
        flag=True
       
    return flag

def time_gapsame_check(new_flight,temp):   # fn to check the time collsion
    
    flag=False
    T1 = int(new_flight.T_departure[0] + new_flight.T_departure[1])
    T2 = int(temp.T_departure[0] + temp.T_departure[1])

    if T1==T2:    # no gap hence time collsion
        flag=True    
    return flag
     

    
def book_flight(x=None,y=None,n=None,text=None,name=None,phone=None,email=None,cnic=None,age=None):  # fn to book the flight 

    if x==None:
        print("----------------------------------")
        print("         Book a Flight")
        print("----------------------------------")
        total_cost=0  # variable storing the total cost to tickets
        print(" Select the flight ")
        print("---------------------------------")
        print(" Please! select an Option :")
        print("1) Domestics flights")
        print("2) International flights")
    else:
        total_cost=0
    if y!=None:
        op1=y
    else:
        op1 = int(input("Enter the option:"))  # selecting domestic or international flight
    
    if op1==1:  #if domestic
        if x==None:
            print("      Domestic Fligths")
            print("---------------------------------")
            Dom.display_list()  # displaying the domestic flights
            print("---------------------------------")
        Type = Dom.head
    elif op1==2:  # if international
        if x==None:
            print("     International Flights")
            print("---------------------------------")
            Int.display_list() # displaying the international flights
            print("---------------------------------")
        Type = Int.head
    if x!=None:
        ID=x
    else:
        ID = input("Enter the Flight ID you want to Book :")  # asking user to enter the flight ID to book
    
    while Type.ID!=ID:
        Type=Type.next
    your_Flight =Type    # storing the flight address in the your_flight variable for easier access

    print("Avaliable days : ",your_Flight.Days)  #displaying the avaliable days per week of selected flight

    day = input("Enter the Flight day, you want to travel on :")  # user selecting the day
    flag1=False
    for i in range(len(your_Flight.Days)):
        if your_Flight.Days[i]==day  or your_Flight.Freq==7:  # on entered day flight travels
            flag1=True
            break
    if flag1==False:
        print("your selected flight doesnot occur at entered day")
        return
        
    if toDay!=day:     # if flight is not on todays day 
        my_day =day
        day_list = ['M','T','W','t','F','S','s']   
        for i in range (7):
            if day==day_list[i]:    
                dc = i   # getting the selected day number  
                break
        for i in range(7):
            if toDay==day_list[i]:
                tdc = i   # getting the today's day number
                break
        c=0
        while tdc!=dc:
            tdc = (tdc+1)%7     # finding the today's and flight day difference in days
            c=c+1
        
        D = int(toDate[0]+toDate[1]) +c   # getting selected flight date 
        M = int(toDate[3]+toDate[4])      # getting selected flight month  
        
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            q=31
        elif M == 4 or M==6 or M==9 or M==11:
            q=30
        elif M==2:
            q=28   ## can add year wise if handled leap year 
            
        if D<=q:    # if the selected flight date is inbetweeen 1-30 or 1-31
            if len(str(D))==1:
                D = "%02d" % D         # converting e.g 2/1/2021 to 02/01/2021
            if len(str(M))==1:
                M = "%02d" % M
            my_date = str(D)+"/"+str(M)     #concatinating selected flight date and month

        else:  # if the selected flight date is not inbetween 1-30 or 1-31 
             
            D = D%q   # bring it into 1-30 range
            M=M+1   # adding  the month
            if len(str(D))==1:
                D = "%02d" % D
            if len(str(M))==1:
                M = "%02d" % M
            my_date=str(D)+"/"+str(M)        
        
    else:      # if selected flight is in todays day 
        my_day =day
        
        D = int(toDate[0]+toDate[1]) +7    # getting selected flight date next weeek same day
        if len(str(D))==1:
            D = "%02d" % D
            D =int(D)
        
        M = int(toDate[3]+toDate[4])
        if len(str(M))==1:
            M = "%02d" % M
            M=int(M)
        
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            q=31
        elif M == 4 or M==6 or M==9 or M==11:
            q=30
        elif M==2:
            q=28   ## can add year wise if handled leap year 
            
        if D<=q:
            if len(str(D))==1:
                D = "%02d" % D
            if len(str(M))==1:
                M = "%02d" % M
            my_date = str(D)+"/"+str(M)
        else:
            
            D = D%q
            M=M+1
            if len(str(D))==1:
                D = "%02d" % D
            if len(str(M))==1:
                M = "%02d" % M
            my_date=str(D)+"/"+str(M)

    print("---------------------------------------------------------------------")
    print(" The closed Flight will be Booked On : ",my_day,"  ",my_date,"/21", )   # displaying the selected flight upcoming flight date 
    print("---------------------------------------------------------------------")
    print("")
    g = int(input("If you want to proceed enter 1 :")) # asking user for confirmation
    if g!=1:
        return
  
    your_Flight_day = your_Flight.flights_per_week.head  

    while your_Flight_day !=None:
        if your_Flight_day.F_Day == my_day:         #getting the pointer for seleted flight on the selected day  
            break
        your_Flight_day=your_Flight_day.next
    if n!=None:
        N=n
    else:
        N = int(input("Enter the Number of seats you want to book:"))   # asking user to enter the no. of tickets he wants for the selected flight

    seats_left = your_Flight_day.seats-N                   #checking for seats avaliablility
    if seats_left <0 :   
        print(" Booking NOT avaliable!!!")
        print("*** Sorry You cant Book the Flight for",N,"passagers***")
        return

    waiting_flag=False
       
    if seats_left <=100:    # if seats left are less than or equal to 100
        waiting_flag=True
        print(" Booking NOT avaliable!!!")
        print("*** Sorry You can't Book the Flight for",N,"passagers IMMEDIATELY ***")
        print("----------------------------------------------------------------------------------")
        print(" we have prioritized your request will let you know when any booking is cancelled ")
        print(" Kindly Give your Details : ")
        print("----------------------------------------------------------------------------------")

        if your_Flight_day.Q.length()==100:   # checking if waiting list Queue has space or not 
            print("---------------------------------------------")
            print(" ***  Sorry no room for waiting list *** ")
            print("---------------------------------------------")
            waiting_flag =False   
            return
        
        
    if text!=None:
        File_ticket=text
    else:
        File_ticket=input("please enter Ticket file name (please add '.txt' at the end ):")   # making the file to store the ticket
    
    f = open(File_ticket,"a+")
    while N!=0:
        if name!=None and phone!=None and email!=None and cnic!=None:  #if fn is called from another fn then data is take from fn
            Name = name
            Phone = phone
            Email =email
            CNIC = cnic
        else:                         #if fn is NOT called from another fn then data is taken fromm user directly
            Name = input("Enter the name of passanger:")     # getting Name of passanger
            Phone =input("Enter the passengers phone no.:")  # getting Phone of passanger
            Email =input("Enter the passengers email:")      # getting Email of passanger
            CNIC = input("Enter your CNIC no. :")            # getting CNIC of passanger

        found = SF_prev_booking_check(CNIC,your_Flight_day)  # calling fn to check collsion with same flight

        if found==True:
            print("")
            v = int(input("If you want to proceed for other passangers enter 1:"))
            if v==1:
                break
            else:
                return
        
        collision = SD_prev_booking_check(CNIC,your_Flight_day,your_Flight)  # calling fn to check collsion with other flights

        if collision==True:
            print("Collision")
            break
               
        if age!=None:
            Age = age
        else:
            Age = input("Enter the passenger age:")   #getting age of the user
        if Age<="12":   # if age is less than equal to 12 
            reduction=0.75   # ticket rate is 75%
        else:
            reduction=1   # if age is greater than 12 then ticket rate is 100%
            
    
        print("Select the option of the type of seat you want for",Name)    
        if your_Flight_day.seat_B!=0:
            print("1) Business class       Fare = ",int(your_Flight.costB)*reduction,"Rs")
        if your_Flight_day.seat_A!=0:
            print("2) A class              Fare = ",int(your_Flight.costA)*reduction,"Rs")               # seletion of seat type
        if your_Flight_day.seat_E!=0:
            print("3) Economy  class       Fare = ",int(your_Flight.costE)*reduction,"Rs")
        seat_type=int(input("select the option:"))
        if seat_type==1:
            your_Flight_day.seat_B =your_Flight_day.seat_B -1
            your_Flight_day.seats=your_Flight_day.seats-1             # reducing the seat count from selected flight total seats and seat type
            book_no2=str(your_Flight_day.seat_B)    
            if reduction==0.75:   # applying reduction (age factor)
                Cost=int(your_Flight.costB)*reduction
            else:
                Cost=int(your_Flight.costB)
            seat_type="B class"
        elif seat_type==2:
            your_Flight_day.seat_A =your_Flight_day.seat_A -1
            your_Flight_day.seats=your_Flight_day.seats-1
            book_no2=str(your_Flight_day.seat_A)
            if reduction==0.75:
                Cost=int(your_Flight.costA)*reduction
            else:
                Cost=int(your_Flight.costA)
            seat_type="A class"
        elif seat_type==3:
            your_Flight_day.seat_E =your_Flight_day.seat_E -1
            your_Flight_day.seats=your_Flight_day.seats-1
            book_no2=str(your_Flight_day.seat_E)
            if reduction==0.75:
                Cost=int(your_Flight.costE)*reduction
            else:
                Cost=int(your_Flight.costE)
            seat_type="E class"
        
        o = Node_P(Name,CNIC,Phone,Email,Age,your_Flight.ID,seat_type,your_Flight.T_departure,my_date,my_day)   # making a node of passanger 
        your_Flight_day.passangers.insert(o)   # inserting the node into the flight per week passanger list
        total_cost = total_cost + Cost  # getting the total cost of the booking 
        print("-------------------------------------------------")
        print("Name :",o.Name)
        print("CNIC :",o.CNIC)
        print("Phone no. :",o.Phone)
        print("Email Address: ",o.Email)
        print("Age :",o.Age)
        print("Flight ID:",your_Flight.ID)
        print("Seat class :",o.seat_type)
        print("Time of Departure:",o.my_time)                                   ## displaying all the information of booking 
        print("Date of Departure:",o.my_date)
        print("Day of Departure:",o.my_day)        
        print("Type :",your_Flight.Type)
        print("Duration :",your_Flight.Dur)
        print("City of Arrival :",your_Flight.C_arrival)
        print("City of Departure :",your_Flight.C_departure)
        print("charges :",Cost," Rs")
        print("-------------------------------------------------")
        confirm = input("To confirm your Ticket press 1 : ")          # Asking for confirmation

        if waiting_flag==True:  # if booking have exceeded 100
            print(" We will automatically book your ticket and inform you as soon as we get any seat for you ")
            your_Flight_day.Q.enqueue(o)    # adding passanger's booking to Queue
            return
            
        if confirm!="1":      # if user didn't confirm the booking 
            your_Flight_day.seats=your_Flight_day.seats + 1
            
            if o.seat_type=="B class":
                your_Flight_day.seat_B =your_Flight_day.seat_B +1
            elif o.seat_type=="A class":
                your_Flight_day.seat_A =your_Flight_day.seat_A +1           # Adding back the flight seats count
            elif o.seat_type=="E class":
                your_Flight_day.seat_E =your_Flight_day.seat_E +1
            print("")
            print("-------------------------------------------------")
            print("              Booking Process Cancelled ")       # Displaying the message of cancellation
            print("-------------------------------------------------")
            print(" ")
            return
        
        Book_no = your_Flight.ID + book_no2 + my_day    # creating the booking 
        o.B_no =Book_no    # inserting the booking No. into the passanger's node
        o.Cost=Cost      # inserting the Cost into the passanger's node
        print("")
        print("-------------------------------------------------")
        print("   YOUR BOOKING NO. is ",o.B_no)
        print("-------------------------------------------------")
        print("")
        f.write("---------------------------------------------------------------------------------\n\n")
        f.write("                               PIA come fly with us! \n")
        f.write("                                   Booking pass\n\n")
        f.write("\nName of Passanger : ")
        f.write(Name)
        f.write("\nCNIC of Passanger : ")
        f.write(CNIC)
        f.write("\nPhone No. :")
        f.write(Phone)
        f.write("\nEmail Address :")
        f.write(Email)
        f.write("\nFlight ID :")
        f.write(your_Flight.ID )
        f.write("\nSeat type :")
        f.write(seat_type)                                                                                     #### Making the ticket in the txt file
        f.write("\nTime of Departure :")
        f.write(your_Flight.T_departure)
        f.write("\nDay of Departure :")
        f.write(o.my_day)
        f.write("\nDate of Departure :")
        f.write(o.my_date)
        f.write("\nDomestic/International :")
        f.write(your_Flight.Type)
        f.write("\nFlight Duration :")
        f.write(your_Flight.Dur )
        f.write("\nCity of Arrival :")
        f.write(your_Flight.C_arrival)
        f.write("\nCity of Departure :")
        f.write(your_Flight.C_departure )
        f.write("\nBooking No. : ")
        f.write(Book_no )
        f.write("\n\n  Charges : ")
        Cost=str(Cost)
        f.write(Cost)
        f.write("Rs")
        f.write("\n\n---------------------------------------------------------------------------------")
        f.write("\n\n\n")

        with open("Flight passangers database.txt", "a+") as file_object:
                                                         # Move read cursor to the start of file.
            file_object.seek(0)
                                                          # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
                                                  # Append text at the end of file
            A=[]*50
            if your_Flight.Type =="Domestic":
                A.append(1)
            else:
                A.append(2)
            A.append(your_Flight.ID)
            A.append(o.my_day)
            A.append(Name)
            A.append(Phone)                                    # making a list of passangers data
            A.append(Email)
            A.append(CNIC)
            A.append(Age)
            if seat_type =="B class":
                A.append(1)
            elif seat_type =="A class":
                A.append(2)
            else:
                A.append(3)
                
            file_object.write(str(A[0]))
            file_object.write(" ")
            file_object.write(str(A[1]))
            file_object.write(" ")
            file_object.write(str(A[2]))
            file_object.write(" ")
            file_object.write(str(A[3]))
            file_object.write(" ")                          # adding the passangers data into the database file
            file_object.write(str(A[4]))
            file_object.write(" ")
            file_object.write(str(A[5]))
            file_object.write(" ")
            file_object.write(str(A[6]))
            file_object.write(" ")
            file_object.write(str(A[7]))
            file_object.write(" ")
            file_object.write(str(A[8]))
            
                
        file_object.close()
        if N!=1:
            print("-------------")
            print("    Next ")
            print("-------------")
        N=N-1
    if x!=None:
        f.close()
        return total_cost,Book_no,o.my_time,o.my_date,o.my_day
    
    else:
        
        f.write("\n\n Total Charges: ")
        total_cost=str(total_cost)
        f.write(total_cost)                     # calculating the total cost of al tickets of selected flight and adding into the ticket file
        f.write("Rs")
        f.close()
    
        print("---------------------------------------------------------------------------------")
        print("")
        print(" Thank you  ")
        print("")
        print("---------------------------------------------------------------------------------")

def book_flight_simulation(op,FID,Fday,name,phone,email,cnic,age,st):   # Fn to add passangers into the flight from the data base
   
    total_cost=0
    
    op1 = int(op )#
    
    if op1==1:
        Type = Dom.head
    else:
        Type = Int.head
    
    ID = str(FID)  #                                                        #### All the logic is almost similar to the "book_flight"

    while Type.ID!=ID:                                                      #### no input is asled from user and no ticket is made
        Type=Type.next
    your_Flight =Type
    
    day = str(Fday) #
    flag1=False
    for i in range(len(your_Flight.Days)):
        if your_Flight.Days[i]==day  or your_Flight.Freq==7:
            flag1=True
            break
    if flag1==False:
        return
        
    if toDay!=day:
        my_day =day
        day_list = ['M','T','W','t','F','S','s']
        for i in range (7):
            if day==day_list[i]:
                dc = i
                break
        for i in range(7):
            if toDay==day_list[i]:
                tdc = i
                break
        c=0
        while tdc!=dc:
            tdc = (tdc+1)%7
            c=c+1
            
        D = int(toDate[0]+toDate[1]) +c
        M = int(toDate[3]+toDate[4])
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            q=31
        elif M == 4 or M==6 or M==9 or M==11:
            q=30
        elif M==2:
            q=28   ## can add year wise if handled leap year 
            
        if D<=q:
            my_date = str(D)+"/"+str(M)
        else:
            D = D%q
            M=M+1
            my_date=str(D)+"/"+str(M)        
        
    else:
        my_day =day

        D = int(toDate[0]+toDate[1]) + 7 
        M = int(toDate[3]+toDate[4])
        
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
            q=31
        elif M == 4 or M==6 or M==9 or M==11:
            q=30
        elif M==2:
            q=28   ## can add year wise if handled leap year 
            
        if D<=q:
            my_date = str(D)+"/"+str(M)
        else:
            D = D%q
            M=M+1
            my_date=str(D)+"/"+str(M)

     
    your_Flight_day = your_Flight.flights_per_week.head

    while your_Flight_day !=None:
        if your_Flight_day.F_Day == my_day:
            break
        your_Flight_day=your_Flight_day.next
        

    if your_Flight_day.seats-1<=100:
        return

    Name = name #
    Phone =phone #
    Email =email #
    CNIC = cnic #
          
    Age = age #
    if Age<="12":
        reduction=0.75
    else:
        reduction=1

    seat_type=int(st) #
    if seat_type==1:
        your_Flight_day.seat_B =your_Flight_day.seat_B -1
        your_Flight_day.seats=your_Flight_day.seats-1
        book_no2=str(your_Flight_day.seat_B)
        if reduction==0.75:
            Cost=int(your_Flight.costB)*reduction
        else:
            Cost=int(your_Flight.costB)
        seat_type="B class"
    elif seat_type==2:
        your_Flight_day.seat_A =your_Flight_day.seat_A -1
        your_Flight_day.seats=your_Flight_day.seats-1
        book_no2=str(your_Flight_day.seat_A)
        if reduction==0.75:
            Cost=int(your_Flight.costA)*reduction
        else:
            Cost=int(your_Flight.costA)
        seat_type="A class"
    elif seat_type==3:
        your_Flight_day.seat_E =your_Flight_day.seat_E -1
        your_Flight_day.seats=your_Flight_day.seats-1
        book_no2=str(your_Flight_day.seat_E)
        if reduction==0.75:
            Cost=int(your_Flight.costE)*reduction
        else:
            Cost=int(your_Flight.costE)
        seat_type="E class"
    
    o = Node_P(Name,CNIC,Phone,Email,Age,your_Flight.ID,seat_type,your_Flight.T_departure,my_date,my_day)
    your_Flight_day.passangers.insert(o)

    Book_no = your_Flight.ID + book_no2 + my_day
    o.B_no =Book_no
    o.Cost=Cost   

def time_gap_calculator(ct,cd,dt,dd):    #Fn to calculate the time gap between curent day and the flight day  (used in cancel_flight)
    days =['M','T','W','t','F','S','s']
    for i in range(6):
        if cd==days[i]:
            cd=i            # finding the current day number as per week
            break
    temp=days[cd]
    c=0
    for i in range(1,7):
        if temp==dd:                   # getting the flight day number as per week 
            break
        k = (cd+i)%7
        temp=days[k]
        c=c+1
    c=c-1

    ct_in_hr = 24  - int(ct[0]+ct[1])      # current day time in hours
    ct_in_m = int(ct[3]+ct[4])           # current day time in min
    ct_in_m = int(ct_in_hr) * 60 + ct_in_m     # current total time in min

    dt_in_hr = int(dt[0]+dt[1])              #flight day time in  hours
    dt_in_m = int(dt[3]+dt[4])             # flight day time in min
    dt_in_m = int(dt_in_hr) * 60 + dt_in_m       # flight day total time in min

    D_in_m = c*24*60    
    
    gap = ct_in_m +dt_in_m + D_in_m    # time gap in minutes between flight and current time

    return(gap)
            

def cancel_flight(x=None):    # fn to cancel the flight 
    print("----------------------------------")
    print("        Cancel a booking")   
    print("----------------------------------")
    if x==None:
        
        No=input("Enter the Booking No. to cancel:")    #Asking user to enter the booking no. to cancel
    else:
        No=x
    C_flight = search_booking(No)     # searching the booking by calling the fn and display its detail
    if C_flight == None:
        return   # if no booking found then return 
    print("--------------------------------------------------")
    print("    Do you want to cancel this flight's Booking ")
    op=int(input("      Press 1 to confirm :"))   # asking user for confirmation of cancellation
    print("--------------------------------------------------")
    if op!=1:   # if NO
        print("---------------------------")
        print(" Booking Not Cancelled ")   # Booking not cancelled
        print("---------------------------")
        return
        # if YES
    C= Delete_P(C_flight[0],C_flight[1],C_flight[2],0)  # Fn to find and cancel the node
    C_flight[1].seats=C_flight[1].seats + 1       # adding back the total seats count
    s_t = C_flight[2].seat_type       #checking seat type
    if s_t =="B class":
        C_flight[1].seat_B = C_flight[1].seat_B +1     #adding back the seat count as per seat type
    elif s_t =="A class":
        C_flight[1].seat_A = C_flight[1].seat_A +1
    else:
        C_flight[1].seat_E = C_flight[1].seat_E +1
    Cost = C.Cost   # getting the booking cost 
    Current_time = str(toTime)   # getting the current time
    Current_day = str(toDay)     # getting the current day
    D_time = str(C.my_time)      # getting the flight time
    D_day = str(C.my_day)        # getting the flight day

    gap_min = time_gap_calculator(Current_time,Current_day,D_time,D_day)   # calling the Fn to find the gap between flight and current
    
    if gap_min >=4320:   # if gap time in min is greater or equal to 72 hours 
        # 100%
        print("-------------------------------------------------------------")
        print(" Refunded 100% as booking Cancelled 72hrs prior to departure")
        print(" chargers refunded = ",Cost*1 ," Rs")               # 100% refund 
        print("-------------------------------------------------------------")
    elif gap_min >=2880 and gap_min<4320:    # if gap time in min is between  48 to 72 hours 
        #75%
        print("------------------------------------------------------------")
        print(" Refunded 75% as booking Cancelled 48hrs prior to departure")
        print(" chargers refunded = ",Cost*0.75 ," Rs")            # 75% refund
        print("------------------------------------------------------------")
    elif gap_min >=1440 and gap_min<2880:   # if gap time in min is between  24 to 48 hours
        #50%
        print("------------------------------------------------------------")
        print(" Refunded 50% as booking Cancelled 24hrs prior to departure")
        print(" chargers refunded = ",Cost*0.5 ," Rs")
        print("------------------------------------------------------------")
    elif gap_min>=720 and gap_min<1440:   # if gap time in min is between  12 to 24 hours
        #25%
        print("------------------------------------------------------------")
        print(" Refunded 25% as booking Cancelled 12hrs prior to departure")
        print(" chargers refunded = ",Cost*0.25 ," Rs")           # 25% refund
        print("-------------------------------------------------------------")
    elif gap_min<720 and gap_min>0 :   # if gap time in min is between  24 to 48 hours
        #no refund
        print("---------------------------------------------------------------------------------")
        print(" No Refunded possible as booking Cancelled in less than 12hrs prior to departure")
        print(" chargers refunded = ",Cost*0 ," Rs")              # NO refund 
        print("----------------------------------------------------------------------------------")
    else:   # if gap time in min is between  24 to 48 hours    
        print("---------------------------------------------------")
        print("Flight Can't be cancelled as Flight has Departured")   # can't cancel as the Flight departure time has passed 
        print("---------------------------------------------------")

    if C_flight[2].Flight_ID[2]==0:   # getting if flight is domestic or international
        op=1
    else:
        op=2

    while C_flight[1].Q.is_empty()!=True:   # checking for waiting list of booking
        P = C_flight[1].Q.dequeue()    # removinf the booking node from passangers list
        if P.seat_type =="B class":
            st = 1
        elif P.seat_type =="A class":                   # getting passangers seat type
            st = 2
        else:
            st = 3
        book_flight_simulation(op,P.Flight_ID,P.my_day,P.Name,P.Phone,P.Email,P.CNIC,P.Age,st)  # automatiically booking the waiting list passangers orderwise

        print("---------------------------------------------------")
        print(" Confirm Booking waiting list Passangers ...")
        print("---------------------------------------------------")
        

def view_booking():    # Fn to view the booking details 
    print("----------------------------------")
    print("     View Booked Flight's detail")
    print("----------------------------------")
    No=input("Enter the Booking No.:")        # Asking for booking no. from the user 
    print("----------------------------------")
    print("    The Booking No. detail is  ")
    print("----------------------------------")
    
    B_flight = search_booking(No)   #  calling the fn to search the booking and display passangers detail
    if B_flight ==None:
        return
    print("---------------------------------------")
    print("    Respective Booked Flight details  ")
    print("---------------------------------------")
    
    print("Flight Name :",B_flight[0].name)
    print("Flight ID :",B_flight[0].ID)
    print("Time of Departure :",B_flight[0].T_departure)
    print("Day of Departure :",B_flight[1].F_Day)
    print("Domestic / international :",B_flight[0].Type)
    print("Duration :",B_flight[0].Dur)
    print("City of Arrival :",B_flight[0].C_arrival)
    print("City of Departure :",B_flight[0].C_departure)                             # displaying the detail of the Flight in which booing was done
    print("Seats booked :",200-int(B_flight[1].seats))
    print("Total seats left :",B_flight[1].seats)
    print("Business class seats left :",B_flight[1].seat_B)
    print("    A    class seats left :",B_flight[1].seat_A)
    print("Economy  class seats left :",B_flight[1].seat_E)
    
    print("Business class seats charges :",int(B_flight[0].costB)," Rs")
    print("    A    class seats charges :",int(B_flight[0].costA)," Rs")
    print("Economy  class seats charges :",int(B_flight[0].costE)," Rs")
    
    print("Flight distance :",B_flight[0].dist," km")
    print("")
    print("------------------------------------------------------")

        
    
def search_flight(x=None):     # fn to search the flight from the name 
    print("----------------------------------")
    print("         Search Flight")
    print("----------------------------------")
    c=0
    temp=0
    if x!=None:
        F_name = x
    else:
        F_name =input("Enter the flights name you want search (e.g ISB_KHR):")   # asking the user for the name of the flight
    flight1=Dom.head
    flight2=Int.head
    print("---------------------------------------")
    print("  Following are the Flights Avalible:")
    print("---------------------------------------")
    while flight1!=None:   # checking for the flight in the domestic list
        if flight1.name==F_name:  # if found
            temp=1
            display(flight1)        #calling the fn to diaplay the flight    
            c=c+1   # flag to check if found
        flight1=flight1.next
        
    while flight2!=None:   # checking for the flight in the international list
        if flight2.name==F_name: # if found
            temp=2
            display(flight2)       #calling the fn to display the flight  
            c=c+1   # flag to check if found
        flight2=flight2.next
    
    if c==0:  # if flag is false
        print("-------------------------------------")
        print("      No Flight from ",F_name)   # no flight found
        print("-------------------------------------")
    else:
        return temp
        
        
def search_booking(x=None):   # fn to search the booking in the flighth
    print("----------------------------------")
    print("         Search Booking")
    print("----------------------------------")
    if x!=None:
        No=x
    else:
        No=input("Enter the Booking Number :")    # getting the booking no.
    flight1=Dom.head
    flight2=Int.head
    while flight1!=None:   # checking the flight in the domestic list
        flight11=flight1.flights_per_week.head
        while flight11!=None:
            temp = flight11.passangers.head
            while temp!=None:
                if temp.B_no==No:   # if booking found
                    print("Found !!! ")
                    print("-------------------------------------------------")
                    print("             For Booking No.:",No)
                    print("")
                    print("Name :",temp.Name)
                    print("Phone no. :",temp.Phone)
                    print("Email Address: ",temp.Email)
                    print("Age :",temp.Age)
                    print("Flight ID:",flight1.ID)                          # displaying the users detail
                    print("Seat class :",temp.seat_type)
                    print("Time of Departure:",temp.my_time)
                    print("Day of Departure:",temp.my_day)
                    print("Date of Departure:",temp.my_date)
                    print("Type :",flight1.Type)
                    print("Duration :",flight1.Dur)
                    print("City of Arrival :",flight1.C_arrival)
                    print("City of Departure :",flight1.C_departure)
                    print("charges :",temp.Cost," Rs")
                    print("-------------------------------------------------")
                    return flight1,flight11,temp # returning the flight,flight per week and passanger pointers
                temp=temp.next
            flight11=flight11.next
        flight1=flight1.next
        
    while flight2!=None:    # checking the flight in the international list
        flight22=flight2.flights_per_week.head
        while flight22!=None:
            temp = flight22.passangers.head
            while temp!=None:
                if temp.B_no==No:   # if booking found
                    print("Found !!! ")
                    print("-------------------------------------------------")
                    print("             For Booking No.:",No)
                    print("")
                    print("Name :",temp.Name)
                    print("Phone no. :",temp.Phone)
                    print("Email Address: ",temp.Email)
                    print("Age :",temp.Age)
                    print("Flight ID:",flight2.ID)
                    print("Seat class :",temp.seat_type)
                    print("Time of Departure:",temp.my_time)               # displaying the users detail
                    print("Day of Departure:",temp.my_day)
                    print("Date of Departure:",temp.my_date)
                    print("Type :",flight2.Type)
                    print("Duration :",flight2.Dur)
                    print("City of Arrival :",flight2.C_arrival)
                    print("City of Departure :",flight2.C_departure)
                    print("charges :",temp.Cost," Rs")
                    print("-------------------------------------------------")
                    return flight2,flight22,temp
                temp=temp.next
            flight22=flight22.next
        flight2=flight2.next
        print("--------------------------------------------------")
        
    print("  Flight Not Found against ",No,"Booking number")
    print("--------------------------------------------------")

def destination_check(d):   # fn to check the destination across number ( Used in the create_trip )
    if d==1:
        return 'LHE'
    elif d==2:
        return 'ISB'
    elif d==3:
        return 'KHI'
    elif d==4:
        return 'DXB'
    elif d==5:
        return 'LON'
    elif d==6:
        return 'JED'
    elif d==7:
        return 'DOH'
    elif d==8:
        return 'IST'

def create_trip(): #Fn to create a trip
    print("----------------------------------")
    print("         Create a trip ")
    print("----------------------------------")
    flag=0
    print("")
    print("Remember : your trip route should be logical as per the given list below ")
    print("                These are all the flight That PIA offers")
    print("")
    list_flights(1)         # displaying the domestic flights list
    list_flights(2)         # displaying the international flights list
    print("")
    
    op = int(input("Enter the No. of destinations you want to add in the trip : "))
    if op==2:   # if user only wants to visit 2 destination hence no need for trip making 
        print("")
        print("-----------------------------------------------------------------------------------")
        print(" As you want one flight trip kindly select option '3)Book a flight' from the menu  ")
        print("-----------------------------------------------------------------------------------")
        print("")
        return
    if op<2:   # if user entered less than 2 destination hence no possible to do that
        print("")
        print("-----------------------------------------------------------------------------------")
        print("             As you selected only one destination, trip can't exist   ")
        print("-----------------------------------------------------------------------------------")
        print("")
        return
    
    B = []*op
    total_cost=[]*op
    des=[]*op
    v=0
    j=0
    name =input("Enter your Name : ")
    B.append(name)
    phone =input("Enter your Phone no. : ")
    email =input("Enter your Email : ")             # getting the information of user 
    cnic =input("Enter your CNIC : ")
    age =input("Enter your Age : ")
    text = input("Enter the name of the text file to save your tickets in (please ended it with .txt : ")

    for i in range (op):  
        if i!=0:
            print("-------------------------------------------")
            print(" PIA offers following destination visits: ")
            print("-------------------------------------------")
            if flag==1 and j==0:
                print("2) Islamabad")
                print("3) Karachi")
                print("4) Dubai")
                print("5) London")      # showing the destinations except Lahore(because lahore was select just before it)
                print("6) Jeddah")
                print("7) Doha")
                print("8) Istanbul")
                print("")
            elif flag==2 and j==0:
                print("1) Lahore")
                print("3) Karachi")
                print("4) Dubai")
                print("5) London")     # showing the destinations except Lahore(because lahore was select just before it)
                print("6) Jeddah")
                print("7) Doha")
                print("8) Istanbul")
                print("")
            elif flag==3 and j==0:
                print("1) Lahore")
                print("2) Islamabad")
                print("4) Dubai")
                print("5) London")     # showing the destinations except Lahore(because lahore was select just before it)
                print("6) Jeddah")
                print("7) Doha")
                print("8) Istanbul")
                print("")
            else:
                print("1) Lahore")
                print("2) Islamabad")
                print("3) Karachi")
                print("4) Dubai")       # showing the destinations except Lahore(because lahore was select just before it)
                print("5) London")
                print("6) Jeddah")
                print("7) Doha")
                print("8) Istanbul")
                print("")
        
            d = int(input("Enter the destination no .from above that you want to add to trip :"))   # asking user to enter the destination
            j=j+1
            
            d = destination_check(d)   # getting the destination no. through the fn
       
            des.append(d)    # adding it into the list of destinations
        
            print(i+1,")",des[i])
            print("------------------")
            
        else:     
            print("-------------------------------------------")
            print("           Starting location :  ")
            print("-------------------------------------------")          # as flight has to start from Lahore, Islamabad or Karachi so no more options are given
            print("1) Lahore")
            print("2) Islamabad")
            print("3) Karachi")
            print("")
            d = int(input("Enter your trip's starting location no. from the above list :  "))   # asking for users starting location
            flag=d
            d = destination_check(d)   # getting the First destination no. through the fn
                   
            des.append(d)  # adding the first location into the list of destinations
        
            print(i+1,")",des[i])
            print("------------------")
    global toDate          # getting the current date,time and day
    global toTime
    global toDay
             
    real_date = toDate  
    real_time = toTime                 # storing the current date,time and day in variables 
    
    real_day =toDay
    trip=[]*50    
    
    for i in range(op-1):  # 
        dx = str(des[i]+"_"+des[i+1])
        y = search_flight(dx)
        f = input("Enter the ID of Flight you want to book : ")  # asking user to enter the ID of flight to book
        trip = book_flight(f,y,1,text,name,phone,email,cnic,age)      #callinf fn to book the flight
        
        toTime=str(trip[2])
        toDate = str(trip[3])    # changing the required time so that the next flight has gap and non collsion with flights
        toDay=str(trip[4])

        total_cost.append(int(trip[0]))   #adding the total cost 
        B.append( trip[1])    # adding the flight into list
        
    for i in range(len(total_cost)):
        v = v + total_cost[i]
    f = open(text,"a+")
    f.write("")
    f.write("\n Total charges  = ")                          # displaying the trip cost in the ticket file
    f.write(str(v))
    f.write("Rs")
    f.write("\n--------------------------------------------------")
    f.close()
   
    trip_list.append( B)  # adding the trip into the list of trips 

    toTime=real_time
    toDate=real_date    #reseting the time , date and day to real 
    toDay=real_day

def cancel_trip():  # Fn to cancel the trip
    print("-------------------------------------------")
    print("              Cancel your trip ")
    print("-------------------------------------------")
    name = input("Enter your Name : ")    # as trips were stored througt names hence asking user to enter the name 
    print("")
    for i in range(len(trip_list)):   #  finding the trip in the list of trips
         if  trip_list[i][0] == name:
             for j in range(len(trip_list[i])):
                 cancel_flight(str(trip_list[i][j]))   # if found cancelling the booking one by one
                 

    print("-------------------------------------------")
    print("     Your Trip is Cancelled Successfully   ")
    print("-------------------------------------------")
                   
        
    
        
def outro():  # fn displaying outro
    print("")
    print("-----------------------------------------------------")
    print("           THANK YOU FOR VISITING PIA  ")
    print("-----------------------------------------------------")
#################################################################
import datetime   

now = datetime.datetime.now()  # getting the current time
D = now.strftime("%A")  #getting the day
if D=='Monday':
    toDay = 'M'
elif D=='Tuesday':
    toDay = 'T'
elif D=='Wednesday':
    toDay = 'W'            # converting the day into programs day list values
elif D=='Thursday':
    toDay = 't'
elif D=='Friday':
    toDay = 'F'
elif D=='Saturday':
    toDay = 'S'
else:
    toDay = 's'
print("-----------------------------------------------------")  
print("  Your Current Time and Date : ",now)   # displaying the current time and date
print("  Your Current Day : ",toDay)           # displaying the current day
print("-----------------------------------------------------")    

T = str(datetime.datetime.now())    # getting the current time 

toTime=str(T[11]+T[12]+T[13]+T[14]+T[15])        # storing the current time in a variable

toDate=str(T[8]+T[9]+"/"+T[5]+T[6])              # storing the current date 

#################################################################
intro()
print("-----------------------------------------------------")
print("        Loading the data ...")
print("-----------------------------------------------------")
##################################################################
trip_list = []*50   # list of trips
##################################################################

Dom=Linkedlist()         # making the domestic flight linked list
Int=Linkedlist()         # making the international flight linked list
A=[]*50
with open('FFF.txt','r') as file:      # opening the file 
    for line in file:    # reading the line
        for word in line.split():  # reading the word
            A.append(word)  # adding the word into the list 
        x = Node_F(A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9])   # making the flight Node
        if A[0]=="Domestic":
            Dom.insert(x)  # adding the flight into list 
        else:
            Int.insert(x)
        A.clear()
#################################################################
temp1D=Dom.head
temp1I=Int.head

while temp1D!=None:
    for i in range(temp1D.Freq):
        day = temp1D.Days[i]
        h = Node_F_F(day)
        temp1D.flights_per_week.insert(h)
           
    temp1D=temp1D.next                                  ## adding flight per week into the list 

while temp1I!=None:
    for i in range(temp1I.Freq):
        day = temp1I.Days[i]
        h = Node_F_F(day)
        temp1I.flights_per_week.insert(h)
    
    temp1I=temp1I.next
#################################################################
simulation_booking()  # calling the fn to add database bookings into the list 

##################################################################
options_display()   # fn displaying the options
op = int(input("Enter the Option:"))    # asking for option
while op!= 0:
    if op==1:
        list_flights()
        options_display()
        op = int(input("Enter the Option:"))
    
    elif op==2:
        flight_info()
        options_display()
        op = int(input("Enter the Option:"))
    
    elif op==3:
        book_flight()
        options_display()
        op = int(input("Enter the Option:"))
     
    elif op==4:
        cancel_flight()
        options_display()
        op = int(input("Enter the Option:"))
        
    elif op==5:
        view_booking()
        options_display()
        op = int(input("Enter the Option:"))
         
    elif op==6:
        search_flight()
        options_display()
        op = int(input("Enter the Option:"))
    
    elif op==7:
        search_booking()
        options_display()
        op = int(input("Enter the Option:"))
      
    elif op==8:
        create_trip()
        options_display()
        op = int(input("Enter the Option:"))
     
    elif op==9:
        cancel_trip()
        options_display()
        op = int(input("Enter the Option:"))
        
outro() # calling outro



#### END

    
