#5) Take input of age of 3 people by user and determine oldest and youngest among them.


def find_oldest_youngest(age1, age2, age3):
    youngest = min(age1, age2, age3)
    oldest = max(age1, age2, age3)
    return youngest, oldest


age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))


youngest, oldest = find_oldest_youngest(age1, age2, age3)


print("The youngest person is:", youngest)
print("The oldest person is:", oldest)