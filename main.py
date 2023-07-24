# this is a basic python quiz game

# counters
marks = 0

# questions
q1 = "How long is an Olympic swimming pool (in meters)? "
q2 = "What countries made up the original Axis powers in World War II? "
q3 = "Which country do cities of Perth, Adelade & Brisbane belong to? "
q4 = "What geometric shape is generally used for stop signs? "
q5 = "What is cynophobia?"
q6 = "What does “www” stand for in a website browser? "
q7 = "Who named the Pacific Ocean? "
q8 = "How many languages are written from right to left? "
q9 = "Which countries still have Shilling as currency? "
q10 = "What is the name of the man who launched eBay back in 1995? "


# answers
a1 = "50 meters"
a2 = "germany, italy, japan"
a3 = "australia"
a4 = "octagon"
a5 = "fear of dogs"
a6 = "world wide web"
a7 = "ferdinand magellan"
a8 = "12"
a9 = "kenya, uganda, tanzania, somalia"
a10 = "pierre omidyar"


q_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
a_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

# start of game!

print("welcome to this quiz game! \n")
reply = input("do you want to play? (yes or no) ")

if reply != "yes":
    quit()

print("Great! answer questions and earn points :) good luck! \n")

for i in range(10):
    print("QUESTION {}: ".format(i + 1))
    print(q_list[i])

    answer = input("your answer: ").lower()

    if answer == a_list[i]:
        print("Correct! next question :) \n")
        marks += 1
    else:
        print("incorrect :( the correct answer is {} \n".format(a_list[i]))

print("well done! you have completed the quiz game! \n")
print("your score is {}".format(marks))
print("you got {}% of the questions correct!" .format(marks * 10))




