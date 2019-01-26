def prime_num(num):
    #to check if the input number is prime or not

    if num%2==0:
        if num==2:
            return ("it is a prime number")
        else:
            return("not a prime number")
    else:

        for n in range (3,num):

            if num%n == 0:
                return ("not a prime number ")
                break
        else:
            return ("it is a prime number")
    #else:
    #    return ("not a prime number")
a=int(input ("enter a number: "))
b= prime_num(a)
print (b)
