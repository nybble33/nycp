#!/usr/bin/python3

import datetime

class nDateTime:
    '''
    Classs for manilputlating with date and time

    nDateTime(dateTimeString, formatString) - creating standart datetime object
        using formatString wich is dd/mm/YYYY hh:mm:ss by default
    nDateTime object have properties to every part of date and time. They can be
        read and set.
    '''
    def __init__(self, _datetime_string, _format_string='%d/%m/%Y %H:%M:%S'):
        self.__date = datetime.datetime.strptime(_datetime_string, _format_string)
        self.__format_string = _format_string
        self.__year = self.__date.strftime('%Y')
        self.__month = self.__date.strftime('%m')
        self.__day = self.__date.strftime('%d')
        self.__hour = self.__date.strftime('%H')
        self.__min = self.__date.strftime('%M')
        self.__sec = self.__date.strftime('%S')
        print(f'Seconds: {self.__sec}')

    def __update__(self):
        self.__date = datetime.datetime.strptime(
            ' '.join((
                f'{self.__day}/{self.__month}/{self.__year}',
                f'{self.__hour}:{self.__min}:{self.__sec}')),
            self.__format_string
            )

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, _year):
        self.__year = str(_year)
        self.__update__()

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, _month):
        self.__month = str(_month)
        self.__update__()

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, _day):
        self.__day = str(_day)
        self.__update__()

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, _hour):
        self.__hour = str(_hour)
        self.__update__()

    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, _min):
        self.__min = str(_min)
        self.__update__()

    @property
    def sec(self):
        return self.__sec

    @sec.setter
    def sec(self, _sec):
        self.__sec = str(_sec)
        self.__update__()

    @property
    def value(self):
        return self.__date.strftime(self.__format_string)

    @property
    def format_string(self):
        return self.__format_string

    @format_string.setter
    def format_string(self, _format_string):
        self.__format_string = _format_string

    @property
    def date_format_string(self):
        return self.__format_string.split(' ')[0]

    @date_format_string.setter
    def date_format_string(self, _date_format_string):
        self.__format_string = ' '.join([
            _date_format_string,
            self.time_format_string
        ])

    @property
    def date(self):
        return self.__date.strftime(self.date_format_string)

    @date.setter
    def date(self, _date):
        _foo = datetime.datetime.strptime(_date, self.date_format_string)
        self.__year = _foo.strftime('%Y')
        self.__month = _foo.strftime('%m')
        self.__day = _foo.strftime('%d')
        self.__update__()

    @property
    def time_format_string(self):
        return self.__format_string.split(' ')[1]

    @time_format_string.setter
    def time_format_string(self, _time_format_string):
        self.__format_string = ' '.join([
            self.date_format_string,
            _time_format_string
        ])

    @property
    def time(self):
        return self.__date.strftime(self.time_format_string)

    @time.setter
    def time(self, _time):
        _foo = datetime.datetime.strptime(_time, self.time_format_string)
        self.__hour = _foo.strftime('%H')
        self.__min = _foo.strftime('%M')
        self.__sec = _foo.strftime('%S')
        self.__update__()

    def __str__(self):
        return self.__date.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    myDate = datetime.datetime.strptime('22/06/1942 4:20:30', '%d/%m/%Y %H:%M:%S')
    print(myDate)
    print(myDate.strftime('%d-%m-%Y'))
    myDate_obj = nDateTime('22/06/1942 04:15:16')
    print(f'myDate format string is: {myDate_obj.format_string}')
    print(f'myDate date formatted by string: {myDate_obj.date_format_string}')
    print(f'myDate time formatted by string; {myDate_obj.time_format_string}')
    print(myDate_obj.date)
    print(f'TIME in my obj is: {myDate_obj.time}')
    print(f'Date format string is: {myDate_obj.date_format_string}')
    myDate_obj.date = '01/01/2001'
    print(f'Now object is: {myDate_obj}')
    myDate_obj.time = '3:12:13'
    print(f'Now object is: {myDate_obj}')
    #myDate_obj.format_string = 'Ololo'
    #print(f'And now myDate format string is: {myDate_obj.format_string}')


    '''
    date_obj = nDateTime('22/06/1942 04:00:00')
    print(date_obj.year)
    #print(f'Hour: {date_obj.hour}')
    date_obj.year = '1945'
    #print(f'Min: {date_obj.min}')
    #print(f'New year: {date_obj.year}')
    print(date_obj)
    date_obj.day = 7
    print(date_obj)
    date_obj.min = 34
    print(date_obj)
    print(f'Value as given: {date_obj.value}')
    '''

