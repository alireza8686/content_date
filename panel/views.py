from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from date_app.models import DaysInformation
from persiantools.jdatetime import JalaliDate
import calendar
# Create your views here.


def month_days(year,month):
    year = int(year)
    month = int(month)

    # last_day = calendar.monthrange(year, month)
    # print(last_day)
    _, last_day = calendar.monthrange(year, month)

    if month == 2:
        last_day += 3
    elif month == 12:
        last_day -= 1

    month_calendar = []
    week = []
    for day in range(1, last_day + 1):
        jalali_date = JalaliDate(year,month, day)

        day_info = {
            "day": day,
            "weekday": jalali_date.strftime('%A'),
            "day_id" : jalali_date.weekday()
        }

        week.append(day_info)
        print(day,last_day,month)
        if jalali_date.weekday() == 6 or day == last_day:
            month_calendar.append(week)
            week = []

    return month_calendar

@login_required
def panel_view(request, user_id, *args):
    if request.user.id == user_id:

        user = request.user
        
        first_name = user.first_name
        last_name = user.last_name

        if request.method == 'POST':
            month_number = request.POST["month"]
            year_number = request.POST["year"]

            days = DaysInformation.objects.all().filter(user_id=user_id, month=month_number, year=year_number)

            month_calendar = month_days(year_number,month_number)
            
            if (month_number and year_number) or days:
                show = 1
                return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name,'days' : days, "month_number" : month_number, "year_number" : year_number, "show": show, "month_calendar" : month_calendar})
            else:
                return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name,'days' : days, "month_number" : month_number, "year_number" : year_number, "month_calendar" : month_calendar})

            
        else:
            if "month" in request.GET:
                month_number = request.GET["month"]
                year_number = request.GET["year"]
                days = DaysInformation.objects.all().filter(user_id=user_id, month=month_number, year=year_number)
                
                month_calendar = month_days(year_number,month_number)

                if "error" in request.GET:
                    month_number = request.GET["month"]
                    year_number = request.GET["year"]
                    error = request.GET["error"]
                    content = request.GET["content"]
                    day_number = request.GET["day_number"]
                    
                    month_calendar = month_days(year_number,month_number)

                    days = DaysInformation.objects.all().filter(user_id=user_id, month=month_number, year=year_number)
                    
                    if (month_number and year_number) or days:
                        show = 1
                    print(error)
                    return render(request, 'panel/panel.html', 
                                  {"first_name" : first_name , 
                                   "last_name" : last_name,
                                   'days' : days, 
                                   "month_number" : month_number, 
                                   "year_number" : year_number, 
                                   "error" : error,
                                   "content" : content,
                                   'day_number' : day_number,
                                   "show" : show})
                
                else:
                    if (month_number and year_number) or days:
                        show = 1

                        return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name,'days' : days, "month_number" : month_number, "year_number" : year_number, "show":show, "month_calendar" : month_calendar})
                    else:
                        return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name,'days' : days, "month_number" : month_number, "year_number" : year_number, "month_calendar" : month_calendar})

            else:
                return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name})
   
    else:
        return redirect('login') 
    