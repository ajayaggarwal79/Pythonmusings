"""
A series of functions using the datetime module to help verify date values
"""

import datetime

def days_in_month(year, month):
    """
    A function that takes the days and month as an integer value and
    returns the number of days in the input month
          
    """
    #Check to understand if the year is in the date range and if the month is between 1-12. 
    # And if the month falls into a certain integer the days in the month are returned
    #A final check for February to address the leap year challenge
    if datetime.MINYEAR <= year <= datetime.MAXYEAR and month in (1,3,5,7,8,10,12):
        return 31
    elif datetime.MINYEAR <= year <= datetime.MAXYEAR and 1 <=month <=12 and month in (4,6,9,11):
        return 30
    elif (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0) and month==2:
        return 29
    elif datetime.MINYEAR <= year <= datetime.MAXYEAR and 1 <=month <=12 and month==2:
        return 28
        

#    
#    
#print (days_in_month(2015,2))    
#


def is_valid_date(year, month, day):
    """
    A function to validate if the date convention provided by the user is valid
    """ 
#    """
#    Inputs:
#      year  - an integer representing the year
#      month - an integer representing the month
#      day   - an integer representing the day
#
#    Returns:
#      True if year-month-day is a valid date and
#      False otherwise

    valid_date=None
    try:
        valid_date=datetime.date(year,month,day)
        valid_date=True
        return valid_date
    except ValueError:
        valid_date=False
        return valid_date


#print(is_valid_date(2014, 5, 5))

#
#
def days_between(year1, month1, day1, year2, month2, day2):
    
    """
    A function to validate and calcualte the difference 
    """ 
    date_1=None
    date_2=None
    checked_date_1=None
    checked_date_2=None
    diff=None
    if (is_valid_date(year1, month1, day1)) is True:
        date_1=True
        #return date_1
    elif(is_valid_date(year1, month1, day1)) is False:
        date_1=False
        #return date_1
    if (is_valid_date(year2, month2, day2))is True:
        date_2=True
        #return date_2
    elif (is_valid_date(year2, month2, day2))is False:
        date_2=False
        #return date_2
    
    if date_1 is True:
        checked_date_1=datetime.date(year1,month1,day1)
        #return checked_date_1
    if date_2 is True:
        checked_date_2=datetime.date(year2,month2,day2)
        #return checked_date_2
    
    if (date_1 is False or date_2 is False or checked_date_1 >checked_date_2):
        return 0
    else:
        diff=checked_date_2-checked_date_1
        return diff.days
        

#
#print(days_between(2020, 12, 5, 2023  ,1 ,1 ))


def age_in_days(year, month, day):
   
    """
    A function to validate and calcualte the age in days
    """

    todays_date = datetime.date.today()
    todays_day=todays_date.day
    todays_month=todays_date.month
    todays_year=todays_date.year
    
    
    #todays_date.year, todays_date.month, and todays_date.day)
    try:
        if(datetime.date(year,month,day)) > todays_date:
            return 0 
        else:
            return(days_between(year, month, day, todays_year, todays_month, todays_day))
    except ValueError:
        return 0
    
print(age_in_days(0, 1, 21))
