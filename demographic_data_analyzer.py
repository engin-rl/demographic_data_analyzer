import pandas as pd
import numpy as np

def clean_data(df):
    """
    Args:
      df: DataFrame to clean

    Returns:
      clean dataframe
    """
    df = df.dropna()
    return df
def calculate_demographic_data(df, print_data=True):
    """
    Args:
      df: DataFrame to calculate demographic data
      print_data: Whether to print the data

    Returns:
      data: String with demographic data
    """
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[(df["sex"] == "Male")]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_bachelors = df[df["education"] == "Bachelors"].value_counts().sum()
    total_people = df["education"].value_counts().sum()
    
    percentage_bachelors = round(total_bachelors * 100 / total_people, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    
    # What percentage of people without advanced education make more than 50K?
    higher_education = df[  
                    (
                        (df["education"] == "Bachelors")
                        | (df["education"] == "Masters")
                        | (df["education"] == "Doctorate")
                    )
                ].value_counts().sum()

    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    
    higher_education_and_salary = higher_education& (df["salary"] == ">50K").value_counts().sum()
    lower_education_and_salary = lower_education.loc[lower_education['salary'] == '>50K', 'salary'].count()
    

    higher_education_salary_percentage = round(((higher_education_and_salary) * 100 / (higher_education)),1,)

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
    highest_earning_country = (
        df[df["salary"] == ">50K"]["native-country"].value_counts().idxmax()
    )
    
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
            f"Percentage with higher education that earn >50K: {higher_education_and_salary}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_and_salary}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", higher_education_and_salary)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_and_salary,
        "lower_education_rich": lower_education_and_salary,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
