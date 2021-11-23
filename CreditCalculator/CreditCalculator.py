import math


def main():
    principal = int(input("Enter the loan principal: "))
    print("What do you want to calculate?")
    mp = input("type 'p' – for the monthly payment\ntype 'm' – for number of monthly payments")

    if mp == "p":
        month = int(input("enter the number of month\n>"))
        pay = math.ceil(principal/month)
        lastpay = math.ceil(principal - (month - 1)*pay)
        if lastpay != pay:
            print("Your monthly payment was", pay, "and last payment was", lastpay)
        else:
            print("Your monthly payment was", pay)
    elif mp == "m":
        m = int(input("enter the monthly payment"))
        mm = math.ceil(principal//m)
        print("it will take", mm, "month to repay the loan")


if __name__ == '__main__':
    main()
