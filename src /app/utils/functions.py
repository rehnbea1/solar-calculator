from pandas import Timestamp, to_timedelta, DataFrame
from datetime import datetime
from calculator import Solar


def get_year():

    time = datetime.strptime('2022-12-31 23:00:00', '%Y-%m-%d %H:%M:%S')
    N = time.timetuple().tm_yday
    N = N*24
    year_df = DataFrame({'hour':[n for n in range(N+1)]})

    date_root = datetime.strptime(str(datetime.now()),'%Y-%m-%d %H:%M:%S.%f')
    date_root = datetime.strftime(date_root,format='%Y-01-01 00:00:00')

    year_df['time'] = [Timestamp(date_root) + to_timedelta(year_df['hour'][row], unit='H') for row in year_df['hour']]
    year_df = year_df.set_index('time')

    return year_df

def calculate(row):

    irradiation = 0  # Egal for now, function not yet implemented, hardcoded above
    country = 'Portugal, Lisbon'
    hemisphere = 'N'
    latitude = 40  # Lisbon
    time = '2022-12-16 09:00:00'

    #str(row) # Fill in 0 if no time is given, it will calculate for today

    object = Solar(irradiation,country,hemisphere,latitude,time)
    result = object.result()

    return result

def solar_output(year_df):
    for row in year_df.index:
        var = calculate(row)
    print('done')
    return




def get_solar_table():

    year_df = get_year()
    output = solar_output(year_df)

    return



get_solar_table()