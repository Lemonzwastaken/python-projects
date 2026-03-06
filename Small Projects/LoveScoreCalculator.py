def calculate_love_score(name1, name2):
    true_total = 0
    love_total = 0
    coombined_name = (name1 + name2).lower()
    for letter in coombined_name:
        if letter in "true":
            true_total += 1
        else:
            pass
    
    for letter in coombined_name:
        if letter in "love":
            love_total += 1
        else:
            pass

    love_score = (true_total*10) + love_total
    print(love_score)

first = input("Please enter the first name: ")
second = input("Please enter the second name: ")
calculate_love_score(first, second)