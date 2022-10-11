from django.shortcuts import render

# Create your views here.


from django.views import View


# Create your views here.

class IndexShow(View):
    def get(self, request):
        return render(request, "index.html")