# weather_advice.py

# This script demonstrates the use of if, elif, and else statements 
# to provide clothing recommendations based on user-provided weather conditions.

def provide_weather_advice():
    """
    Prompts the user for the current weather and prints a clothing recommendation 
    based on conditional logic.
    """
    
    # 1. Prompt User for Weather Input
    # Convert input to lowercase to ensure case-insensitive checking (e.g., 'Sunny' becomes 'sunny')
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    recommendation = ""

    # 2. Provide Clothing Recommendations using if-elif-else statements

    # Check for 'sunny'
    if weather == "sunny":
        recommendation = "Wear a t-shirt and sunglasses."
    
    # Check for 'rainy'
    elif weather == "rainy":
        recommendation = "Don't forget your umbrella and a raincoat."
        
    # Check for 'cold'
    elif weather == "cold":
        recommendation = "Make sure to wear a warm coat and a scarf."
        
    # 3. Handle unexpected input using the else statement
    else:
        recommendation = "Sorry, I don't have recommendations for this weather."
        
    # Output the recommendation
    print(recommendation)

# Execute the function
if __name__ == "__main__":
    provide_weather_advice()
