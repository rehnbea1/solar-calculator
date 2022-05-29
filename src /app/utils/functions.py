from pandas import Timestamp, to_timedelta, DataFrame, concat
from datetime import datetime
from calculator import Solar
from numpy import floor


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
    #Input necessary settings here

    #–––––––––––––––––––––––––––––

    irradiation = None #None if no info is given
    country = 'Portugal, Lisbon'
    hemisphere = 'N'
    latitude = 40 # Lisbon
    time = str(row) #None if no time is given

    #–––––––––––––––––––––––––––––

    object = Solar(irradiation,country,hemisphere,latitude,time)
    result = object.result()

    return result


def run_calculator():

    summary_df = get_year()
    list = []
    [list.append(calculate(row)) for row in summary_df.index]

    solar = DataFrame(list)
    solar = solar.set_index('time')
    summary_df = summary_df.join(solar, how='left')

    sunseconds = (summary_df['day_length'].sum())
    sunhours =  sunseconds/3600
    return


run_calculator()