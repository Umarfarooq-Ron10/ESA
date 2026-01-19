def n(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    num = 7
    if num <= 1:
        print("Not Prime")
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
    n(num)


