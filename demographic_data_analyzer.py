import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # print(df.head())

    # cleaning data
    # print(df.info())
    # print(df.isnull().sum())
    df = df.dropna()
    # print("duplicated rows:", df.duplicated().sum())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    race_count = df["race"].value_counts()

    # What is the average age of men?

    average_age_men = round(df[(df["sex"] == "Male")]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (
            (df[df["education"] == "Bachelors"].value_counts().sum())
            * 100
            / (df["education"].value_counts().sum())
        ),
        1,
    )

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_rich = round(
        (
            (
                df[  # people with advanced education and >50K salary
                    (
                        (df["education"] == "Bachelors")
                        | (df["education"] == "Masters")
                        | (df["education"] == "Doctorate")
                    )
                    & (df["salary"] == ">50K")
                ]
                .value_counts()
                .sum()
            )
            * 100
            / (
                df[  # people with advanced education
                    (
                        (df["education"] == "Bachelors")
                        | (df["education"] == "Masters")
                        | (df["education"] == "Doctorate")
                    )
                    & (df["salary"])
                ]
                .value_counts()
                .sum()
            )
        ),
        1,
    )

    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    lower_education_rich = round(
        (
            (
                df[  # people without advanced education and make >50K salary
                    (
                        (df["education"] != "Bachelors")
                        & (df["education"] != "Masters")
                        & (df["education"] != "Doctorate")
                    )
                    & (df["salary"] == ">50K")
                ]
                .value_counts()
                .sum()
            )
            * 100
            / (
                df[  # people without advanced education and not making >50K salary
                    (
                        (df["education"] != "Bachelors")
                        & (df["education"] != "Masters")
                        & (df["education"] != "Doctorate")
                    )
                    & (df["salary"] != "")
                ]
                .value_counts()
                .sum()
            )
        ),
        1,
    )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df["hours-per-week"])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # its 35 hours min per week

    rich_percentage = round(
        (
            (
                df[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")]
                .value_counts()
                .sum()
            )
            * 100
            / (df[(df["hours-per-week"] == 1)].value_counts().sum())
        )
    )

    # What country has the highest percentage of people that earn >50K?

    highest_earning_country = pd.Series(
        round(
            (df[df["salary"] == ">50K"]["native-country"].value_counts())
            * 100
            / (df[df["salary"] != ""]["native-country"].value_counts()),
            1,
        )
    ).idxmax()

    highest_earning_country_percentage = max(
        round(
            (df[df["salary"] == ">50K"]["native-country"].value_counts())
            * 100
            / (df[df["salary"] != ""]["native-country"].value_counts()),
            1,
        )
    )

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
        df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"]
        .value_counts()
        .idxmax()
    )

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
