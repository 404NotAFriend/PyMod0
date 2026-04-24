def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def counter(current, limit):
        if current > limit:
            return
        print(f"Day {current}")
        counter(current + 1, limit)

    counter(1, days)
    print("Harvest time!")
