import time
import pandas as pd
import numpy as np
import datetime

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
        city = input("Which city would you like to explore? Choose one of the following: Chicago, New York City or Washington \n\n").lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print("I can't recognize the city name! Please choose the city again.")
            
            


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month you would like to check? Choose one of the following:\n All \n January \n February \n March \n April \n May \n June \n\n").lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print("I can't recognize the month.")
            
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day you would like to check? Choose one of the following:\n All \n Sunday \n Monday \n Tuesday \n Wednesday \n Thursday \n Friday \n Saturday \n Sunday\n\n").lower()
        if day in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            break
        else: 
            print("I can't recognize the day")


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    print("\nThe most common month is " + months[common_month])

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nThe most common day is " + common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("\nThe most common hour is " + str(common_hour))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station is " + start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station is " + end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df[['Start Station', 'End Station']].agg(' - '.join, axis = 1)
    popular_route = df['route'].mode()[0]
    
    print("\nThe most frequent combination of start station and end station trip is " + popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("\nTotal travel time is " + str(datetime.timedelta(seconds=int(total_time))))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("\nAverage travel time is " + str(datetime.timedelta(seconds=int(mean_time))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nNumber of users by type: \n"+ str(user_types))
    print('-'*30)
    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print("\nNumber of users by gender: \n" + str(count_gender))
    except KeyError:
        print("\nWe are sorry, but there is no gender data available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print("\nThe earliest birth year is: ", int(earliest_year))
    
        latest_year = df['Birth Year'].max()
        print("\nThe latest birth year is: ", int(latest_year))
    
        most_common_year = df['Birth Year'].mode()[0]
        print("\nThe most common birth year is: ", int(most_common_year))
    except KeyError:
        print("\nWe are sorry, but there is no birth year data available for this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """Displays raw data on bikeshare users."""
    i = 0
    while True:
        raw = input("Would you like to see 5 rows of raw data? Please enter yes or no.").lower()
        if raw != 'yes':
            break
        else:
            print(df.iloc[i:i+5])
            i = i+5

# Function combines all previous created functions
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
