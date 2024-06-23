# source https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html
oil_production_tonnes_year = [
    1965,
    1966,
    1967,
    1968,
    1969,
    1970,
    1971,
    1972,
    1973,
    1974,
    1975,
    1976,
    1977,
    1978,
    1979,
    1980,
    1981,
    1982,
    1983,
    1984,
    1985,
    1986,
    1987,
    1988,
    1989,
    1990,
    1991,
    1992,
    1993,
    1994,
    1995,
    1996,
    1997,
    1998,
    1999,
    2000,
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
]

oil_production_tonnes = [
    1567.6,
    1702.2,
    1826.2,
    1992.3,
    2144.5,
    2358.9,
    2493.6,
    2635.4,
    2875.8,
    2882.2,
    2737.6,
    2974.3,
    3078.1,
    3106.1,
    3237.6,
    3091.1,
    2913.0,
    2797.8,
    2762.0,
    2816.2,
    2791.5,
    2929.4,
    2936.2,
    3061.7,
    3098.7,
    3157.9,
    3149.4,
    3195.0,
    3190.5,
    3234.7,
    3279.1,
    3366.4,
    3441.5,
    3528.5,
    3448.5,
    3598.1,
    3598.0,
    3554.6,
    3712.4,
    3898.3,
    3931.6,
    3966.7,
    3958.6,
    4000.5,
    3901.3,
    3979.2,
    4010.0,
    4119.6,
    4126.2,
    4223.3,
    4364.9,
    4379.6,
    4386.4,
    4486.8,
    4477.6,
    4170.9,
    4221.4,
]


oil_consumption_tonnes = [
    1514.3,
    1628.1,
    1745.2,
    1893.3,
    2050.9,
    2233.5,
    2358.1,
    2536.1,
    2741.2,
    2702.4,
    2668.2,
    2839.9,
    2939.0,
    3065.1,
    3111.0,
    2980.3,
    2871.8,
    2778.9,
    2756.9,
    2816.2,
    2812.7,
    2898.7,
    2955.3,
    3051.9,
    3101.3,
    3141.5,
    3139.9,
    3185.7,
    3167.1,
    3235.9,
    3287.7,
    3359.3,
    3450.8,
    3469.6,
    3528.0,
    3568.3,
    3600.5,
    3628.5,
    3711.1,
    3854.2,
    3887.2,
    3928.3,
    3975.8,
    3940.4,
    3856.6,
    3982.0,
    4015.4,
    4074.3,
    4113.5,
    4139.3,
    4219.5,
    4300.3,
    4361.8,
    4420.7,
    4428.8,
    4018.6,
    4245.7,
]


import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_file(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


if __name__ == "__main__":
    # df = load_file("data/oil production/oil-production-by-country.csv")
    # df_world = df[df["Entity"] == "World"]
    # print(df_world)

    # x_year = []
    # y_oil_production = []
    # for i in range(1900, 2022):
    #     x_year.append(i)
    #     y_oil_production.append(
    #         df_world[df_world["Year"] == i]["Oil production (TWh)"].values[0]
    #     )

    # print(x_year)
    # print(y_oil_production)

    diff = []
    for i in range(0, len(oil_production_tonnes)):
        diff.append(oil_production_tonnes[i] - oil_consumption_tonnes[i])

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.margins(0.05)
    # plt.plot(
    #     oil_production_tonnes_year,
    #     oil_production_tonnes,
    #     label="Production",
    #     marker="x",
    # )
    # plt.plot(
    #     oil_production_tonnes_year,
    #     oil_consumption_tonnes,
    #     label="Consumption",
    #     marker="x",
    # )
    plt.plot(
        oil_production_tonnes_year,
        diff,
        marker="x",
    )
    plt.grid(True, linestyle="--", linewidth=0.1, alpha=0.7)
    # plt.ylabel("Oil production world (Tonne)", fontsize="large")
    plt.ylabel(
        "Diff beteewn Oil production and consomation world (Tonne)", fontsize="large"
    )
    plt.xlabel("Years", fontsize="large")
    plt.savefig("plots/world-oil-diff-production-consomation.pdf", bbox_inches="tight")
