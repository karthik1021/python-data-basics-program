weight_in_lbs = input("weight_in_lbs =")
weight_in_kgs =int(weight_in_lbs) * 0.45
print(weight_in_kgs);
weight_in_kgs = input("weight_in_kgs =")
weight_in_lbs =int(weight_in_kgs) / 0.45
print(weight_in_lbs);
course = "python"
print(course[1]);

is_hot = True
is_cold = True

if is_hot:
    print("it is a  hot day")
    print("drink plenty of water")

elif is_cold:
    print("it is a cold day")
    print("wear warm clothes")

else:
    print("it is a lovely day");

birth_year = input("birth_year =")
age = 2020 - int(birth_year)
print(age);

has_good_credit = True
has_good_income = False

if has_good_credit and has_good_income:
    print("loan accepted")
else:
    print("loan denied");


name= input("name: ")
secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count<guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print('you won ')
        print(name)
        break
else:
    print("sorry, you Lost!");


