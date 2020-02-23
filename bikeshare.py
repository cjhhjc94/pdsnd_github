import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all', 'january', 'feburary', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Select a city from {}, {} or {}:".format(*CITY_DATA.keys())).strip().lower()
        if city in CITY_DATA.keys():
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:

        month = input('month to check:').lower()
        if month not in months:
            print('re-enter month')
            continue
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        weekdays = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        weekday = input('weekday to check:').lower()
        if weekday not in weekdays:
            print('re-enter weekday')
            continue
        break

    print('-'*40)
    return city, month, weekday


def load_data(city, month, weekday):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    months = ['all', 'january', 'feburary', 'march', 'april', 'may', 'june']
    weekdays = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['weekday'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        df = df[ df['month'] == months.index(month) ]
    if weekday != 'all':
        df = df[ df['weekday'] == (weekdays.index(weekday)-1)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df['month'].value_counts().max())
    most_common_month = df['month'].value_counts().max()
    print("most common month is ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].value_counts().max()
    print("most common day is", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts().max()
    print("most common hour is", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("most commonly used start station is ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("most commonly used end station is ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("the most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0], mostcommonstartendstation[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types:\n")

    user_counts = df['User Type'].value_counts()
    print(user_counts)

    # TO DO: Display counts of gender
    print("counts of gender:\n")
    try:
        gender_counts = df['Gender'].value_counts()
        print("Gender:")
        print(gender_counts)
        print()
    except KeyError:
        print("There isn't a [Gender] column in this spreedsheet!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birthyear = df['Birth Year']
        print("Birth Year:")
        print()
        most_common_year = birthyear.value_counts().max()
        print("the most common birth year:", most_common_year)
        most_recent = birthyear.max()
        print("the most recent birth year:", most_recent)
        earliest_year = birthyear.min()
        print("the most earliest birth year:", earliest_year)
    except KeyError:
        print("There isn't a [Birth Year] column in this spreedsheet!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """shows 5 rows of data"""
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1 # use index values for rows

    print_line = lambda char: print(char[0] * 90)

    print('\n    Would you like to see some raw data from the current dataset?')

    while True:
        raw_data = input('      (y or n):  ')
        if raw_data.lower() == 'y':
        # display show_rows number of lines, but display to user as starting from row as 1
        # e.g. if rows_start = 0 and rows_end = 4, display to user as "rows 1 to 5"
            print('\n    Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))

            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows

            print_line('.')
            print('\n    Would you like to see the next {} rows?'.format(show_rows))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
