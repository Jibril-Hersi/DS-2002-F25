
import os, sys
import pandas as pd

def generate_summary(portfolio_file: str) -> None:
    if not os.path.exists(portfolio_file):
        print(f"ERROR: Portfolio file not found: {portfolio_file}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)
    if df.empty:
        print("Portfolio is empty. Nothing to summarize.")
        return

    total = df["card_market_value"].sum()
    if (df["card_market_value"] > 0).any():
        mv = df.loc[df["card_market_value"].idxmax()]
        print(f"Total Portfolio Value: ${total:,.2f}")
        print(f"Most Valuable Card: {mv.get('card_name','?')} ({mv.get('card_id','?')}) - ${mv.get('card_market_value',0):,.2f}")
    else:
        print(f"Total Portfolio Value: ${total:,.2f}")
        print("Most Valuable Card: none found with market price.")

def main(): generate_summary("card_portfolio.csv")
def test(): generate_summary("test_card_portfolio.csv")

if __name__ == "__main__": test()

