from datetime import datetime, timedelta
from numpy import sin,cos,tan,arccos,arcsin, floor, pi, deg2rad, rad2deg,round_
from sympy import symbols, Eq, solve

#Använd pandas/numpy räknare istället
from timeit import default_timer as timer

class Solar:

    def __init__(self, irradiation, country, hemisphere, latitude, time):

        self.country = country

        self.hemisphere = hemisphere

        self.latitude = deg2rad(latitude)

        self.time = self.time(time) #4,04-4,5*10-5

        self.irradiation = self.country_irradiance(self.country) #10*-6

        self.declination_angle = self.declination_angle() #6/7*10-6

        self.solar_hour_angle = self.solar_hour_angle()#2-4*10-6

        self.solar_altitude_angle = self.solar_altitude_angle() #10-3!!!

        self.day_length = self.day_length()#10*-3

        self.azimuth = self.azimuth() #10*-3, 0,006

        self.sun_interval = self.sun_interval() #0,5-0,13s

    def time(self, time):
        if time == 0:
            #print('no time given')
            return datetime.now()
        else:
            return datetime.strptime(time, '%Y-%m-%d %H:%M:%S')


    def country_irradiance(self, country):
        return 500


    def solar_hour_angle(self):
        #solar hour angle = hs
        time = self.time.hour
        #time = self.time.time()
        #time = time.replace(microsecond=0,second=0)
        noon = 12
        delta = time - noon

        solar_hour_angle = (15 * delta)

        return deg2rad(solar_hour_angle)


    def declination_angle(self):
        #declination angle = ∂

        tilt = 23.45
        #N = self.time.timetuple().tm_yday
        N = 320
        sin_obj = deg2rad((360/365)*(284+N))
        declination_angle = deg2rad(tilt*sin(sin_obj))

        return declination_angle


    def solar_altitude_angle(self):
        #alfa
        lat = self.latitude
        h = self.solar_hour_angle
        d = self.declination_angle
        sin_angle = sin(lat) * sin(d) + cos(lat) * cos(d) * cos(h)
        altitude_angle = arcsin(sin_angle)

        return altitude_angle


    def day_length(self):
        lat = self.latitude
        d = self.declination_angle
        a = round(2/15,3)
        acos_param = arccos((-tan(deg2rad(lat))*tan(deg2rad(d))))
        acos_param = rad2deg(acos_param)
        day_length = a*acos_param
        hours = floor(day_length)
        minutes = round((day_length-hours)*60)
        #kolla
        return '%s:%s' % (hours, minutes)


    def azimuth(self):
        # Azimuth angle = alfa_s
        # Azimuth is 0 at noon, negative before noon and positive after noon

        try:

            d = self.declination_angle
            h = self.solar_hour_angle
            a = self.solar_altitude_angle

            nom = cos(d)*sin(h)
            denom = cos(a)

            sin_alfa = nom/denom
            azimuth = arcsin(sin_alfa)
            return azimuth

        except TypeError:
            print('Azimuth could not be calculated')
            return None

        #date = 16.12.2022 kl 09:00:00
        #L = 40
        #d = -19,38
        #hs = -45
        #as = -44,3
        #a = 17,32

    def sun_interval(self):
        #solar altitude angle should be 0
        # sunset when cos(h) = -tanL*tan(d)
        # calc right-side
        # alfa
        lat = self.latitude
        d = self.declination_angle

        h = arccos(-(tan(lat) * tan(d)))
        solution = [1,2]
        solution[1] = solution[1] - 2 * pi

        sunrise =  12 - rad2deg(solution[0])/15
        hours = floor(sunrise)
        minutes = (sunrise - hours) * 60
        sunrise = '%s:%s' % (hours, minutes)
        sunset =  12 - rad2deg(solution[1])/15
        hours = floor(sunset)
        minutes = (sunset - hours) * 60
        sunset = '%s:%s' % (hours, minutes)
        return [sunrise,sunset]


    def __repr__(self):
        return "Class calculator object"

    def print(self):
        return print('Info:', 'Country:', self.country,'\n| Hemisphere: ',self.hemisphere,'\n| Latitude: ',
                     rad2deg(self.latitude),'\n| Irradiation: ', self.irradiation,'\n| Time: ',
                     self.time,'\n| Declination angle (d): ',rad2deg(self.declination_angle),'\n| Solar hour angle (h): ',
                     rad2deg(self.solar_hour_angle),'\n| Solar altitude angle (alfa): ', rad2deg(self.solar_altitude_angle),
                     '\n| Azimuth (alfa_s): ', rad2deg(self.azimuth),'\n| Day length: ', self.day_length, '\n| Sunrise & Sunset:', self.sun_interval)

    def result(self):
        return {'country':self.country,
                'hemisphere':self.hemisphere,
                'latitude':rad2deg(self.latitude),
                'irradiation':self.irradiation,
                'time':self.time,
                'declination_angle':rad2deg(self.declination_angle),
                'solar_hour_angle':rad2deg(self.solar_hour_angle),
                'solar_altitude_angle':self.solar_altitude_angle,
                'azimuth_angle':self.azimuth,
                'day_length':self.day_length,
                'sunrise':self.sun_interval[0],
                'sunset':self.sun_interval[1]}

