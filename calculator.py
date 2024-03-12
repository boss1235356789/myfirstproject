# Program to calculate the total cost of a new vehicle purchase over 5 years with 15% interest rate
 
def calculate_total_cost(price, years, interest_rate):
    total_interest = price * interest_rate * years
    total_cost = price + total_interest
    return total_cost
 
def main():
    # Vehicle purchase details
    vehicle_price = 180000.00
    purchase_years = 5
    interest_rate = 0.15
 
    # Calculate total cost
    total_cost = calculate_total_cost(vehicle_price, purchase_years, interest_rate)
 
    # Print total cost
    print("Total cost of the vehicle over 5 years with 15% interest rate:", total_cost)
 
if __name__ == "__main__":
    main()