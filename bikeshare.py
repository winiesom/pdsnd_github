import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter City: ")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Please enter a valid city")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter Month: ")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Please enter a valid month")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter Day: ")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Please enter a valid day")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze.
        (str) month - name of the month to filter by, or "all" to apply no month filter.
        (str) day - name of the day of week to filter by, or "all" to apply no day filter.
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load file in dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from Start Time to create a new column
    df['month'] = df['Start Time'].dt.month
    
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        
        # filter by month to create new dataframe
        df = df[df['month'] == month]
        
    # extract day from Start Time to create a new column 
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week is: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " "  + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: ", df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("The mean travel time is: ", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types)


    # TO DO: Display counts of gender
    try:
        gender_count = df.groupby(['Gender'])['Gender'].count()
        print(gender_count)
    except:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        most_recent_year_of_birth = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        
        print("The earliest year of birth is: ", earliest_year_of_birth)
        print("The most recent year of birth is: ", most_recent_year_of_birth)
        print("The most common year of birth is: ", most_common_year_of_birth)
    except:
        print('Birth year stats cannot be calculated because birth year does not appear in the dataframe')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    x = 1
    while True:
        raw = input("Enter yes to see some raw data. Enter no to skip")
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x + 5
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
