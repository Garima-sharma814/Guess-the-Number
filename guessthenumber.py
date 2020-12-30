# guess the number
guess = 10
n = 68
while(guess <= 10):
    print("number of guesses left:- ", guess)
    i = int(input("enter the number "))
    if i > n:
        print("WRONG! \n your no. is greater than the actual number\n")
        guess -= 1
    if i < n:
        print("WRONG! \n your no. is less than the actual number\n")
        guess -= 1
    if i == n:
        print("Yea !! \n quiet smart huh \n you won ")
        break
    if guess == 0:
        print("game over \n you lose")
        break
