# 1- import random module
import random

# 2- create subject
subjects = [
    "Shah rukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group Of Monkeys",
    "Prime Minister Modi",
    "Auto Riskshaw From Delhi"
] 

actions = [
    "Lanches",
    "Cancels",
    "Dances with",
    "Eats",
    "Declare's War On",
    "Orders",
    "Celebrates"
]
place_or_things = [
      "at red fort",
      "in Mumbai Local Train",
      "a plot of samosa",
      "inside parliament",
      "at ganga ghat",
      "during IPL match",
      "at india gate"
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)
    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo You Want Another Headline? (Yes/No)").strip()
    if user_input == "no":
        break

#print goodbye message
print("\nThanks For using the Fake News Headline Generator, Have a fun day")