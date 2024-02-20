# voting program
def calculate_age(age):
    # Check if the radius is non-negative
    if age < 0:
        return "Error: age cannot be negative."
age = int(input("enter your age: "))

print("Select your country.")
print("1.Kenya")
print("2.Uganda")
print("3.Tanzania")
choice = input("Enter choice(1/2/3): ")

if age >= 18 :
        print("Elegible to vote")

else:
        print("invalid voter")
