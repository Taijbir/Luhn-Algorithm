cardNum = str(input("What's Your credit card number? no spaces"))
card =  len(cardNum)
if card == 16:
    print("valid creditcard length ")
    revnum = str(cardNum)[::-1]
    pos=0
    sum1=0
    sum2=0
    while pos<16:
        if pos%2==0: # position is even
            sum1+=int(revnum[pos])
        else:
            doubledValue= int(revnum[pos])*2
            if doubledValue>9:
                digitsadded=0
                for digit in str(doubledValue):
                    digitsadded+=int(digit)
                sum2+=digitsadded
            else:
                sum2+=doubledValue
        pos+=1
    total= sum1 +sum2
    if total%10==0:
        print("The card is valid")
    else:
        print ("Invalid card")
else:
    print("Invalid valid creditcard length ")



