import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_file(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


if __name__ == "__main__":
    df = load_file("data/oil-production-by-country.csv")
    df_world = df[df["Entity"] == "World"]
    print(df_world)

    x_year = []
    y_oil_production = []
    for i in range(1900, 2022):
        x_year.append(i)
        y_oil_production.append(
            df_world[df_world["Year"] == i]["Oil production (TWh)"].values[0]
        )

    print(x_year)
    print(y_oil_production)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.margins(0.05)
    plt.plot(x_year, y_oil_production, marker="x")
    plt.legend(loc="best", prop={"size": "large"})
    plt.grid(True, linestyle="--", linewidth=0.1, alpha=0.7)
    plt.ylabel("Oil production world (TWh)", fontsize="large")
    plt.xlabel("Years", fontsize="large")
    plt.savefig("plots/world-oil-production.pdf", bbox_inches="tight")
