# Ask the user for the weather (sunny/rainy/cold) and print a clothing recommendation 

def recommend_clothing(weather: str) -> str:
    weather_clean = weather.strip().lower()

    # Check each possible weather and return the matching recommendation.
    if weather_clean == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather_clean == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather_clean == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else: # Handles any unexpected input
        return "Sorry, I don't have recommendations for this weather."

def main():
    user_input = input("What's the weather like today? (sunny/rainy/cold): ")
    recommendation = recommend_clothing(user_input)
    print(recommendation)

if __name__ == "__main__":
    main()
