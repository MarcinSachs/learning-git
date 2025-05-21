shopping = {"Piekarnia": ['Chleb', 'Pączek', 'Bułki'],
            "Warzywniak": ['Marchew', 'Seler', 'Rukola']}
items = 0
for shop in shopping:
    print(
        f"Idę do {shop.upper()}, kupuję tu następujące rzeczy: {[item.upper() for item in shopping[shop]]}")
    items += len(shopping[shop])
print(f"W sumie kupuję {items} produktów.")
print("zmodyfikowano")
print("zmodyfikowano2")
print("zmodyfikowano3")
