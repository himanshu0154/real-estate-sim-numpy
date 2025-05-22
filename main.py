import numpy as np
np.random.seed(42)
# No of total houses (no of rows)
no_houses = 100
house_names = [
    "Maple Haven", "Oakwood Manor", "Willow Creek", "Sunset Villa", "Pinecone Place",
    "Bluebird Nest", "Redbrick Retreat", "Meadowview", "Silverstone Estate", "Golden Acres",
    "Whispering Pines", "Brookstone Cottage", "Crystal Hollow", "Ivywood Lodge", "Riverbend House",
    "Cedar Grove", "Sunnydale", "Birchview", "Starlight Estate", "Velvet Pines",
    "Highland House", "Emerald Glen", "Jasmine Hill", "Moonlight Manor", "Sapphire Ridge",
    "Foxglove Farm", "Raven's Roost", "Oak Hollow", "Thornfield", "Chestnut Hill",
    "The Homestead", "Lavender Lane", "Blue Horizon", "Rosewood Residence", "Misty Meadows",
    "Hearthstone Villa", "Pebblebrook", "Redwood Retreat", "Cloudberry Cottage", "Sandstone Heights",
    "Buttercup Bungalow", "Shady Oaks", "Crystal Springs", "Fernhill Manor", "Lily Pond Estate",
    "Mossy Ridge", "Stonegate", "Whitetail Hollow", "Starfall Heights", "Timber Trail",
    "Briarwood", "Elmshade", "Windswept Pines", "Magnolia Hollow", "Aspen Rise",
    "Moonridge", "Hollyhock House", "Glacier Point", "Eagle’s Nest", "Violet Valley",
    "Orchard Bluff", "Driftwood Lodge", "Wildflower Way", "Pine Haven", "Morning Mist Manor",
    "Amber Grove", "Sunflower Hill", "Quiet Quarters", "Fox Run Estate", "Ocean Breeze Villa",
    "Hawk’s Peak", "Twilight Terrace", "Rustic Roost", "Hilltop Haven", "Misty Ridge",
    "The Willows", "Stonebridge Cottage", "Breezy Hollow", "Whisperwind", "Daisy Dell",
    "Huckleberry House", "Glowing Embers Lodge", "Serenity Pines", "Blossom Glen", "Windmill Estate",
    "Marigold Manor", "Hidden Hollow", "Sunset Peaks", "Thistlewood", "Winterberry Way",
    "Golden Glen", "Ashwood Lodge", "Springbrook", "Frostfall Retreat", "Larkspur Landing",
    "Snowdrop Haven", "Thunder Ridge", "Sunrise Summit", "Tranquil Trails", "Cloverhill Estate"
]

# Prices of the houses (fist column)
price = np.random.randint(10_00_000, 1_00_00_001, (no_houses, 1))
# Sq_feet of the houses (second column)
sq_feet = np.random.randint(500, 3001, (no_houses, 1))
# no of bedrooms (third column)
bedroom = np.random.randint(1, 6, (no_houses, 1))
# age of house (forth column)
age_of_house = np.random.randint(0, 51, (no_houses, 1))
# House price per sqfeet 
price_per_sqfeet = np.divide(price, sq_feet)

# final array 
house = np.hstack((price, sq_feet, bedroom, age_of_house, np.round(price_per_sqfeet)))
np.set_printoptions(suppress=True)

raised_house = house.copy()
# INFLATION !!
raised_house[:, 0] = raised_house[:, 0] + raised_house[:,0]*0.06

# Renovation cost
renovated_house = raised_house[:, 3] > 20
raised_house[renovated_house, 0] = raised_house[renovated_house, 0] + raised_house[renovated_house, 0]*0.1

# Market crash (random 5 houses lose 20% of their price)
np.random.seed(42)
random_rows = np.random.choice(raised_house.shape[0], size=5, replace=False)
raised_house[random_rows, 0] = raised_house[random_rows,0] - raised_house[random_rows,0]*0.2

def show_info(prompt, column, order):
    try:
        in_range = int(input("Please enter the range of the list: "))
    except ValueError:
        print("please choose a  int value")
    print(prompt)
    sorted_array = np.argsort(raised_house[:,column])[::order]
    index = 1
    for i in sorted_array[:in_range]:
        print(f"{index}. {house_names[i]}\nPrice - {raised_house[i,0]} Rs.\nSqfeet - {raised_house[i,1]} sq.feet",
              f"\nBedrooms - {int(raised_house[i,2])}\nAge - {int(raised_house[i,3])} years\n")
        index = index + 1

