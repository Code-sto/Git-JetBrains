import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i1", "--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)

args = parser.parse_args()
z = 0
j = 0
for value in vars(args):
    if args.__getattribute__(value):
        z += 1
        if isinstance(args.__getattribute__(value), float) and args.__getattribute__(value) < 0:
            j += 1
if args.interest:
    i = args.interest/1200
Sum = 0
if not args.interest:
    print("Incorrect parameters")
elif args.type not in ["diff", "annuity"]:
    print("Incorrect parameters in type")
elif args.type == 'diff' and args.payment:
    print("Incorrect parameters in payment")
elif z < 4:
    print("Incorrect parameters, not enough")
elif j > 1:
    print("Incorrect parameters --")
elif args.type == "diff" and not args.payment:
    for m in range(1, args.periods + 1):
        D = args.principal / args.periods + i * (args.principal - (args.principal * (m-1))/args.periods)
        Sum += math.ceil(D)
        print(f"Month {m}: payment is {math.ceil(D)}")
        m += 1
    print(f"Overpayment = {round(Sum - args.principal)}")
elif args.type == "annuity" and not args.payment:
    Paiment = args.principal * ((i * (1 + i) ** args.periods)/((1 + i) ** args.periods - 1))
    Overpay = math.ceil(Paiment) * args.periods - args.principal
    print(f"Your annuity payment = {math.ceil(Paiment)}!")
    print(f"Overpayment = {round(Overpay)}")
elif args.type == "annuity" and not args.principal:
    P = args.payment / ((i * (1 + i) ** args.periods)/((1 + i) ** args.periods - 1))
    Principal = math.floor(P)
    Overpay = args.payment * args.periods - Principal
    print(f"Your loan principal = {Principal}")
    print(f"Overpayment = {round(Overpay)}")
elif args.type == "annuity" and not args.periods:
    N = math.log(args.payment/(args.payment - i * args.principal), 1 + i)
    if N % 1 != 0:
        N = math.ceil(N)
        Overpay = args.payment * N - args.principal

    if N // 12 > 1:
        if N % 12 == 0:
            print('It will take ' + str(N // 12) + ' years')
            print(f"Overpayment = {Overpay}")
        elif N % 12 == 1:
            print('It will take ' + str(N // 12) + ' years and ' + str(N % 12) + ' month to repay this loan!')
            print(f"Overpayment = {Overpay}")
        else:
            print('It will take ' + str(N // 12) + 'years and ' + str(N % 12) + 'months to repay this loan!')
            print(f"Overpayment = {Overpay}")


