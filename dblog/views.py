from django.shortcuts import render

def post_list(request):
    return render(request, 'dblog/post_list.html', {})