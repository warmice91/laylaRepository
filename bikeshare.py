
import time
import pandas as pd
import numpy as np


# I used the folowing sources
# https://github.com/FaAlwatban/Bikeshare.py/blob/master/Bikeshare.py


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
          city = input("Which city would you like to filter by? new york, chicago or washington?\n")
          city=city.lower()

          if city not in ("new york", "chicago", "washington"):
            print("Sorry, I didn't catch that. Try again.")
            continue
          else:
            break
    while True:
          month = input("Which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
          month = month.lower()
          if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Sorry, I didn't catch that. Try again.")
            continue
          else:
            break
    while True:
          day = input("Are you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")
          day=day.lower()
          if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("Sorry, I didn't catch that. Try again.")
            continue
          else:
            break
    return city, month, day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())



    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month,:]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day,:]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    common_month = df["month"].mode()[0]
    print("Most Common Month:", common_month)
    common_day = df["day_of_week"].mode()[0]
    print("Most Common day:", common_day)
    df['hour'] = df["Start Time"].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most Common Hour:", common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    Commonly_Start_Station = df["Start Station"].value_counts().idxmax()
    print("Most Commonly used start station:", Commonly_Start_Station)
    Commonly_End_Station = df["End Station"].value_counts().idxmax()
    print("Most Commonly used end station:", Commonly_End_Station)
    Combination_Station = df.groupby(["Start Station", "End Station"]).count()
    print('Most Commonly used combination of start station and end station trip:', Combination_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    Total_Travel_Time = sum(df['Trip Duration'])
    print("Total travel time:", Total_Travel_Time/86400, "Days")
    Mean_Travel_Time = df["Trip Duration"].mean()
    print("Mean travel time:", Mean_Travel_Time/60, "Minutes")
    print("\nThis took %s seconds." % (time.time() - start_time))



def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df["User Type"].value_counts()
    gender_types = df["Gender"].value_counts()
    print("Gender Types:", gender_types)
    Earliest_Year = df["Birth Year"].min()
    print("Earliest Year:", Earliest_Year)
    print("\nThis took %s seconds." % (time.time() - start_time))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        counter1=0
        counter2=5
        while True:
          ch = input("Do you want to see raw data type yes or no?\n")
          ch=ch.lower() # conv to lower case
          if ch == "yes":
            print(df.iloc[counter1:counter2])
            counter1=counter1+5
            counter2=counter2+5


          else:
            break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
