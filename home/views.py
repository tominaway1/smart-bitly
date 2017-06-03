from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    d = {}
    d["test"] = "Shuyang got laid last night"
    a = ["test1", "test2"]
    d["testing"] = a
    return render(request, 'home/index.html', d)
