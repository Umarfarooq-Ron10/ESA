def check_number(num):
    # Check Even or Odd
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    # Check Prime
    if num <= 1:
        print("Not Prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


if __name__ == "__main__":
    num = 7
    check_number(num)

