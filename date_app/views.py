from django.shortcuts import render, redirect, reverse
from date_app.models import Day
from django.http import HttpResponseRedirect
# Create your views here.



def create_content_day(request):
    user_id = request.user.id
    if request.method == "POST":
        day_number = request.POST["day_number"]
        month_number = request.POST["month_number"]
        year_number = request.POST["year_number"]
        content = request.POST["content"]
        width = request.POST["width"]
        height = request.POST["height"]
        # dayid = request.POST['dayid']


        day = Day.objects.filter(user_id=user_id, day_number=day_number, month = month_number, year = year_number, width=width, height = height)
        if day.exists():
            day = Day.objects.get(user_id=user_id, day_number=day_number, month = month_number, year = year_number, width=width, height = height)
            day.content = content
            day.save()
        else:
            print(width, height)
            day = Day.objects.filter(user_id=user_id, month = month_number, year = year_number, width=width, height = height)
            # print(day.width , day.height)
            if day.exists():
                day = Day.objects.filter(user_id=user_id,day_number = day_number, month = month_number, year = year_number)
                if day.exists():
                    redirect_url = reverse("panel", kwargs={"user_id": user_id})
                    redirect_url += f"?month={month_number}&year={year_number}&error={'این شماره برای روز دیگری وجود دارد ابتدا آن را حذف کنید'}&content={content}&day_number={day_number}&width={width}&height={height}"

                    return HttpResponseRedirect(redirect_url)
                else:
                    day = Day.objects.get(user_id=user_id, month = month_number, year = year_number, width=width, height=height)
                    day.day_number = day_number
                    day.content = content
                    day.save()
            else:
                day = Day.objects.filter(user_id=user_id, day_number=day_number, month=month_number, year=year_number)
                if day.exists():
                    day = Day.objects.get(user_id=user_id, day_number=day_number, month=month_number, year=year_number)
                    redirect_url = reverse("panel", kwargs={"user_id": user_id})
                    redirect_url += f"?month={month_number}&year={year_number}&error={'این شماره برای روز دیگری وجود دارد ابتدا آن را حذف کنید'}&content={content}&day_number={day_number}&width={width}&height={height}"

                    return HttpResponseRedirect(redirect_url)
                else:
                    day = Day.objects.create(user_id=user_id, day_number=day_number, month=month_number, year=year_number,content=content, width=width, height=height)
                
        redirect_url = reverse("panel", kwargs={"user_id": user_id})
        redirect_url += f"?month={month_number}&year={year_number}"

        return HttpResponseRedirect(redirect_url)
    else:
        redirect_url = reverse("panel", kwargs={"user_id": user_id})
        redirect_url += f"?month={month_number}&year={year_number}"

        return HttpResponseRedirect(redirect_url)
    




def delete_content_day(request):
    user_id = request.user.id
    if request.method == "POST":
        dayid = request.POST["dayid"]

        day = Day.objects.get(id=dayid)

        month_number = day.month
        year_number = day.year

        day.delete()
        # day.save()
        redirect_url = reverse("panel", kwargs={"user_id": user_id})
        redirect_url += f"?month={month_number}&year={year_number}"

        return HttpResponseRedirect(redirect_url)

    return redirect("panel" , request.user.id)
