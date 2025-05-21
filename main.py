shopping = {"Piekarnia": ['Chleb', 'Pączek', 'Bułki'],
            "Warzywniak": ['Marchew', 'Seler', 'Rukola']}
for shop in shopping:
    print(
        f"Idę do {shop.upper()}, kupuję tu następujące rzeczy: {[item.upper() for item in shopping[shop]]}\n")
