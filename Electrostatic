from math import pi

EPSILON = 8.854e-12  # Permittivity of free space (F/m)
ke = 1 / (4 * pi * EPSILON)  # Coulomb's constant


def get_strength_category(magnitude):
    if magnitude > 1000:
        return "Very Strong"
    elif magnitude >= 1:
        return "Moderate"
    else:
        return "Weak"


def main():
    print("=== Electrostatic Force Calculator ===\n")

    # Get and validate distance
    distance = float(input("Enter distance r (in meters): "))
    if distance <= 0:
        print("Error: Distance must be greater than zero.")
        return

    # Get charges
    point1 = float(input("Enter Charge Q1 (in Coulombs): "))
    point2 = float(input("Enter Charge Q2 (in Coulombs): "))

    # Calculate force magnitude using Coulomb's law
    F_magnitude = ke * (abs(point1 * point2) / distance ** 2)

    # Display results
    print("\n--- Results ---")
    print("Force Magnitude : %.2f Newtons" % F_magnitude)
    print("Strength Category : %s" % get_strength_category(F_magnitude))


main()
