import sys
from tabulate import tabulate


PURCHASE_PRICE = 0
DOWN_PAYMENT_PERCENT = 0
INITIAL_PRINCIPAL_AMT = 0 #after down payment, if applicable
INTEREST_RATE =  0 #percentage
LOAN_LENGTH = 0 #years



def main():
    global PURCHASE_PRICE
    global DOWN_PAYMENT_PERCENT
    global INITIAL_PRINCIPAL_AMT
    global INTEREST_RATE
    global LOAN_LENGTH
    PURCHASE_PRICE = float(raw_input("Enter purchase price: "))
    DOWN_PAYMENT_PERCENT = float(raw_input("Enter down payment %: "))
    down_payment = PURCHASE_PRICE * (DOWN_PAYMENT_PERCENT/100)
    INTEREST_RATE = float(raw_input("Enter interest rate %: "))
    INTEREST_RATE = INTEREST_RATE/100
    LOAN_LENGTH = int(raw_input("Enter loan length: "))
    INITIAL_PRINCIPAL_AMT = PURCHASE_PRICE - down_payment

    schedule = []
    beginning_balance = INITIAL_PRINCIPAL_AMT
    pmt = calculate_pmt(beginning_balance)
    for i in range(0,LOAN_LENGTH*12):
        new_row = []
        new_row.append(i + 1) #month number
        new_row.append(beginning_balance)
        new_row.append(pmt)
        interest = beginning_balance*(INTEREST_RATE/12)
        new_row.append(interest)
        principal = pmt - interest
        new_row.append(principal)
        ending_balance = beginning_balance - principal
        if i == LOAN_LENGTH*12 - 1:
            ending_balance = 0 #account for maturity
        new_row.append(ending_balance)
        schedule.append(new_row)
        beginning_balance = ending_balance
    #calculate totals
    total_row = []
    total_row.append("TOTAL")
    total_row.append(" ")
    col_totals = [ sum(x) for x in zip(*schedule) ]
    total_row.append(col_totals[2]) #PMT sum
    total_row.append(col_totals[3]) #Interest sum
    total_row.append(col_totals[4]) #Principal sum
    total_row.append(" ")
    schedule.append(total_row)

    headers = ["Month", "Beginning Balance", "PMT", "Interest", "Principal", "Ending Balance"]
    print tabulate(schedule, headers=headers)


def calculate_pmt(present_value):
    numerator = 1 - (1/ ((1+(INTEREST_RATE/12))**(LOAN_LENGTH*12)))
    denominator = INTEREST_RATE/12

    return present_value / (numerator/denominator)

if __name__ == '__main__':
    main()
