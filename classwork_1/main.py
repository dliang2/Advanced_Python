"""
Q1:
    A:
        Create a function that converts miles to kilometers and kilometers to miles.
        You should be able to specify whether you want to do a mile or kilometer conversion.
"""


def convert_metric(unit_value, unit_to_convert_to):
    mile_to_kilometer_conversion = 1.61
    kilometer_to_mile_conversion = 1 / 1.61

    if unit_to_convert_to == 'k':
        return unit_value * mile_to_kilometer_conversion
    else:
        return unit_value * kilometer_to_mile_conversion


"""
    B:
        Create a function that does the same as A but this time with a little tweak:
        Now the user can specify which unit of measurement they enter and the output they want it in, in particular the function should ask the user if they're using feet, meters, miles or kilometers. 
        Additionally the function should ask the user in what unit type they want to return their output.
"""


def convert_metric_input():
    unit_input = input("Which units are you using?")
    unit_value = int(input("How many of those units?"))
    unit_to_convert_to = input("Which units do you want to convert to?")

    conversion_rates = {  # input_to_output_conversion
        "feetmeters": 1 / 3.281,
        "feetmiles": 1 / 5280,
        "feetkilometers": 1 / 3281,
        "metersfeet": 3.281,
        "metersmiles": 1 / 1609,
        "meterskilometers": 1 / 1000,
        "milesfeet": 5280,
        "milesmeters": 1609,
        "mileskilometers": 1.61,
        "kilometersfeet": 3821,
        "kilometersmeters": 1000,
        "kilometersmiles": 1 / 1.61,
    }
    # value * conversion rate of input to output
    return unit_value * conversion_rates[unit_input + unit_to_convert_to]


"""
    C: Create a function that is similar to A except this time it is for Fahrenheit, Celcius and Kelvin. The function should offer all three temperature measures given the temperature and the unit type.
"""


def convert_temp(unit_type, unit_value):
    conversion_rates = {  # [Fahrenheit, Celcius, Kelvin]
        "Fahrenheit": [unit_value, (unit_value - 32) * 5 / 9, (unit_value - 32) * 5 / 9 + 273.15],
        "Celcius": [(unit_value * 9 / 5) + 32, unit_value, unit_value + 273.15],
        "Kelvin": [(unit_value - 273.15) * 9 / 5 + 32, unit_value - 273.15, unit_value],
    }

    return [conversion_rates[unit_type]]


"""
Q2:

    A:
        Create a function that can convert seconds to minutes, hours and days your output should be a combination of all three
"""


def convert_time(seconds):
    days = divmod(seconds, 60 * 60 * 24)
    hours = divmod(days[1], 60 * 60)
    minutes = divmod(hours[1], 60)

    return [days[0], hours[0], minutes[0], minutes[1]]


"""
    B:
        Create a function that given a distance traveled and the amount of time provided (in seconds) gives the average kilometers and the average miles per hour.
"""


def calculate_speed(unit_type, unit_value, seconds):
    hours = seconds / 3600
    mile_to_kilometer_conversion = 1.61
    kilometer_to_mile_conversion = 1 / 1.61

    # [Average Kilometers per Hour, Average Miles per Hour]
    if unit_type == 'k':
        return [unit_value, unit_value * kilometer_to_mile_conversion]
    else:
        return [unit_value * mile_to_kilometer_conversion, unit_value]


"""
    C:
        Create a function that given the amount of time traveled (in seconds) and the average kilometers per hour, returns the total distance traveled
"""


def calculate_distance(seconds, speed):
    hours = seconds / 3600
    return speed * hours


"""
    D: (not required challenge question)
        Create a function that given the velocity of an object in two different times, calculates the acceleration of that object between those two times.
"""

"""
Q3: Running

    Someone told you it's healthy to run and you want to try out this routine for yourself (wow, isn't that just a genius idea!>!)
    Because you're a software developer, you have enough money to live by a warm beachfront (think Long Beach or Collins Avenue in Miami). You want to algorithmically figure out running by steadily increasing your pace and improving the amount of time you can run. 

    However, you can only run for one hour a day...

    A: On the boardwalk
        Running on the boardwalk is pretty easy. To start off you can run 1 mile on the boardwalk in 25 minutes (this is more jogging than running...)

        The more you run, the faster you can run. For every ten miles you run on the boardwalk, your time to run decreases by 2 minutes, until you reach a hard limit of 1 mile per 7 minutes (don't ask me how I know this :D )

        ^^^Given a pace you want to achieve, how many days of running on the boardwalk will it take you to achieve that pace?^^^
"""


def q3a(pace):
    day_count = 0
    mile_count = 0
    counter = 10
    current_pace = 25
    speed = 1 / current_pace
    daily_time = 0

    while pace < current_pace:
        day_count += 1
        while daily_time < 60:
            daily_time += 1
            mile_count += speed

            if mile_count > counter:
                current_pace -= 2
                speed = 1 / current_pace
                counter += 10
        daily_time = 0
    return day_count


"""
    B: On the beach
        Running on the beach is a little more difficult...to start off you can run 1 mile in 40 minutes. However for every 7 miles you run, you'll be able to improve your pace by 3 minutes, until you hit a hard limit of 1 mile per 10 minutes.

        The other problem is that if you run over 3.5 miles on the beach in 4 days, you'll exhaust yourself and you won't be able to run for the 3 following days.

        ^^^Given those constraints and a pace you want to achieve, what is the minimal number of days of running on the beach to achieve the pace you'd like to achieve.
"""

def q3b(pace):
    day_count = 0
    mile_count = 0
    counter = 7
    current_pace = 40
    speed = 1 / current_pace
    daily_time = 0
    daily_mile_count = 0

    while pace < current_pace:
        day_count += 1
        while daily_time < 60 and daily_mile_count + speed <= 0.875:
            daily_time += 1
            daily_mile_count += speed
            mile_count += speed

            if mile_count > counter:
                current_pace -= 3
                speed = 1 / current_pace
                counter += 7
        daily_time = 0
        daily_mile_count = 0
    return day_count

"""
    C: Putting the two together
        Given the constraints in A and B above and a pace, what is the minimal number of days you'll need to achieve your pace?
        Assume that running on the boardwalk can increase your beach running speed by 1.5 minutes for every 10 miles.
        Also assume that running on the beach can increase your boardwalk running speed by 4.5 minutes for every 7 miles.

    D: An array of locations, speeds, constraints and resulting speedups

        You are not required to code this question, but it is something you might see on an interview.
        Given any number of locations, the initial speeds you can run in them, constraints (like in question B) and the ability to run in any of them at any given time, 
            construct an algorithm that produces the optimal combination of those locations and runtimes to give you the best pace you can achieve in a limited time.

        You do not have to code this! But you should think about this, because you may well have to answer a question like this in a timed interview...
"""

if __name__ == "__main__":
    print(convert_metric(20, 'k'))
    print(convert_metric(32.2, "m"))
    print(convert_metric_input())
    print(convert_temp("Fahrenheit", 32))

    print(convert_time(3600*24))
    print(calculate_speed("m", 1, 3600))
    print(calculate_distance(3600, 1))

    print(q3a(7))
    print(q3b(10))
