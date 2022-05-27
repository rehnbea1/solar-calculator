from datetime import datetime, timedelta
from math import radians,degrees, floor, pi
from sympy import *
from math import sin

class Solar:

    def __init__(self, irradiation, country, hemisphere, latitude, time):
        self.country = country
        self.hemisphere = hemisphere
        self.latitude = latitude
        self.time = self.time(time)
        self.irradiation = self.country_irradiance(self.country)
        self.declination_angle = self.declination_angle()
        self.solar_hour_angle = self.solar_hour_angle()
        self.solar_altitude_angle = self.solar_altitude_angle()
        self.day_length = self.day_length()
        self.azimuth = self.azimuth()
        self.sun_interval = self.sun_interval()


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

        solar_hour_angle = round((15 * delta),2)

        return solar_hour_angle


    def declination_angle(self):
        #declination angle = ∂

        tilt = 23.45
        N = self.time.timetuple().tm_yday
        sin_obj = (360/365)*(284+N)
        d = tilt*sin(radians(sin_obj))
        declination_angle = round(d,2)
        return declination_angle


    def solar_altitude_angle(self):
        #alfa
        lat = radians(self.latitude)
        h = radians(self.solar_hour_angle)
        d = radians(self.declination_angle)
        sin_angle = sin(lat)*sin(d) + cos(lat)*cos(d)*cos(h)
        angle = degrees(asin(sin_angle))
        altitude_angle = round(angle,2)

        return altitude_angle


    def day_length(self):
        lat = radians(self.latitude)
        d = radians(self.declination_angle)
        a = round(2/15,3)
        acos_param = acos(-tan(lat)*tan(d))
        acos_param = degrees(acos_param)
        day_length = a*acos_param
        hours = floor(day_length)
        minutes = round((day_length-hours)*60)

        return '%s:%s' % (hours, minutes)


    def azimuth(self):
        try:
            #Azimuth angle = alfa_s
            #Azimuth is 0 at noon, negative before noon and positive after noon

            d = radians(self.declination_angle)
            h = radians(self.solar_hour_angle)
            a = radians(self.solar_altitude_angle)

            nom = cos(d)*sin(h)
            denom = cos(a)
            sin_alfa = nom/denom
            azimuth = asin(sin_alfa)
            azimuth = degrees(azimuth)
            return azimuth
        except TypeError:
            print('Azimuth could not be calculated')
            return 'Nan'


        #d = -19,38
        #hs = -45
        #as = -44,3
        #a = 17,32

    def sun_interval(self):
        #solar altitude angle should be 0
        # sunset when cos(h) = -tanL*tan(d)
        # calc right-side
        # alfa
        lat = radians(self.latitude)
        h = symbols('h')
        d = radians(self.declination_angle)
        result = -(tan(lat) * tan(d))

        eq1 = Eq(cos(h),-(tan(lat) * tan(d)))
        solution = solve(eq1, h)
        solution[1] = solution[1]-2*pi

        sunrise =  12 - degrees(solution[0])/15
        hours = floor(sunrise)
        minutes = round((sunrise - hours) * 60)
        sunrise = '%s:%s' % (hours, minutes)
        sunset =  12 - degrees(solution[1])/15
        hours = floor(sunset)
        minutes = round((sunset - hours) * 60)
        sunset = '%s:%s' % (hours, minutes)
        return [sunrise,sunset]


    def __repr__(self):
        return "Class calculator object"

    def print(self):
        return print('Info:', 'Country:', self.country,'\n| Hemisphere: ',self.hemisphere,'\n| Latitude: ',
                     self.latitude,'\n| Irradiation: ', self.irradiation,'\n| Time: ',
                     self.time,'\n| Declination angle (d): ',self.declination_angle,'\n| Solar hour angle (h):  ',
                     self.solar_hour_angle,'\n| Solar altitude angle (alfa): ', self.solar_altitude_angle,
                     '\n| Azimuth (alfa_s): ', self.azimuth,'\n| Day length: ', self.day_length, '\n| Sunrise & Sunset:', self.sun_interval)

    def result(self):
        return {'country':self.country,
                'hemisphere':self.hemisphere,
                'latitude':self.latitude,
                'irradiation':self.irradiation,
                'time':self.time,
                'declination_angle':self.declination_angle,
                'solar_hour_angle':self.solar_hour_angle,
                'solar_altitude_angle':self.solar_altitude_angle,
                'azimuth_angle':self.azimuth,
                'day_length':self.day_length,
                'sunrise':self.sun_interval[0],
                'sunset':self.sun_interval[1]}

