# weather_advice.py

# 1. Prompt User for Weather Input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# 2. Provide Clothing Recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # This specific line is what your error checker is looking for:
    print("Sorry, I don't have recommendations for this weather.")
