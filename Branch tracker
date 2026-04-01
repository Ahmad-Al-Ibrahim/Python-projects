def get_branch_profit(branch_num):
    """Collect product sales for a branch and return total profit."""
    print("\nBranch %d" % branch_num)
    print("-" * 20)

    total_profit = 0
    product = input("Enter product type (or press Enter to finish): ")

    while product != "":
        amount = int(input("  Enter amount sold: "))
        price = float(input("  Enter price per unit: "))
        total_profit += amount * price
        product = input("Enter product type (or press Enter to finish): ")

    return total_profit


def main():
    print("=== Branch Sales & Profit Tracker ===\n")

    # Get and validate number of branches
    branches = int(input("Enter number of branches (minimum 3): "))
    while branches < 3:
        print("Please enter 3 or more branches.")
        branches = int(input("Enter number of branches: "))

    # Collect and display profit per branch
    print("\n--- Entering Sales Data ---")
    results = []
    for branch_num in range(1, branches + 1):
        profit = get_branch_profit(branch_num)
        results.append((branch_num, profit))

    # Summary report
    print("\n=== Profit Summary ===")
    print("+----------+----------------+------------------+")
    print("| Branch   | Total Profit   | Performance      |")
    print("+----------+----------------+------------------+")

    for branch_num, profit in results:
        performance = "Exceptional!" if profit > 300 else "Standard"
        print("| %-8d | %-14.2f | %-16s |" % (branch_num, profit, performance))

    print("+----------+----------------+------------------+")


main()
