def ft_count_harvest_recursive():
    days_till_harvest = int(input("Days until harvest: "))

    def count_days(current_day: int):
        if current_day > days_till_harvest:
            return
        print(f"Day {current_day}")
        count_days(current_day + 1)
    if days_till_harvest > 0:
        count_days(1)
    print("Harvest time!")
