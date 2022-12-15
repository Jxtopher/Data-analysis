import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_file(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, skiprows=4)


if __name__ == "__main__":
    df = load_file("data/CO2 emissions/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_4756074.csv")
    df_world = df[df["Country Name"] == "World"]

    x_year = []
    y_gdb = []
    for i in range(1990, 2022):
        x_year.append(i)
        y_gdb.append(df_world[str(i)].values[0])

    print(x_year)
    print(y_gdb)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.margins(0.05)
    plt.plot(x_year, y_gdb, marker="x")
    plt.grid(True, linestyle="--", linewidth=0.1, alpha=0.7)
    plt.ylabel("CO2 emissions (kt)", fontsize="large")
    plt.xlabel("Years", fontsize="large")
    plt.savefig("plots/world-CO2-emissions.pdf", bbox_inches="tight")
