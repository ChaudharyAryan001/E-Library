
import pandas as pd
import numpy as np

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print("File is empty")
            return None

        df['Date'] = pd.to_datetime(df['Date'])
        print("Data loaded successfully\n")
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None

def calculation(df):

    most_borrowed = df['Book Title'].mode()[0]

    avg_days = np.mean(df['Borrowing Duration (Days)'])

    busiest_day = df['Date'].dt.day_name().mode()[0]

    return most_borrowed, avg_days, busiest_day

def show_info(df):

    high_book, avg, day = calculation(df)

    print("information")
    print(f"Most Borrowed Book: {high_book}")
    print(f"Average Borrow Time: {round(avg, 2)} days")
    print(f"Busiest Day: {day}")
    print("\n")

file_name = "library_transactions.csv"


data = load_data(file_name)

if data is not None:
    show_info(data)
