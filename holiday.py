# This program does holiday booking. It allows user to input the destination, number of night they will
# be staying in hotel and also number of days they will rent a car. It adds costs according to the user 
# selection and displays total cost of the holiday to the user

def hotel_cost(num_nights): #Function hotel_cost has one parameter num_nights
    total_hotel_cost = 0    #Set total_hotel_cost as 0
    if (num_nights > 0):
        print("-----------------------------------") #print options for hotel booking
        print("****** HOTEL BOOKING OPTIONS ******")
        print("-----------------------------------")
        print ("1: Cost for 1 night for a double room with garden view is £100 ")
        print ("2: Cost for 1 night for a studio room with is £80 ")
        print ("3: Cost for 1 night for a double room with pool view is £200 ")
        print ("4: Cost for 1 night for a double room with self catering option is £150 ")
        option = input("\nSelect any of the above options: ") #user selects one option 
        if (option == "1"): 
            total_hotel_cost = 100 * num_nights #assuming hotel cost for 1 night as 100
        elif (option == "2"):
            total_hotel_cost = 80 * num_nights #assuming hotel cost for 1 night as 80
        elif (option == "3"):
            total_hotel_cost = 200 * num_nights #assuming hotel cost for 1 night as 200
        elif (option == "4"):
            total_hotel_cost = 150 * num_nights #assuming hotel cost for 1 night as 150
    return(total_hotel_cost) 

def plane_cost(city_flight):
    if city_flight == "Paris":        
        flight_cost = 250              # assuming flight cost for Paris as 250            
    elif city_flight == "London":
        flight_cost = 300              #assuming flight cost for London as 300            
    elif city_flight == "New York":
        flight_cost = 740              #assuming flight cost for New York as 740            
    elif city_flight == "Milan":
        flight_cost = 350              #assuming flight cost for Milan as 350            
    
    print(f"\n Your Flight cost to {city_flight.upper()} is: £{flight_cost}\n")
    return(flight_cost) 

def car_rental(rental_days):
    total_rental_cost = 0   #set total_rental_cost as 0
    if (rental_days > 0):
        print("---------------------------------------")
        print("****** CAR RENTAL BOOKING OPTIONS ******")
        print("---------------------------------------")
        print ("1: 4 seater manual drive Toyota Prius £50") #Show user options for selecting car
        print ("2: 4 seater manual drive Ford Fiesta £55 ")
        print ("3: 4 seater automatic drive BMW i5 £85 ")
        print ("4: 4 seater automatic drive Honda CRV £110 ")
        option = input("\nSelect any of the above options: ")
        if (option == "1"):
            total_rental_cost = rental_days * 50    #assuming rental cost for a day as 50
        elif (option == "2"):
            total_rental_cost = rental_days * 55    #assuming rental cost for a day as 55
        elif (option == "3"):
            total_rental_cost = rental_days * 85    #assuming rental cost for a day as 85
        elif (option == "4"):
            total_rental_cost = rental_days * 110   #assuming rental cost for a day as 110
    return(total_rental_cost)   

def holiday_cost(plane_cost, hotel_cost, car_rental):
    total_holiday_cost = plane_cost + hotel_cost + car_rental    #sum of hotel, flight and car rental cost
    return total_holiday_cost   

while( True ):
    city_flight = input("Please enter your destination city(Paris,London,New York or Milan): ")
    if (city_flight.title() in ("Paris","London","New York","Milan")):
        num_nights = input("Please enter number of nights you are staying: ")
        rental_days = input("Please enter number of days you are hiring a car for: ")
        break
    else:
        city_flight = print("You entered incorrect destination.",end=" ")

#print holiday details and total_holiday_cost
print(f"\nYour Total Holiday Cost to {city_flight.upper()} for {num_nights} nights in hotel with car rental for {rental_days} days is: £"+str(holiday_cost(plane_cost(city_flight.title()),hotel_cost(int(num_nights)),car_rental(int(rental_days)))))
