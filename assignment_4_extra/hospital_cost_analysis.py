import numpy as np
import pandas as pd


def main():
    patients = ["Aarav", "Meera", "Rohan", "Sneha", "Vikram", "Priya"]
    costs = np.array([15000, 32000, 8500, 45000, 21000, 19999])

    print(f"Mean treatment cost: Rs.{costs.mean():.2f}")
    print(f"Maximum treatment cost: Rs.{costs.max()}")
    print(f"Minimum treatment cost: Rs.{costs.min()}")

    df = pd.DataFrame({"Patient": patients, "Treatment Cost": costs})
    print("\n--- All Patient Records ---")
    print(df.to_string(index=False))

    high_cost = df[df["Treatment Cost"] > 20000]
    print("\n--- Patients with Treatment Cost above Rs.20,000 ---")
    print(high_cost.to_string(index=False))


if __name__ == "__main__":
    main()
