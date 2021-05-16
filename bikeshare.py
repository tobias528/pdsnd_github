import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
       Asks user to specify a city, month, and day to analyze.

       Returns:
           (str) city - name of the city to analyze
           (str) month - name of the month to filter by, or "all" to apply no month filter
           (str) day - name of the day of week to filter by, or "all" to apply no day filter
       """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    available_cities = ["washington", "chicago", "new york city"]

    city = input("Do you want to see data from Chicago, Washington or New York City? ")

    while str.lower(city) not in available_cities:
        print("""Please select one of the following cities: 
                    chicago
                    new york city
                    washington""")
        city = input("Please tell us a city you want to discover: ")

    # TO DO: get user input for month (all, january, february, ... , june)
    available_months = ["january", "february", "march", "april", "may", "june", "all"]

    month = input("Please select a month between january and june or type all for no filter: ")

    while str.lower(month) not in available_months:
        print("""Please select one of the following month:
           january, february, march, april, may, june, all   
           """)
        month = input("Please select a month between january and june or type all for no filter: ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    available_days = ["monday", "thuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

    day = input("Please select a day of the week or type all for no filter: ")

    while str.lower(day) not in available_days:
        print("""Please select one of the following days:
           monday, thuesday, wednesday, thursday, friday, saturday, sunday, all""")
        day = input("Please select a day of the week or type all for no filter: ")

    print(f"""You selected: 
                 city: {city}
                 month: {month}
                 day: {day}""")
    print('-' * 40)
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
    df["hour"] = df["Start Time"].dt.hour

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
    common_month = df['month'].mode()[0]
    print('The most common month is:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is:', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode().values[0]
    print(f"The most frequently used used start station is: \n {start_station} \n")

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode().values[0]
    print(f"The most frequently used end station is: \n {end_station} \n")

    # TO DO: display most frequent combination of start station and end station trip
    most_popular_route = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(f"Most people used the following route: \n {most_popular_route}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_duration = df['Trip Duration'].sum()
    print(f"The total trip duration is: {travel_duration}")

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print(f"The average trip duration is: {avg_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users = df['User Type'].value_counts()
    print(f"""The number for each user type ist: 
          {count_users}""")

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        count_genders = df['Gender'].value_counts()
        print(f"\nThe gender counts are: {count_genders}")
        if 'Birth Year' != 'NaN':
            common_year = df['Birth Year'].mode()[0]
            print(f"The most common birth year ist: {common_year}")
            earliest_year = df['Birth Year'].min()
            print(f"The earliest year of birth is: {earliest_year}")
            recent_year = df['Birth Year'].max()
            print(f"The most recent year of birth is: {recent_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_datalines(df):
    """Show 5 rows of data at user\'s request"""
    print("Type yes to see raw data, type no to skip")
    lines_count = 0
    see_raw_data = ["yes", "no"]
    selection = input().lower()
    while selection not in see_raw_data:
        print("Type yes to see raw data, type no to skip")
        selection = input().lower()

    while selection == "yes":
        lines_count += 5
        print(df.head(lines_count))
        print("Type yes to see more raw data, type no to skip")
        selection = input().lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_datalines(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
