from django.shortcuts import render

def Author(request):
    return render (request, 'Author/Author.html', {})