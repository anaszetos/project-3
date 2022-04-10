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
    city = input("Please provide the city you would like to see data for (all, chicago, new york city, washington): ")
    city = city.casefold()
    cities = ['all', 'chicago', 'new york city', 'washington']
    while city not in cities:
        city = input("City not valid! Please provide one of the following: all, chicago, new york city, washington : ")
        city = city.casefold()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please provide the month you would like to see data for (all, january, february, ... , june): ")
    month = month.casefold()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month = input("Month not valid! Please provide one of the following: all, january, february, march, april, may, jun : ")
        month = month.casefold()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please provide the day you would like to see data for (all, monday, tuesday, ... , sunday): ")
    day = day.casefold()
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        day = input("Day not valid! Please provide one of the following: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday : ")
        day = day.casefold()

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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


   # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes' :
         print(df.iloc[start_loc:start_loc+5])
         start_loc += 5
         view_data = input("Do you wish to continue?: ").lower()
    

    return df

def time_stats(fulldf):


    
    """Displays statistics on the most frequent times of travel."""
    fulldf['Start Time'] = pd.to_datetime(fulldf['Start Time'])
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # extract hour from Start Time to create new columns (columns for month and day of week already created in load_data())
    fulldf['hour'] = fulldf['Start Time'].dt.hour
    fulldf['month'] = fulldf['Start Time'].dt.month
    fulldf['day_of_week'] = fulldf['Start Time'].dt.weekday_name
    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = fulldf['month'].mode()[0]
    month_name = months[most_common_month - 1]
    print("Most common month is:", month_name.title())


    # TO DO: display the most common day of week
    most_common_day = fulldf['day_of_week'].mode()[0]
    print("Most common day of the week is:", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = fulldf['hour'].mode()[0]
    print(f"Most common start hour is: {most_common_hour}:00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return fulldf

def station_stats(fulldf):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Popular Start Station: ', fulldf['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Popular End Station: ', fulldf['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most Popular Star start station and end station trip: ', fulldf.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(fulldf):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Trip Duration:', fulldf['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Mean Trip Duration:', fulldf['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(fulldf):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = fulldf['User Type'].value_counts()
    print(user_types,'\n')

    # TO DO: Display counts of gender
    if 'Gender' in fulldf.columns:    
        gender = fulldf['Gender'].count()
        print(gender,'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in fulldf.columns:
        print('Earliest year of Birth:', fulldf['Birth Year'].min())
        print('Most Recent year of Birth:', fulldf['Birth Year'].max())
        print('Most Common year of Birth:', fulldf['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        fulldf = load_data(city, 'all', 'all')
        time_stats(fulldf)
        station_stats(fulldf)
        trip_duration_stats(fulldf)
        user_stats(fulldf)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

