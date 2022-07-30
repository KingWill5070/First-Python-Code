#Harold Williams
#05/17/2022
#Desc: This program will ask for name, age, and display theme


#Define main function
def main():
    #Display intro
    #print statementis for output/display only
    print("Welcome To My First Python Program")
    #An empty print statement makes a blank statement

    #Prompt user for their name
    #An input is for asking a question
    #The difference betweenprint and and input is that print runs and then moves on
    #Input runs and waits for user interaction
    userName = input("Enter your name: ")
    #Prompt user for age
    userAge = input("Enter your age: ")

    #Display name and age to user
    #This style uses commas and arguements, a comma will always make a space
    print("Name:", userName)
    print("Age:", userAge)
    #using concatenation
    print("Hi " + userName + userAge + ".")
    #This way isgoing to use f formatting which is the newest and best practice way
    print(f"Hi {userName} {userAge}.")

    #Display Outro
    print("\n Bye",userName)

    #Call or invoke main function
main()
