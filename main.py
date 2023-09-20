import csv

MEALS_OF_THE_DAY = ["breakfast", "lunch", "dinner"]


def main():
    # this function's body is where the main program is executed
    printable_file = open("Diary.txt", "w")

    date = input("Date: ")
    printable_file.write(date + ",")

    day = input("Day: ")
    printable_file.write(" " + day + ",")

    hour = input("Hour: ")
    printable_file.write(" " + hour + ".\n\n\n")

    temp = input("¿Did you have breakfast? ")
    if temp == "Yes" or temp == "yes" or temp == "YES":
        #this if statement checks if the user got breakfast or not; if yes, asks the user for what they got for breakfast and stores it in a file.
        description_breakfast = input(f"¿What did you got for breakfast? ")
        printable_file.write("Breakfast:\n" + description_breakfast + "\n\n\n")
    temp = input("¿Did you have lunch? ")
    if temp == "Yes" or temp == "yes" or temp == "YES":
        #this if statement checks if the user got lunch; if yes, it asks the user for what they got for lunch and stores it after what the program saved previously in it.
        description_lunch = input("¿What did you got for lunch? ")
        printable_file.write("Lunch:\n" + description_lunch + "\n\n\n")
    temp = input("¿Did you have dinner? ")
    if temp == "Yes" or temp == "yes" or temp == "YES":
        #this if statement checks if the user got dinner; if yes, it asks the user for what they got for dinner and stores it after what the program saved previously in it.
        description_dinner = input("¿What did you got for dinner? ")
        printable_file.write("Dinner:\n" + description_dinner + "\n\n\n")

    temp = int(
        input("¿How many snacks you got through the day? Place 0 for not having any: ")
    )
    if temp > 0:
        """
        This if statement checks if the user ate snacks throughout the day; if yes, it asks the user for what they got for the respective snack and stores it 
        in the "Snacks" section after what the program saved previously.
        """
        snacks = []
        for i in range(1, temp + 1):
            snacks.append(input(f"¿What did you got for snack {i}? "))
            printable_file.write(f"Snack {i}:\n" + snacks[i - 1] + "\n\n\n")

    emotions = []
    print(
        "Enlist with one word the emotions you got today. For each emotion hit an enter without any spaces before or after the emotion. To end, hit an enter without typing anything. "
    )
    temp = input("Type with one word your emotion: ")
    while temp != "":
        #asks the user an emotion until the emotion enters none or simply an enter
        emotions.append(temp)
        temp = input("Type with one word your emotion: ")
    for i in emotions:
        #asks the user to enter the reason they feel that way and stores it in the same row as the emotion being dealt with
        emotions[emotions.index(i)] = [i, input(f"¿Why you feel {i}? ")]
    emotions.insert(0, ["Emotions", "Reason"])

    first_column = get_first_column(emotions)

    largest_width = get_largest_width(first_column)

    for row in range(len(emotions)):
        #
        if len(emotions[row][0]) == largest_width:
            """
            This first part of the if statement checks if the word at the cell located in the intersection of row (variable aka iterator) and the first column 
            is equally long to the longest word of the first column (aka the model); the model is the basis for the generated space between columns to make an 
            even-looking table. The equally large words to the model and the model will be the minority of one needed space only inserted between the columns 
            of the two-by-two matrix.   
            """
            printable_file.write(" ".join([str(a) for a in emotions[row]]) + "\n")
        elif len(emotions[row][0]) < largest_width:
            printable_file.write(
                generate_spaces(largest_width - len(emotions[row][0])).join(
                    [str(a) for a in emotions[row]]
                )
                + "\n"
            )
    printable_file.write("\n\n")

    final_description = input(
        "Feel free to write anything in this prompt (recommended to discharge yourself): "
    )
    description_chunks = divide_string(final_description)
    printable_file.write("Description:\n")
    for i in description_chunks:
        printable_file.write(i + "\n")
    printable_file.write("\n\n")

    weight = float(input("Give me your weight in kg: "))
    ideal_daily_water = get_ideal_water(weight)
    print(
        "You should drink daily based on your weight: " + str(ideal_daily_water) + " ml"
    )
    printable_file.write("Stats:\n")
    printable_file.write(
        "- You should drink daily based on your weight: "
        + str(ideal_daily_water)
        + " ml"
        + "\n"
    )

    taste_meal_average = get_taste_satisfaction()
    print("Your average of taste satisfaction is: " + str(taste_meal_average))
    printable_file.write(
        "- Your average of taste satisfaction is: " + str(taste_meal_average) + "\n"
    )

    print("Now lets get your emotions score (also known as NEV).")
    print(
        "For NEV, the higher to zero is better, the lower to zero is worse, and zero is neutral."
    )
    nev = get_nev(first_column)
    print("Your Net Emotional Value (NEV) is: " + str(nev))
    printable_file.write("- Your Net Emotional Value (NEV) is: " + str(nev) + "\n")

    print("Now lets get your active metabolic rate (AMR). ")
    age = int(input("Give me your age: "))
    height = int(input("Give me your height in cm: "))
    gender = input('What is your gender (type "f" for female or "m" for male)? ')
    print("Select your activity level:\n")
    print(
        "  - Inactive (user type 1): Never or rarely include physical activity in your day.\n"
    )
    print(
        "  - Somewhat active (user type 2): Include light activity or moderate activity from one to three days per week.\n"
    )
    print(
        "  - Moderately active (user type 3): Include at least 30 minutes of moderate activity most days of the week, or 20 minutes of vigorous activity at least three days a week.\n"
    )
    print("  - Active (user type 4): exercise 6–7 days per week\n")
    print(
        "  - Very active (user type 5): Include large amounts of moderate or vigorous activity in pretty much all days.\n"
    )
    activity_level = int(input("Your choice (1, 2, 3, 4, 5): "))
    amr = get_amr(age, height, weight, gender, activity_level)
    print("Your active metabolic rate (AMR) is: " + str(amr) + "\n")
    printable_file.write("- Your active metabolic rate (AMR) is: " + str(amr) + "\n")

    (
        min_run_1000_cal,
        min_bicycling_1000_cal,
        min_calisthenics_1000_cal,
        min_swimming_1000_cal,
        min_dancing_1000_cal,
        min_run_500_cal,
        min_bicycling_500_cal,
        min_calisthenics_500_cal,
        min_swimming_500_cal,
        min_dancing_500_cal,
        minimum_lose_weight,
        maximum_lose_weight,
        minimum_gain_weight,
        maximum_gain_weight,
    ) = get_calorie_data(amr, weight)
    selection = str(
        input("Do you want to increase (type i) or decrease (type d) weight? ")
    )
    if selection == "i":
        print(
            f"To gain 1 to 2 pounds a week — a rate that experts consider safe — your daily intake of calories should be between {minimum_gain_weight} to {maximum_gain_weight}, respectively."
        )
        printable_file.write(
            f"- To gain 1 to 2 pounds a week — a rate that experts consider safe — your daily intake of calories should be between {minimum_gain_weight} to {maximum_gain_weight}, respectively.\n"
        )
    elif selection == "d":
        selection = input(
            "Do you want to decrease weight by eating less (type s), by doing exercise (type e), or by both (type b)? "
        )
        if selection == "s":
            print(
                f"To lose 1 to 2 pounds a week — a rate that experts consider safe — your daily intake of calories should be between {maximum_lose_weight} to {minimum_lose_weight}, respectively."
            )
            printable_file.write(
                f"- To lose 1 to 2 pounds a week — a rate that experts consider safe — your daily intake of calories should be between {maximum_lose_weight} to {minimum_lose_weight}, respectively.\n"
            )
        elif selection == "e":
            print(
                "To lose two pounds (the maximum recommended by experts) per week you should pick daily and do one of the following: "
            )
            printable_file.write(
                "- To lose two pounds (the maximum recommended by experts) per week you should pick daily and do one of the following:\n"
            )
            print("  - Run: " + str(min_run_1000_cal) + " min.")
            printable_file.write("  - Run: " + str(min_run_1000_cal) + " min.\n")
            print("  - Bicycling: " + str(min_bicycling_1000_cal) + " min.")
            printable_file.write(
                "  - Bicycling: " + str(min_bicycling_1000_cal) + " min.\n"
            )
            print("  - Calisthenics: " + str(min_calisthenics_1000_cal) + " min.")
            printable_file.write(
                "  - Calisthenics: " + str(min_calisthenics_1000_cal) + " min.\n"
            )
            print("  - Swimming: " + str(min_swimming_1000_cal) + " min.")
            printable_file.write(
                "  - Swimming: " + str(min_swimming_1000_cal) + " min.\n"
            )
            print("  - Dancing: " + str(min_dancing_1000_cal) + " min.")
            printable_file.write(
                "  - Dancing: " + str(min_dancing_1000_cal) + " min.\n"
            )

            print(
                "\nTo lose one pound (the minimum recommended by experts) per week you should pick daily and do one of the following: "
            )
            printable_file.write(
                "- To lose one pound (the minimum recommended by experts) per week you should pick daily and do one of the following: "
            )
            print("  - Run: " + str(min_run_500_cal) + " min.")
            printable_file.write("  - Run: " + str(min_run_500_cal) + " min.\n")
            print("  - Bicycling: " + str(min_bicycling_500_cal) + " min.")
            printable_file.write(
                "  - Bicycling: " + str(min_bicycling_500_cal) + " min.\n"
            )
            print("  - Calisthenics: " + str(min_calisthenics_500_cal) + " min.")
            printable_file.write(
                "  - Calisthenics: " + str(min_calisthenics_500_cal) + " min.\n"
            )
            print("  - Swimming: " + str(min_swimming_500_cal) + " min.")
            printable_file.write(
                "  - Swimming: " + str(min_swimming_500_cal) + " min.\n"
            )
            print("  - Dancing: " + str(min_dancing_500_cal) + " min.")
            printable_file.write("  - Dancing: " + str(min_dancing_500_cal) + " min.\n")
            print(
                "\nTo lose between 1 and 2 pounds, do the above criteria ranging their values."
            )
            printable_file.write(
                "\nTo lose between 1 and 2 pounds, do the above criteria ranging their values.\n"
            )
        elif selection == "b":
            print(
                f"To lose one pound a week by cutting calories — a rate that experts consider safe — your daily intake of calories should be {minimum_lose_weight}."
            )
            printable_file.write(
                f"- To lose one pound a week by cutting calories — a rate that experts consider safe — your daily intake of calories should be {minimum_lose_weight}.\n"
            )
            print(
                "\n  To lose one pound (the minimum recommended by experts) per week by exercising you should pick daily and do one of the following: "
            )
            printable_file.write(
                "  To lose one pound (the minimum recommended by experts) per week by exercising you should pick daily and do one of the following: \n"
            )
            print("  - Run: " + str(min_run_500_cal) + " min.")
            printable_file.write("    - Run: " + str(min_run_500_cal) + " min.\n")
            print("  - Bicycling: " + str(min_bicycling_500_cal) + " min.")
            printable_file.write(
                "    - Bicycling: " + str(min_bicycling_500_cal) + " min.\n"
            )
            print("  - Calisthenics: " + str(min_calisthenics_500_cal) + " min.")
            printable_file.write(
                "    - Calisthenics: " + str(min_calisthenics_500_cal) + " min.\n"
            )
            print("  - Swimming: " + str(min_swimming_500_cal) + " min.")
            printable_file.write(
                "    - Swimming: " + str(min_swimming_500_cal) + " min.\n"
            )
            print("  - Dancing: " + str(min_dancing_500_cal) + " min.")
            printable_file.write(
                "    - Dancing: " + str(min_dancing_500_cal) + " min.\n"
            )
            print(
                f"Cutting calories to {minimum_lose_weight} and picking and doing one of the above exercises daily will lead you to lose two pounds per week by an integral combination of both. I hope it helps you! Yay! :)"
            )
            printable_file.write(
                f"  Cutting calories to {minimum_lose_weight} and picking and doing one of the above exercises daily will lead you to lose two pounds per week by an integral combination of both.\n"
            )

    if selection == "i":
        min_carbohydrates_g, min_fat_g, min_proteins_g = get_macronutrients_grams(
            minimum_gain_weight
        )
        max_carbohydrates_g, max_fat_g, max_proteins_g = get_macronutrients_grams(
            maximum_gain_weight
        )
        print(
            f"Because you selected gaining 1 to 2 pounds a week, consume specifically these grams of macronutrients a day: "
        )
        printable_file.write(
            f"- Because you selected gaining 1 to 2 pounds a week, consume specifically these grams of macronutrients a day: \n"
        )
        print(f"  - Carbohydrates: {min_carbohydrates_g} g to {max_carbohydrates_g} g")
        printable_file.write(
            f"  - Carbohydrates: {min_carbohydrates_g} g to {max_carbohydrates_g} g\n"
        )
        print(f"  - Fat: {min_fat_g} g to {max_fat_g} g")
        printable_file.write(f"  - Fat: {min_fat_g} g to {max_fat_g} g\n")
        print(f"  - Proteins: {min_proteins_g} g to {max_proteins_g} g")
        printable_file.write(
            f"  - Proteins: {min_proteins_g} g to {max_proteins_g} g\n"
        )
    elif selection == "s":
        min_carbohydrates_g, min_fat_g, min_proteins_g = get_macronutrients_grams(
            minimum_lose_weight
        )
        max_carbohydrates_g, max_fat_g, max_proteins_g = get_macronutrients_grams(
            maximum_lose_weight
        )
        print(
            f"Because you selected losing 1 to 2 pounds a week solely by excercising, consume specifically these grams of macronutrients a day: "
        )
        printable_file.write(
            f"- Because you selected losing 1 to 2 pounds a week solely by excercising, consume specifically these grams of macronutrients a day: \n"
        )
        print(f"  - Carbohydrates: {min_carbohydrates_g} g to {max_carbohydrates_g} g")
        printable_file.write(
            f"  - Carbohydrates: {min_carbohydrates_g} g to {max_carbohydrates_g} g\n"
        )
        print(f"  - Fat: {min_fat_g} g to {max_fat_g} g")
        printable_file.write(f"  - Fat: {min_fat_g} g to {max_fat_g} g\n")
        print(f"  - Proteins: {min_proteins_g} g to {max_proteins_g} g")
        printable_file.write(
            f"  - Proteins: {min_proteins_g} g to {max_proteins_g} g\n"
        )
    elif selection == "e":
        carbohydrates_g, fat_g, proteins_g = get_macronutrients_grams(amr)
        print(
            f"Because you selected losing 1 to 2 pounds a week solely by excercising, consume specifically these grams of macronutrients a day: "
        )
        printable_file.write(
            f"- Because you selected losing 1 to 2 pounds a week solely by excercising, consume specifically these grams of macronutrients a day: \n"
        )
        print(f"  - Carbohydrates: {carbohydrates_g} g")
        printable_file.write(f"  - Carbohydrates: {carbohydrates_g} g\n")
        print(f"  - Fat: {fat_g} g")
        printable_file.write(f"  - Fat: {fat_g} g\n")
        print(f"  - Proteins: {proteins_g} g")
        printable_file.write(f"  - Proteins: {proteins_g} g\n")
    elif selection == "b":
        carbohydrates_g, fat_g, proteins_g = get_macronutrients_grams(
            minimum_lose_weight
        )
        print(
            f"Because you selected losing one pound a week by cutting calories to {minimum_lose_weight} and losing one pound a week by excercising, consume specifically (ideally) these grams of macronutrients a day: "
        )
        printable_file.write(
            f"- Because you selected losing one pound a week by cutting calories to {minimum_lose_weight} and losing 1 pound a week by excercising, consume specifically these grams of macronutrients a day:  \n"
        )
        print(f"  - Carbohydrates: {carbohydrates_g} g")
        printable_file.write(f"    - Carbohydrates: {carbohydrates_g} g\n")
        print(f"  - Fat: {fat_g} g")
        printable_file.write(f"    - Fat: {fat_g} g\n")
        print(f"  - Proteins: {proteins_g} g")
        printable_file.write(f"    - Proteins: {proteins_g} g\n")

    print(
        "\nDo not worry the information presented to you will be stored in a text file once this program ends. Have a wonderful and lovely day!"
    )

    printable_file.write("\nFor the interpretation of each stat, you shall see README.")
    printable_file.close()


