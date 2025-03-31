import sys

user_input = sys.argv[1]

if user_input == 't2.micro':
    print("We will launch the EC2 Instance for Free Tier!!!")
elif user_input == 't2.medium':
    print("We will launch t2.medium and this will charge you 4 dollars")
elif user_input == 't2.xlarge':
    print("We will launch t2.xlarge and this will charge you 8 dollars")
else:
    print("Invalid input. Please enter valid instance type for t2 instance family!!!")