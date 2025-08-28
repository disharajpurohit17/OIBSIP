# bmi_calculator.py

def read_float(prompt: str, min_value: float | None = None, max_value: float | None = None) -> float:
    """Read a float from input with basic validation."""
    while True:
        try:
            value = float(input(prompt).strip())
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Try again.")
            
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}. Try again.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g., 70 or 1.75.")

def classify_bmi(bmi: float) -> str:
    """Return BMI category using standard cutoffs."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Calculator ===")
    # Reasonable bounds to avoid typos like 0 height or 10000 kg
    weight = read_float("Enter your weight (kg): ", min_value=10, max_value=500)
    height = read_float("Enter your height (meters): ", min_value=0.5, max_value=2.5)

    bmi = weight / (height ** 2)
    category = classify_bmi(bmi)

    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()

