import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("portfolio_data.json")


def load_portfolio():
    if DATA_FILE.exists():
        with DATA_FILE.open("r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}


def save_portfolio(portfolio):
    with DATA_FILE.open("w") as file:
        json.dump(portfolio, file, indent=2)


def add_stock():
    portfolio = load_portfolio()
    symbol = input("Enter stock symbol: ").upper()
    name = input("Enter company name: ")
    shares = float(input("Enter number of shares: "))
    price = float(input("Enter price per share: "))

    portfolio[symbol] = {
        "name": name,
        "shares": shares,
        "price": price,
    }

    save_portfolio(portfolio)
    print(f"Stock {symbol} added successfully.")


def view_portfolio():
    portfolio = load_portfolio()
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_value = 0.0
    print("\nPortfolio Summary")
    print("-" * 45)
    for symbol, stock in portfolio.items():
        value = stock["shares"] * stock["price"]
        total_value += value
        print(f"{symbol:<8} | {stock['name']:<20} | Shares: {stock['shares']:>6} | Value: ${value:>10.2f}")

    print("-" * 45)
    print(f"Total Portfolio Value: ${total_value:,.2f}")


def remove_stock():
    portfolio = load_portfolio()
    symbol = input("Enter stock symbol to remove: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        save_portfolio(portfolio)
        print(f"{symbol} removed from portfolio.")
    else:
        print("Stock not found.")


def show_menu():
    print("\nPortfolio Tracker")
    print("1. Add stock")
    print("2. View portfolio")
    print("3. Remove stock")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            remove_stock()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
