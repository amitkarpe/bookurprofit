# Buy-token.py
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python Buy-token.py <investment token> <buy token> <buying amount with decimal>")
        sys.exit(1)

    investment_token = sys.argv[1]
    buy_token = sys.argv[2]
    buying_amount = float(sys.argv[3])

    print("Investment Token:", investment_token)
    print("Investment Token Type:", type(investment_token).__name__)
    
    print("Buy Token:", buy_token)
    print("Buy Token Type:", type(buy_token).__name__)

    print("Buying Amount:", buying_amount)
    print("Buying Amount Type:", type(buying_amount).__name__)

if __name__ == "__main__":
    main()
