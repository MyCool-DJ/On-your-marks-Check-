#day13 of 100days of code
print("I am your friendly AI grader Lilly")
test = input("What was the test? ")
print("ok")
points = int(input("and what was the result? "))

if test == "Python" or test == "python" or test == "🐍":
    pYresult = points / 20 * 100
    print("ok, your result was, ", pYresult, "%")
    if pYresult >= 50:
        print("You passed your Python test. Well done you!")
    else:
        print("Better luck next time, you did not pass")
elif test == "JavaScript" or test == "javascript" or test == "🧀":
    jScript = points / 50 * 100
    if points >= 25:
        print("You passed! JavaScript is not easy, so you did well!")
    else:
        print("Sorry you did not pass this time, better luck next time!")
else:
    print(
        "Sorry, I don't seem to have those results in my database just yet. Please check back later."
    )
