import math


def main():
    principal = int(input("Enter the loan principal: "))
    mp = input(f"""What do you want to calculate?
     type "n" for number of monthly payments,
     type "a" for annuity monthly payment amount,
     type "p" for loan principal,
     type "exit" for exit:\n >""")
    while True:
        if mp == "p":
            p()
        elif mp == "a":
            a(principal)
        elif mp == "n":
            n(principal)
        elif mp == "exit":
            exit()
        else:
            main()


def p():
    annuity = float(input("Enter the annuity payment:\n"))
    periods = int(input("Enter the number of periods:\n"))
    loan_i = float(input("Enter the loan interest:\n"))
    cal = (loan_i * 0.01 / 12)
    num = pow(1 + cal, periods)
    result_p = annuity / ((cal * num) / (num - 1))
    print("Your loan principal =", math.floor(result_p))


def a(principal):
    per = int(input("Enter the number of periods:\n"))
    li = float(input("Enter the loan interest:\n"))
    cal = (li * 0.01 / 12)
    num = pow(1 + cal, per)
    ra = principal * ((cal * num) / (num - 1))
    print("Your monthly payment =", math.ceil(ra))


def n(principal):
    monthly_payment = int(input("enter the monthly payment:"))
    loan_interests = float(input("enter the loan interests"))
    cal = (loan_interests * 0.01 / 12)
    fraction = (monthly_payment / (monthly_payment - cal * principal))
    res_n = math.ceil(math.log(fraction, cal + 1))
    years = res_n / 12
    month = (years - math.floor(years)) * 12
    if math.floor(years) != 0:
        print("It will take", math.floor(years), "years and", math.ceil(month), "months to repay this loan!\n>")
    else:
        print("Your monthly payment =", month)


if __name__ == '__main__':
    main()
