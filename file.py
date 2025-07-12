# class data: 
#     def __init__(user, id: int, name:str, reason:str):
#         user.id = id
#         user.name = name
#         user.reason = reason
    

#     def displaydetails(user):
#         print("please enter your date of birth by year and month and day")
#         userauth = input("Enter your authentication key: ")
#         if userauth == "02-25-2004":
#             print("congrats! you are eligible to fro learn python programming")
#             print(f"Id: {user.id}, Name: {user.name}, Reason for visit is: {user.reason}")
#         else:
#             print("you are not eligible to learn python programming")
#             print("cause your id is not valid or you have not provided the correct reason for visit")


# Data1: data = data("10", "abdul rehman", "preparing for exams and learning python programming")

# Data1.displaydetails()





class Human:
    def speak(self):
        print("Human: I'm good, thanks!")

class Parrot:
    def speak(self):
        print("Parrot: Polly wants a cracker!")

def have_conversation(person: Human):
    print("\nhave_conversation: Hello, how are you? ", type(person))
    person.speak()


human = Human()
parrot = Parrot()

have_conversation(human)   # I'm good, thanks!
have_conversation(parrot)  # Polly wants a cracker!


