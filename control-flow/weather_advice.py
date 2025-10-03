# weather_advice.py
# Objective: Utilize conditional statements to guide program execution based on user input.

def get_clothing_recommendation():
    """
    Prompts the user for the current weather (sunny, rainy, or cold)
    and provides clothing recommendations using if/elif/else statements.
    """
    # Prompt User for Weather Input
    weather_input = input("What's the weather like today? (sunny/rainy/cold): ")

    # Normalize the input to lowercase and remove surrounding whitespace
    weather = weather_input.lower().strip()

    # Provide Clothing Recommendations based on weather conditions
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # Handle unexpected input
        print("Sorry, I don't have recommendations for this weather.")

# Execute the main function
if __name__ == "__main__":
    get_clothing_recommendation()
