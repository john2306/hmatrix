from django.shortcuts import render

# Create your views here.
def projects_list_view(request):

    context = {}
    return render(request, 'projects/project_list.html', context)