from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect,HttpResponseRedirect,HttpResponseNotFound,HttpResponseForbidden,JsonResponse

def index(request):
    return HttpResponse("<a href='post'>/post</a><br>"
                        "<a href='error'>error</a>")
def last(request):
    return HttpResponse("последние посты")
def post(request):
    return HttpResponse("все посты"
                        "<a href='last'last post</a> "
                        "<a href='popular'>popular post</a>")
def popular(request):
    return HttpResponse("популярные посты")
def like(request,id):
    return HttpResponse(f"количество лайков {id}")
def coment(request,id):
    return HttpResponse(f"количество коментариев {id}")
def user(request):
    login= request.GET.get("login","Ubdefiend")
    password = request.GET.get("password","Undefiend")
    return HttpResponse(f"<h2>login:{login} Password: {password}</h2>")
def about(request):
    return HttpResponse("About")
def about(request):
    return HttpResponseRedirect("/about")
def about(request):
    return HttpResponseRedirect("/")
def contacts(request):
    return HttpResponse("Contacts")
def contacts(request):
    return HttpResponsePermanentRedirect("/contacts")
def contacts(request):
    return HttpResponsePermanentRedirect("/")
def error(request):
    return HttpResponseNotFound(f"Not fund", status=404, reason="Error")

def access(request,name,password):
    if (name=='admin'and password=='admin'):
        return HttpResponse("всё ок")
    else:
        return HttpResponseForbidden("всё не ок")

def json(request):
    return JsonResponse({"name":"mipo","age":18})
def set(request):
    username=request.GET.get("username","bimb")
    response=HttpResponse(f"Hello {username}")
    response.set_cookie("username",username)
    return response
def get(request):
    username=request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")