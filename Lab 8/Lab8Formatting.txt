#Lab8Formatting.py
# Season Chowdhury
# Lab Section M6
# schowd11@syr.edu

def main():
    # create a 12-element list to contain our answers
    answers = [1]*12
    print(answers)
    #IV1a.

    delta = ""
    alpha = 1234.56789
    beta = 268
    gamma = "october"

    # display alpha in a field of width 15, left justified
    answers[0] = "@{0:<15}@".format(alpha,beta,gamma,delta)

    # display alpha in a field of width 15, centered
    answers[1] = "@{0:^15}@".format(alpha,beta,gamma,delta)

    # display alpha with 20 significant digits
    answers[2] = "20 sig digs: {0:.20}".format(alpha,beta,gamma,delta)

    # display alpha with 4 decimal places
    answers[3] = "4 dec places: {0:.4f}".format(alpha,beta,gamma,delta)

    # display both beta and gamma (in that order)
    # in fields of width 10 that are right justified
    answers[4] = "@{1:>10}@{2:>10}@".format(alpha,beta,gamma,delta)

    # display both gamma and beta (in that order),
    #     in fields of width 5 that are left justified
    answers[5] = "@{2:<5}@{1:<5}@".format(alpha,beta,gamma,delta)

    # display beta in a field of width 9, centered, with all blank
    # spaces replaced by periodsâ€¨
    # Result should be: ...268...â€¨
    answers[6] = "{1:.^9}â€¨".format(alpha,beta,gamma,delta)

    # display alpha in a field of width 14, right justified,
    # with all blank spaces replaced by zeros
    answers[7] = "{0:0>14}".format(alpha,beta,gamma,delta)

    # set up the next 4 so that
    # Â     (1) the decimal points line up with each other

    # Â     (2) 1 decimal place is shown for answers[8]

    # Â     (3) 4 decimal places are shown for answers[9]

    # Â     (4) 3 decimal places are shown for the final two
    #
    # You'll have to play with field widths to line things up.

    answers[8] = "{0:>8.1f}".format(528.7568)
    answers[9] = "{0:>11.4f}".format(-32.17)
    answers[10] = "{0:>10.3f}".format(1.357908642)
    answers[11] = "{0:>10.3f}".format(16326.4)
    ##########################################################
    # display all the answersâ€¨
    i=0
    for i in range(12):
        print("answers[{0}]:\n {1}".format(i,answers[i]))
        i=i+1
    
main()


#Final Output


#[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#answers[0]:
# @1234.56789     @
#answers[1]:
# @  1234.56789   @
#answers[2]:
# 20 sig digs: 1234.567890000000034
#answers[3]:
# 4 dec places: 1234.5679
#answers[4]:
# @       268@   october@
#answers[5]:
# @october@268  @
#answers[6]:
# ...268...â€¨
#answers[7]:
# 00001234.56789
#answers[8]:
#    528.8
#answers[9]:
#    -32.1700
#answers[10]:
#      1.358
#answers[11]:
#  16326.400
#>>> 
