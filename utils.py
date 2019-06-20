import datetime


def _json_encode(obj):
    if isinstance(obj, str):
        return str(obj)
    elif isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError(repr(obj) + " is not JSON serializable")


def format_data(json_data):
    current_date = ''
    dict = {}
    for item in json_data['list']:

        time = item['dt_txt']
        next_date, hour = time.split(' ')

        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            date_format = '{d}/{m}/{y}'.format(**date)
            dict[date_format] = []


        hour = int(hour[:2])

        if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
        else:
            if hour > 12:
                hour -= 12
            meridiem = 'PM'

        temperature = item['main']['temp']
        description = item['weather'][0]['description']
        dict[date_format].append({'hour': '%i:00 %s' % (hour, meridiem),
                                  'Weather_condition': description,
                                  'celcius': '{:.2f}'.format(temperature - 273.15),
                                  'farenheit': '%.2f' % (temperature * 9 / 5 - 459.67)})
    return dict

