import datetime
import calendar


def _json_encode(obj):
    if isinstance(obj, str):
        return str(obj)
    elif isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError(repr(obj) + " is not JSON serializable")


def format_data(json_data):
    for item in json_data['list']:

        time = item['dt_txt']
        next_date, hour = time.split(' ')

        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            print('\n{m}/{d}/{y}'.format(**date))

        hour = int(hour[:2])

        if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
        else:
            if hour > 12:
                hour -= 12
            meridiem = 'PM'

        print('\n%i:00 %s' % (hour, meridiem))

        temperature = item['main']['temp']

        description = item['weather'][0]['description'],

        print('Weather condition: %s' % description)
        print('Celcius: {:.2f}'.format(temperature - 273.15))
        print('Farenheit: %.2f' % (temperature * 9 / 5 - 459.67))

    calend = calendar.month(int(year), int(month))
    print('\n' + calend)
