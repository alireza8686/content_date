from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from date_app.models import Day
# Create your views here.


@login_required
def panel_view(request, user_id, *args):
    if request.user.id == user_id:
        user = request.user
        
        first_name = user.first_name
        last_name = user.last_name

        if request.method == 'POST':
            month_number = request.POST["month"]
            year_number = request.POST["year"]

            days = Day.objects.all().filter(user_id=user_id, month=month_number, year=year_number)
            
            if (month_number and year_number) or days:
                show = 1
                return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name,'days' : days, "month_number" : month_number, "year_number" : year_number, "show": show})
            else:
                return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name,'days' : days, "month_number" : month_number, "year_number" : year_number})

            
        else:
            if "month" in request.GET:
                month_number = request.GET["month"]
                year_number = request.GET["year"]
                days = Day.objects.all().filter(user_id=user_id, month=month_number, year=year_number)
                
                if "error" in request.GET:
                    month_number = request.GET["month"]
                    year_number = request.GET["year"]
                    error = request.GET["error"]
                    content = request.GET["content"]
                    day_number = request.GET["day_number"]
                    width = request.GET["width"]
                    height = request.GET["height"]
                    days = Day.objects.all().filter(user_id=user_id, month=month_number, year=year_number)
                    
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
                                   "width" : width,
                                   "height" : height,
                                   "show" : show})
                
                else:
                    if (month_number and year_number) or days:
                        show = 1

                        return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name,'days' : days, "month_number" : month_number, "year_number" : year_number, "show":show})
                    else:
                        return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name,'days' : days, "month_number" : month_number, "year_number" : year_number})

            else:
                return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name})
   
    else:
        return redirect('login') 