import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def w():
    print('Welcome to Bikeshare system')


def info():

    name = input('Enter user name')


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
                    city = input('Enter the name of the city : \n ').lower()
                    if city in ('chicago', 'new york city', 'washington'):
                       break
                    else:
                        print("Invalid input.\n Try again.")
                        continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
                    month = input('Enter the month : \n ').lower()
                    if month in ('all', 'january', 'february', 'march','april','may','june','july','august',
                                'september','october','november','december'):
                       break
                    else:
                        print("Invalid input.\n Try again.")
                        continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
                    day = input('Enter the day : \n ').lower()
                    if day in ('all', 'sunday', 'monday', 'tuesday','wednesday','thursday','friday',
                                'saturday'):
                       break
                    else:
                        print("Invalid input.\n Try again.")
                        continue

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
          months = ['january', 'february', 'march', 'april', 'may', 'june']
          month = months.index(month) + 1
          df = df[df['month'] == month]

    if day != 'all':
            df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month =df['month'].mode()[0]
    print('Most common month: ',common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day: ',common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour: ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station: ',common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most common end station: ',common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = df.groupby(['Start Station','End Station']).count()
    print('Most common combination of start and end station: ',common_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ',total_travel_time/86400,' Days')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Total travel time: ',mean_travel_time/60,' Minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: ',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('Counts of Gender: ',df['Gender'].value_counts())
    except:
        print('There are no Gender informations')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
       earliest= int(df['Birth Year'].min())
       print('The earliest year of birth: ',earliest)
    except KeyError:
        print('There are "no year of birth" informations')
    try:
       most_recent= int(df['Birth Year'].max())
       print('The most recent year of birth: ',most_recent)
    except KeyError:
        print('There are "no year of birth" informations')
    try:
       common_year= int(df['Birth Year'].min())
       print('The most common year of birth: ',common_year)
    except KeyError:
        print('There are "no year of birth" informations')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   #TO Display 5 rows from DataFrame to user
def display_data(df):

          view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
          start_loc = 0
          while view_data == 'yes':
                      print(df.iloc[start_loc:start_loc+5])
                      start_loc += 5
                      view_data = input("Do you wish to continue?: ").lower()
                      if view_data != 'yes':
                                          break

          start_time = time.time()
          print("\nThis took %s seconds." % (time.time() - start_time))
          print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
