import numpy as np
import pandas as pd


def main():
    courses = ["Python Programming", "Data Science", "Web Development", "Machine Learning", "Cloud Computing", "Cyber Security"]
    fees = np.array([18000, 35000, 22000, 40000, 28000, 25000])

    print(f"Average course fee: Rs.{fees.mean():.2f}")
    print(f"Maximum course fee: Rs.{fees.max()}")
    print(f"Minimum course fee: Rs.{fees.min()}")

    df = pd.DataFrame({"Course": courses, "Fee": fees})
    print("\n--- All Course Records ---")
    print(df.to_string(index=False))

    high_fee = df[df["Fee"] > 25000]
    print("\n--- Courses with Fee above Rs.25,000 ---")
    print(high_fee.to_string(index=False))


if __name__ == "__main__":
    main()
