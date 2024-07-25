import csv
import math

def classify_rgb(red: int, green: int, blue: int):
    if red == 0 and green == 0 and blue == 0:
        return "black"
    elif red == 255 and green == 255 and blue == 255:
        return "white"
    elif red != 0 and green == 0 and blue == 0:
        if red <= 35:
            return "black"
        else:
            return classify_red(red)+"Red"
    elif red == 0 and green != 0 and blue == 0:
        if green <= 10:
            return "black"
        else:
            return classify_green(green)+"Green"
    elif red == 0 and green == 0 and blue != 0:
        if blue <= 20:
            return "black"
        else:
            return classify_blue(blue)+"Blue"
    else:
        return deeper_classification(red, green, blue)

def classify_red(value: int):
    if value >= 120:
        return "bright"
    else:
        return "dark"
    
def classify_green(value: int):
    if value >= 80:
        return "bright"
    else:
        return "dark"

def classify_blue(value: int):
    if value >= 150:
        return "bright"
    else:
        return "dark"

def deeper_classification(red: int, green: int, blue: int):
    output = ""
    minimum_dist = 1000
    colour_dict = load_data()
    for key, value in colour_dict.items():
        difference = [abs(key[0] - red), abs(key[1] - green), abs(key[2] - blue)]
        euclid_distances = math.sqrt(sum([x**2 for x in difference]))
        if euclid_distances < minimum_dist:
            minimum_dist = euclid_distances
            output = value
    return output
    
def load_data():
    file = open('data.csv', 'r')
    csv_reader = csv.DictReader(file)
    colour_dict = {}
    for row in csv_reader:
        key = (int(row["red"]), int(row["green"]), int(row["blue"]))
        colour_dict[key] = row["colour"]
    return colour_dict

def test_classify_rgb():
    assert classify_rgb(0, 0, 0) == "black"
    assert classify_rgb(255, 255, 255) == "white"
    assert classify_rgb(255, 0, 0) == "bright red"
    assert classify_rgb(0, 255, 0) == "bright green"
    assert classify_rgb(0, 0, 255) == "bright blue"
    assert classify_rgb(50, 0, 0) == "dark red"
    assert classify_rgb(0, 50, 0) == "dark green"
    assert classify_rgb(0, 0, 50) == "dark blue"
    assert classify_rgb(100, 100, 100) == "unknown"
    print("PASSED")

print(classify_rgb(245, 105, 190))
