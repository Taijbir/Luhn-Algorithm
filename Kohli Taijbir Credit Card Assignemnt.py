#Taijbir's Credit Card Validation Assigment


cardNum = str(input("What's Your credit card number? no spaces"))
card =  len(cardNum)
if card < 16:
    print("invalid creditcard length")
elif card > 16:
    print("invalid creditcard lenght")
else:
    print("valid creditcard length ")



#Reverse the order of the digits in the number
revnum = str(cardNum)[::-1]


#Perform a partial sum of the odd digits 
sum1 = int(revnum[0])+ int(revnum[2])+int(revnum[4])+ int(revnum[6])+ int(revnum[8])+ int(revnum[10])+ int(revnum[12])+ int(revnum[14])
sumeven = (int(revnum[1]) * 2)+(int(revnum[3]) * 2)+(int(revnum[5]) * 2)+(int(revnum[7]) * 2)+(int(revnum[9]) * 2)+(int(revnum[11]) * 2)+(int(revnum[13]) * 2)+(int(revnum[15]) * 2)


#Multiply each digit by two and sum the digits
index1 =(int(revnum[1]) * 2)
index3 =(int(revnum[3]) * 2)
index5 =(int(revnum[5]) * 2)
index7 =(int(revnum[7]) * 2)
index9 =(int(revnum[9]) * 2)
index11 =(int(revnum[11]) * 2)
index13 =(int(revnum[13]) * 2)
index15 =(int(revnum[15]) * 2)



#the answer is greater than 9 then add the 2 digits to form partial sums for the even digits
total_1 = 0

if index1 >9:
    sum = 0;
    temp = index1;
    while index1 > 0:
        rem = index1 % 10;
        sum += rem;
        index1 //= 10;
    total_1 = total_1 + sum;
else:
    total_1 = total_1 +index1;
    

if index3 >9:
    sum = 0;
    temp = index3;
    while index3 > 0:
        rem = index3 % 10;
        sum += rem;
        index3 //= 10;
    total_1 = total_1 + sum;
else:
    total_1 = total_1 +index3;



if index5 >9:
    sum = 0;
    temp = index5;
    while index5 > 0:
        rem = index5 % 10;
        sum += rem;
        index5 //= 10;
    total_1 = total_1 +sum;
else:
    total_1 = total_1 +index5;


if index7 >9:
    sum = 0;
    temp = index7;
    while index7 > 0:
        rem = index7 % 10;
        sum += rem;
        index7 //= 10;
    total_1 = total_1 +sum;
else:
    total_1 = total_1 +index7;


if index9 >9:
    sum = 0;
    temp = index9;
    while index9 > 0:
        rem = index9 % 10;
        sum += rem;
        index9 //= 10;
    total_1 = total_1 +sum;
else:
    total_1 = total_1 +index9;


if index11 >9:
    sum = 0;
    temp = index11;
    while index11 > 0:
        rem = index11 % 10;
        sum += rem;
        index11 //= 10;
    total_1 = total_1 +sum;
else:
    total_1 = total_1 +index11;   

if index13 >9:
    sum = 0;
    temp = index13;
    while index13 > 0:
        rem = index13 % 10;
        sum += rem;
        index13 //= 10;
    total_1 = total_1 +sum;
else:
    total_1 = total_1 +index13;


if index15 >9:
    sum = 0;
    temp = index15;
    while index15 > 0:
        rem = index15 % 10;
        sum += rem;
        index15 //= 10;
    total_1 = total_1 +sum;
else:
    total_1 = total_1 +index15;


    
#Sum the partial sums of the even digits to form sum2
sum2 =("index1+index3+index5+index7+index9+index11+index13+index15",total_1)
sum3 = int(total_1) + int(sum1)


#Credit Card is Valid if Modulus is 0
if(sum3) % 10 ==0:
    print("Valid Credit Card Number")
else:
    print("Invalid Credit Card Number")