def get_taste_satisfaction():
    # get the average of the scores (from the scale of 0 to 10) of the three meals of the day
    taste_meal_scores = []
    for i in MEALS_OF_THE_DAY:
        taste_meal_scores.append(
            float(input(f"From 0 to 10, ¿How much satisfaction you got with {i}? "))
        )
    taste_meal_average = get_average(taste_meal_scores)
    return taste_meal_average


def get_first_column(matrix):
    """
    This function returns the first column (as a list) of any non-
    empty matrix with this limitations:
     - The matrix must be not empty and the matrix's
      lists or rows must have at least one value or element.
    """
    first_column = []
    for i in range(0, len(matrix)):
        first_column.append(matrix[i][0])
    return first_column


def get_largest_width(column_array):
    """
    Input: non-empty array (i.e., at least one element).
    Output: largest string's length of a given column.

    Note: all array's elements must be able to convert to string.
    """
    largest = -1
    for i in column_array:
        if len(str(i)) > largest:
            largest = len(str(i))
            answer = str(i)
    return len(answer)


def generate_spaces(num):
    # Return a string with n number of spaces.
    string = ""
    for i in range(num + 1):
        string = string + " "
    return string


def divide_string(string):
    # return a list of n-number-character pieces of a given string
    chunks = [(string[i : i + 54]) for i in range(0, len(string), 54)]
    return chunks


