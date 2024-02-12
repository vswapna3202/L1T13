## L1T13: Programming with User-defined Functions ##
This program calculates a user's holiday cost, including plane cost,hotel cost, and car rental cost.  
**User Inputs:**  
    - *city_flight:* The city the user will be flying to. The user has option to select from following cities: Paris,London,New York or Milan.  
    - *num_nights:* The number of nights they will be staying at a hotel.  
    - *rental_days:* The number of days that they will be hiring a car for.  
**User-defined functions:**
The program creates the following 4 user-defined functions:  
    - *hotel_cost:* This function will take num_nights as an argument,
    and return a total cost for the hotel stay (You can choose the price
    per night charged at the hotel)  
    - *plane_cost:* This function will take city_flight as an argument
    and return a cost for the flight.  
    - *car_rental:* This function will take rental_days as an argument
    and return the total cost of the car rental (you can choose the daily
    rental cost.)  
    - *holiday_cost:* This function will take the three arguments
    hotel_cost, plane_cost, car_rental. Using these three
    arguments, you can call all three of the above functions with
    respective arguments and finally return a total cost for your
    holiday.

**Output:**
All these details are printed in a similar way to the following example: 
```
Your Total Holiday Cost to PARIS for 3 nights in hotel with car rental for 
3 days is: £1180
```
## Installation
1. **Python**: Ensure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/).
2. **Version**: These programs are written in Python 3. Make sure you have Python 3.x installed.

### Clone the Repository
```bash
git clone https://github.com/vswapna3202/L1T13.git  
```

## Running the programs <br>
Navigate to the directory of each Python file
Run Python using python interpreter
```
python holiday.py

