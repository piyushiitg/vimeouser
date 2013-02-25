from django.shortcuts import render_to_response
from django.http import HttpResponse
from vimeocrawl.models import Vimeouserinfo

def user_search(request):
    return render_to_response('search.html')

def search(request):
        type = request.GET['type']
        if 'userq' in request.GET and request.GET['userq']:
            userq = request.GET.get('userq')
            if type == 'Paying':
                v_users = Vimeouserinfo.objects.filter(Name__icontains=userq,Paying="Yes")
            elif type == 'Video':
                v_users = Vimeouserinfo.objects.filter(Name__icontains=userq,Video="Yes")
            elif type == 'StaffPick':
                v_users = Vimeouserinfo.objects.filter(Name__icontains=userq,StaffPick="Yes")
            else:
                v_users = Vimeouserinfo.objects.filter(Name__icontains=userq)
            return render_to_response('searchresults.html',{'v_users': v_users[0:100], 'query': userq,'length':len(v_users)})
        else:
            return HttpResponse('Please Enter in Textbox.')
            

