#!/usr/bin/env python3

"""
Helper file for Growing Code.

This file helps you test your exercises easily.
Just run: python3 main.py

How it works:
1. It tries to import your exercise files (like ft_plot_area.py)
2. It calls your functions to test them
3. If there's an error, it tells you what went wrong

Make sure your exercise files are in the same folder as this main.py file!
"""


def test_ft_exercise(exercise_file_name):
    """Modified test function to find files in exX/ subfolders."""
    import sys
    import os
    
    print(f"\n=== Testing {exercise_file_name} ===")

    # Add subdirectories ex0 through ex7 to the system path
    for i in range(8):
        folder = f"ex{i}"
        if os.path.isdir(folder):
            full_path = os.path.abspath(folder)
            if full_path not in sys.path:
                sys.path.append(full_path)

    try:
        # Import the module and get the function [cite: 83]
        ft_module = __import__(exercise_file_name)
        ft_function = getattr(ft_module, exercise_file_name)

        if exercise_file_name == "ft_seed_inventory":
            # Exercise 7 requires specific parameters [cite: 231]
            ft_function("tomato", 15, "packets")
            ft_function("carrot", 8, "grams")
            ft_function("lettuce", 12, "area")
            print("\nTesting unknown unit:")
            ft_function("basil", 5, "unknown")
        else:
            ft_function()

    except ImportError:
        print(f"❌ Error: {exercise_file_name}.py not found in root or subfolders.")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Run main function - this runs when you execute: python3 main.py ."""
    print("🌱 Welcome to Growing Code! 🌱")
    print("This helper will test your exercises for you.")
    print("\nWhich exercise would you like to test?")
    print()
    print("0 - ft_hello_garden     (Say hello to the garden community)")
    print("1 - ft_garden_name      (Display garden name)")
    print("2 - ft_plot_area        (Calculate garden plot area)")
    print("3 - ft_harvest_total    (Add up harvest weights)")
    print("4 - ft_plant_age        (Check if plant is ready)")
    print("5 - ft_water_reminder   (Check if plants need water)")
    print("6 - ft_count_harvest    (Count days to harvest)")
    print("7 - ft_seed_inventory   (Seed inventory with type hints)")
    print("a - test all exercises")
    print()

    choice = input("Enter your choice: ")

    # Test the exercise based on user choice
    if choice == "0":
        test_ft_exercise("ft_hello_garden")
    elif choice == "1":
        test_ft_exercise("ft_garden_name")
    elif choice == "2":
        test_ft_exercise("ft_plot_area")
    elif choice == "3":
        test_ft_exercise("ft_harvest_total")
    elif choice == "4":
        test_ft_exercise("ft_plant_age")
    elif choice == "5":
        test_ft_exercise("ft_water_reminder")
    elif choice == "6":
        test_ft_exercise("ft_count_harvest_iterative")
        test_ft_exercise("ft_count_harvest_recursive")
    elif choice == "7":
        test_ft_exercise("ft_seed_inventory")
    elif choice == "a":
        # Test all exercises one by one
        test_ft_exercise("ft_hello_garden")
        test_ft_exercise("ft_garden_name")
        test_ft_exercise("ft_plot_area")
        test_ft_exercise("ft_harvest_total")
        test_ft_exercise("ft_plant_age")
        test_ft_exercise("ft_water_reminder")
        test_ft_exercise("ft_count_harvest_iterative")
        test_ft_exercise("ft_count_harvest_recursive")
        test_ft_exercise("ft_seed_inventory")
    else:
        print("❌ Invalid choice! Please enter 0, 1, 2, 3, 4, 5, 6, 7, or a")


# This line means: "If someone runs this file directly, call main()"
# You don't need to understand this yet, just know it makes the program start
if __name__ == "__main__":
    main()
