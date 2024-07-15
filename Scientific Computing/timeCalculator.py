def add_time(start, duration, starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Helper function to calculate the day index
    def get_day_index(day):
        return days_of_week.index(day.capitalize())

    # Helper function to get the new day
    def get_new_day(start_day_index, days_later):
        new_day_index = (start_day_index + days_later) % 7
        return days_of_week[new_day_index]

    # Split start time into components
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM':
        start_hours += 12
    if start_hours == 12 and period == 'AM':
        start_hours = 0
    elif start_hours == 24 and period == 'PM':
        start_hours = 12

    # Split duration into components
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate the new time
    end_minutes = (start_minutes + duration_minutes) % 60
    extra_hours = (start_minutes + duration_minutes) // 60
    end_hours = (start_hours + duration_hours + extra_hours) % 24
    days_later = (start_hours + duration_hours + extra_hours) // 24

    # Determine new period (AM/PM) and convert back to 12-hour format if needed
    if end_hours == 0:
        new_period = 'AM'
        end_hours = 12
    elif end_hours < 12:
        new_period = 'AM'
    elif end_hours == 12:
        new_period = 'PM'
    else:
        new_period = 'PM'
        end_hours -= 12

    # Determine the new day if starting day is given
    if starting_day:
        start_day_index = get_day_index(starting_day)
        new_day = get_new_day(start_day_index, days_later)
        day_part = f', {new_day}'
    else:
        day_part = ''

    # Determine the (n days later) part
    if days_later == 1:
        day_later_part = ' (next day)'
    elif days_later > 1:
        day_later_part = f' ({days_later} days later)'
    else:
        day_later_part = ''

    # Format the new time
    new_time = f'{end_hours}:{end_minutes:02d} {new_period}{day_part}{day_later_part}'
    
    return new_time

# Test the function
print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))  
print(add_time('10:10 PM', '3:30'))  
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))  
