from django.shortcuts import render

# Create your views here.
def index(request):
    d = {}
    d["test"] = "Shuyang got laid last night"
    a = ["test1", "test2"]
    d["testing"] = a
    return render(request, 'home/index.html', d)
