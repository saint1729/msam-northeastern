MY_HEIGHT = 170                                                                                                 # define my height

def height_conv():                                                                                              # function definition
    name = input("Hello! I am Sai. What is your name? ")                                                        # prompting input from user
    print("Nice to meet you %s! " % name)                                                                       # greeting message
    h_ft, h_inch = [int(v) for v in input("You look tall! How tall are you exactly, %s? " % name).split(" ")]   # asking question about height and extracting height in ft and inch
    print("What is that in metric system?")                                                                     # asking conversion question
    h_inch += h_ft * 12                                                                                         # converting ft to inch
    h_cm = round(h_inch * 2.54, 1)                                                                              # converting inch to cm
    diff = round(h_cm - MY_HEIGHT)                                                                              # getting height difference between me and the user
    h_m = int(h_cm / 100)                                                                                       # converting height from cm to m
    h_cm = round(h_cm % 100)                                                                                    # rounding cm
    print("It is %sm %scm" % (h_m, h_cm))                                                                       # printing converted height
    if diff > 10:                                                                                               # checking if height difference is greater than 10
        print("Omg! You are %s cm taller than me!" % diff)                                                      # printing height difference
        ans = input("Do you play basketball? ").lower()                                                         # ask question about basketball
        if ans == "no":                                                                                         # checking if answer is "no"
            print("I definitely would if I was that tall!")                                                     # print reply message for "no"
        elif ans == "yes":                                                                                      # checking if answer is "yes"
            print("You must be the favorite player in your team!")                                              # print reply messge for "yes"
        else:                                                                                                   # default condition
            print("Uhm, what was that? ")                                                                       # print reply for "gibberish" input
    else:                                                                                                       # default condition when diff is less than or equal to 10
        print("Oh the difference is only %s cm" % diff)                                                         # print message for diff less than or equal to 10


if __name__ == "__main__":                                                                                      # main method
    height_conv()                                                                                               # function call