def get_average(list):
    """
    Return average of the sum of all the numbers in a list.
    Note: the list's items must be all numbers or at least
    be convertable logically with sense to floats.
    """
    sum_list_items = 0
    for i in range(len(list)):
        sum_list_items = sum_list_items + list[i]
    average = (sum_list_items) / len(list)
    return average


def get_ideal_water(weight):
    # return the ideal intake of water a person should have based upon their weight
    ideal_intake = 30 * weight
    return ideal_intake


def get_nev(emotions_list):
    """
    Input: a list of emotions of type string.
    Output: Net Emotional Value (NEV) of type integer.
    Note: the function ignores all neutral values in the .csv file
    and any non-existent ones in the .csv file. To understand what
    is NEV, please refer to the repository's README which is the host
    of this program.
    """
    emotional_count = 0
    for i in emotions_list:
        with open("nev_emotions_benchmark.csv", "r") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                if i == line[0]:
                    emotional_count = emotional_count + 1
                    break
                elif i == line[2]:
                    emotional_count = emotional_count - 1
                    break
    return emotional_count


def get_amr(age, height, weight, gender, activity_level):
    """
    INPUT: age (int), height (cm), weight (kg), gender ("f" or "m"), and
    activity_level (int).
    OUTPUT: calories per day needed to maintain current weight.
    Note: to understand what is NEV, please refer to the repository's README which
    is the host of this program.
    """
    if gender == "f":
        BMR = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
    elif gender == "m":
        BMR = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)

    if activity_level == 1:
        AMR = BMR * 1.2
    elif activity_level == 2:
        AMR = BMR * 1.375
    elif activity_level == 3:
        AMR = BMR * 1.55
    elif activity_level == 4:
        AMR = BMR * 1.725
    elif activity_level == 5:
        AMR = BMR * 1.9

    return AMR


