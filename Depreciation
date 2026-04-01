def main():
    print("=== Asset Depreciation Simulator ===\n")

    # Get inputs
    initial_value = float(input("Enter initial asset value: "))
    depreciation_rate = float(input("Enter annual depreciation rate (as decimal, e.g. 0.1 for 10%): "))
    total_years = int(input("Enter number of years: "))

    # Validate inputs
    if initial_value <= 0:
        print("Error: Initial value must be greater than zero.")
        return
    if not (0 < depreciation_rate < 1):
        print("Error: Depreciation rate must be between 0 and 1.")
        return
    if total_years <= 0:
        print("Error: Number of years must be greater than zero.")
        return

    # Print table header
    print("\n+--------+------------+")
    print("| Year   | Value      |")
    print("+--------+------------+")

    current_value = initial_value
    for year in range(1, total_years + 1):
        current_value = current_value * (1 - depreciation_rate)
        print("| %-6d | %-10.2f |" % (year, current_value))

    print("+--------+------------+")
    print("\nFinal asset value after %d years: %.2f" % (total_years, current_value))


main()
