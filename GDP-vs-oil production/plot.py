import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_file_GDB():
    df = pd.read_csv("data/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4756270.csv", skiprows=4)
    df_world = df[df["Country Name"] == "World"]

    x_year = []
    y_gdb = []
    for i in range(1960, 2022):
        x_year.append(i)
        y_gdb.append(df_world[str(i)].values[0])

    # print(x_year)
    # print(y_gdb)
    return x_year, y_gdb


def load_file_oil_production():
    df = pd.read_csv("data/oil-production-by-country.csv")
    df_world = df[df["Entity"] == "World"]
    print(df_world)

    x_year = []
    y_oil_production = []
    for i in range(1900, 2022):
        x_year.append(i)
        y_oil_production.append(
            df_world[df_world["Year"] == i]["Oil production (TWh)"].values[0]
        )

    # print(x_year)
    # print(y_oil_production)
    return x_year, y_oil_production


def evolution_rate(v: list) -> list:
    rate = []
    for i in range(1, len(v)):
        rate.append((v[i] - v[i - 1]) / v[i - 1] * 100)
    return rate


if __name__ == "__main__":
    x_year, y_gdb = load_file_GDB()
    x_year_oil_production, y_oil_production = load_file_oil_production()

    print((y_gdb[1] / y_gdb[0]))
    evolution_rate(y_gdb)

    fig, ax = plt.subplots()  # figsize=(5, 5)
    ax.margins(0.05)
    plt.plot(
        x_year[1:],
        evolution_rate(y_oil_production[60:]),
        marker="x",
        label="Oil production",
    )
    plt.plot(x_year[1:], evolution_rate(y_gdb), label="GDB", marker="x")
    plt.grid(True, linestyle="--", linewidth=0.1, alpha=0.7)
    plt.legend(loc="best", prop={"size": "large"})
    plt.ylabel("Evolution rate", fontsize="large")
    plt.xlabel("Year", fontsize="large")
    plt.text(1973, 16, "Choc pétrolier 1973", rotation=90, fontsize=5)
    plt.text(1979, 16, "Choc pétrolier 1979", rotation=90, fontsize=5)
    plt.text(2008, 16, "Choc pétrolier 2008 ?", rotation=90, fontsize=5)
    plt.savefig("plots/GDP-vs-oil production.pdf", bbox_inches="tight")
