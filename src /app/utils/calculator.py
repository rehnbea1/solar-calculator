from datetime import datetime
from math import sin,cos,tan, acos, asin, radians,degrees, floor


class Solar_info:

    def __init__(self, irradiation, country, hemisphere, longitude, time):
        self.country = country
        self.hemisphere = hemisphere
        self.longitude = radians(longitude)
        self.time = self.time(time)
        self.irradiation = self.country_irradiance(self.country)

        self.declination_angle = self.declination_angle()
        self.solar_hour_angle = self.solar_hour_angle()
        self.solar_altitude_angle = self.solar_altitude_angle()
        self.day_length = self.day_length()
        self.azimuth = self.azimuth()
        self.sunriseset = self.sunrise_sunset()


    def time(self, time):
        if time == 0:
            return datetime.now()
        else:
            return datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

    def country_irradiance(self, country):
        return 500


    def solar_hour_angle(self):
        time = self.time.hour
        noon = 12
        delta = time - noon

        solar_hour_angle = round(radians(15 * delta),2)
        return solar_hour_angle


    def declination_angle(self):
        tilt = radians(23.45)
        N = self.time.timetuple().tm_yday
        sin_obj = (360/365)*(284+N)

        declination_angle = round(tilt*sin(sin_obj),2)

        return declination_angle


    def solar_altitude_angle(self):
        long = self.longitude
        h = self.solar_hour_angle
        d = self.declination_angle
        sin_angle = sin(long)*sin(d) + cos(long)*cos(d)*cos(h)
        altitude_angle = round(asin(sin_angle),2)
        return altitude_angle


    def day_length(self):
        lon = self.longitude
        d = self.declination_angle
        a = round(2/15,3)
        acos_param= degrees(acos(-tan(lon)*tan(d)))
        day_length = a*acos_param
        hours = floor(day_length)
        minutes = round((day_length-hours)*60)
        return '%s hours and %s minutes' % (hours, minutes)


    def azimuth(self):
        #Azimuth angle is alfa_s
        h = self.solar_hour_angle
        d = self.declination_angle
        nom = cos(d)*sin(h)

        a = self.solar_altitude_angle
        denom = cos(a)

        azimuth = round(asin(nom/denom),2)
        return azimuth

    def __repr__(self):
        return "Class calculator object"

    def print(self):
        return print('Info:', 'Country:', self.country,'| Hemisphere: ',self.hemisphere,'| Longitude: ',
                     self.longitude,'| Irradiation: ', self.irradiation,'| Time: ',
                     self.time,'| Declination angle (d): ',self.declination_angle,'| Solar hour angle (h):  ',
                     self.solar_hour_angle,'| Solar altitude angle (alfa): ', self.solar_altitude_angle,
                     '| Azimuth (alfa_s): ', self.azimuth,'| Day length: ', self.day_length)

    def sunrise_sunset(self):
        lon = self.longitude
        d = self.declination_angle
        acos_obj = -tan(lon)*tan(d)
        hs = degrees(acos(acos_obj))
        return

irradiation    = 500
country        = 'Finland'
hemisphere     = 'N'
longitude      = 40
time           = 0 #Fill in 0 if no time is given
#'2022-06-15 14:00:00'
object = Solar_info(irradiation,country,hemisphere,longitude, time)
object.print()


print('Application works!')