def get_calorie_data(amr, weight):
    # return multiple variables with the data to recommend in a tailored way how many calories the user should consume daily and/or the exercise the user needs to do.
    RUN_MIN_CAL = 0.0175 * 8 * weight
    BICYCLING_MIN_CAL = 0.0175 * 4 * weight
    CALISTHENICS_MIN_CAL = 0.0175 * 4.5 * weight
    SWIMMING_MIN_CAL = 0.0175 * 8 * weight
    DANCING_MIN_CAL = 0.0175 * 5 * weight

    min_run_1000_cal = 1000 / RUN_MIN_CAL
    min_bicycling_1000_cal = 1000 / BICYCLING_MIN_CAL
    min_calisthenics_1000_cal = 1000 / CALISTHENICS_MIN_CAL
    min_swimming_1000_cal = 1000 / SWIMMING_MIN_CAL
    min_dancing_1000_cal = 1000 / DANCING_MIN_CAL

    min_run_500_cal = 500 / RUN_MIN_CAL
    min_bicycling_500_cal = 500 / BICYCLING_MIN_CAL
    min_calisthenics_500_cal = 500 / CALISTHENICS_MIN_CAL
    min_swimming_500_cal = 500 / SWIMMING_MIN_CAL
    min_dancing_500_cal = 500 / DANCING_MIN_CAL

    minimum_lose_weight = amr - 500
    maximum_lose_weight = amr - 1000

    minimum_gain_weight = amr + 500
    maximum_gain_weight = amr + 1000

    return (
        min_run_1000_cal,
        min_bicycling_1000_cal,
        min_calisthenics_1000_cal,
        min_swimming_1000_cal,
        min_dancing_1000_cal,
        min_run_500_cal,
        min_bicycling_500_cal,
        min_calisthenics_500_cal,
        min_swimming_500_cal,
        min_dancing_500_cal,
        minimum_lose_weight,
        maximum_lose_weight,
        minimum_gain_weight,
        maximum_gain_weight,
    )


def get_macronutrients_grams(calorie_target):
    # return the grams of macronutrients needed to consume per day to accomplish your calorie target
    PERCENTAGE_CARBOHYDRATES = 0.55
    PORCENTAGE_FAT = 0.30
    PORCENTAGE_PROTEINS = 0.15

    carbohydrates_g = (calorie_target * PERCENTAGE_CARBOHYDRATES) / 4
    fat_g = (calorie_target * PORCENTAGE_FAT) / 9
    proteins_g = (calorie_target * PORCENTAGE_PROTEINS) / 4

    return carbohydrates_g, fat_g, proteins_g


main()