# The average price of houses 
def avg_price():
    avg_house_price = np.mean(house[:, 0])
    print(f"The average price of the all the houses is - {avg_house_price}")

# The most expensive house 
def most_expensive():
    show_info("This is the list of most expensive house", 0,-1)

# The most cheapest house
def most_cheapest():
    show_info("This is the list of most cheapest house", 0,1)

# best deal 
def best_deal():
    show_info("This is the list of best deals", 4,1)

# Worst deal 
def worst_deal():
    show_info("This is the list of worst deal", 4,-1)

# Group houses by age (e.g., old, new) and calculate average price per group
def old_house_list():
    try:
        in_range = int(input("Please enter the range of the list: "))
    except ValueError:
        print("Please enter a int value")
    print("This is the list of the most oldest houses available")
    old_house = raised_house[:, 3] > 20
    old_indices = np.where(old_house)[0]
    sorted_array = old_indices[np.argsort(raised_house[old_indices, 3])[::-1]]
    index = 1
    for i in sorted_array[:in_range]:
        print(f"{index}. {house_names[i]}\nPrice - {raised_house[i,0]} Rs.\nSqfeet - {raised_house[i,1]} sq.feet",
              f"\nBedrooms - {int(raised_house[i,2])}\nAge - {(raised_house[i,3])} years\n")
        index = index + 1

def young_house_list():
    try:
        in_range = int(input("Please enter the range of the list: "))
    except ValueError:
        print("Please enter a int value")
    print("This is the list of the most youngest houses available")
    new_house = raised_house[:, 3] <= 20
    young_indices = np.where(new_house)[0]
    sorted_array = young_indices[np.argsort(raised_house[young_indices, 3])[::-1]]
    index = 1
    for i in sorted_array[:in_range]:
        print(f"{index}. {house_names[i]}\nPrice - {raised_house[i,0]} Rs.\nSqfeet - {raised_house[i,1]} sq.feet",
              f"\nBedrooms - {int(raised_house[i,2])}\nAge - {int(raised_house[i,3])} years\n")
        index = index + 1

def show_menu():
    print("Welcome! to Himanshu's Real Estate Agency")
    print("Enter 1 to see the real price of all estates",
          "\nEnter 2 to see the modified price of all estates(after inflation,renovation cost and price crash)"
          ,"\nEnter 3 to see the average price of all the houses",
          "\nEnter 4 to see the list of most expensive house",
          "\nEnter 5 to see the list of most cheapest house",
         "\nEnter 6 to see the list of great deals",
          "\nEnter 7 to see the list of worst deals",
          "\nEnter 8 to see the list of oldest house",
          "\nEnter 9 to see the list of youngest house",
         "\nEnter 10 to see the menu again",
         "\nEnter 11 to leave the agency")
    
def show_houses():
    index = 1
    for i in range(len(house_names)):
        print(f"{index}. {house_names[i]}\nPrice - {house[i,0]} Rs.\nSqfeet - {house[i,1]} sq.feet",
              f"\nBedrooms - {int(house[i,2])}\nAge - {int(house[i,3])} years\n")
        index = index + 1


def show_raised_houses():
    index = 1
    for i in range(len(house_names)):
        print(f"{index}. {house_names[i]}\nPrice - {raised_house[i,0]} Rs.\nSqfeet - {raised_house[i,1]} sq.feet",
              f"\nBedrooms - {int(raised_house[i,2])}\nAge - {int(raised_house[i,3])} years\n")
        index = index + 1

if __name__=="__main__":
    show_menu()
    while True:
        try:
            user = int(input("Please enter the no. from the following: "))
        except ValueError:
            print("Please enter a int value")
        if user == 1:
            show_houses()
        elif user == 2:
            show_raised_houses()
        elif user == 3:
            avg_price()
        elif user == 4:
            most_expensive()
        elif user == 5:
            most_cheapest()
        elif user == 6:
            best_deal()
        elif user == 7:
            worst_deal()
        elif user == 8:
            old_house_list()
        elif user == 9:
            young_house_list()
        elif user == 10:
            show_menu()
        elif user == 11:
            print("Thanks for you precious time, customer")
            print("We hope you have a good time!")
            break
        else:
            print("please choose from above options")
