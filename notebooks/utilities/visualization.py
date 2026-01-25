import matplotlib.pyplot as plt

def plot_actual_vs_expected(df, metric, expected, title):
    """
    Plots actual vs expected values for a given metric during trial period.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(
        df["YEARMONTH"].astype(str),
        df[metric],
        marker="o",
        label="Actual",
        linewidth=2
    )

    ax.plot(
        df["YEARMONTH"].astype(str),
        df[expected],
        marker="o",
        linestyle="--",
        label="Expected (No Trial)",
        linewidth=2
    )

    ax.set_title(title)
    ax.set_xlabel("Month")
    ax.set_ylabel(metric.replace("_", " ").title())
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()

def plot_uplift(df, uplift_col, title):
    """
    Plots uplift (Actual - Expected) for a given metric.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        df["YEARMONTH"].astype(str),
        df[uplift_col],
        color=["green" if x > 0 else "red" for x in df[uplift_col]]
    )

    ax.axhline(0, color="black", linewidth=1)
    ax.set_title(title)
    ax.set_xlabel("Month")
    ax.set_ylabel("Uplift")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()

