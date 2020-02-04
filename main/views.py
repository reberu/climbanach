from django.shortcuts import render

def my_test_view(request):
    return render(
        request,
        'main/index.html'
    )
