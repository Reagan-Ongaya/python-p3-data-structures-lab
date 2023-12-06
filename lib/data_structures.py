spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
spicy_food =[
        {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    }
]

def get_names(spicy_foods):
    return [food['name']for food in spicy_foods]

result = get_names(spicy_foods)
print(result)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get('heat_level', 0) > 5]

result = get_spiciest_foods(spicy_foods)
print(result)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name', 'Unknown')
        cuisine = food.get('cuisine', 'Unknown')
        heat_level = food.get('heat_level', 0)
        
        heat_emojis =  '🌶' * heat_level
        
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
        
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
    return None 

american_food = get_spicy_food_by_cuisine(spicy_foods, "American")
print(american_food)

thai_food = get_spicy_food_by_cuisine(spicy_foods, "Thai")
print(thai_food)

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name', 'Unknown')
        cuisine = food.get('cuisine', 'Unknown')
        heat_level = food.get('heat_level', 0)

        heat_emojis = '🌶' * heat_level

    
        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
            

print_spicy_foods(spicy_foods)            

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get('heat_level', 0) for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)

    if num_spicy_foods == 0:
        return 0  

    return total_heat_level // num_spicy_foods

result = get_average_heat_level(spicy_foods)
print(result)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food = create_spicy_food(spicy_foods, spicy_food)

print(create_spicy_food)
