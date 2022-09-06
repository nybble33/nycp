#!/usr/bin/python3

import datetime

class nDateTime:
    '''
    Classs for manilputlating with date and time
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

    def __str__(self):
        return self.__date.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
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
