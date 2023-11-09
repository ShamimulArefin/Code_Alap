from django.shortcuts import render
import requests

# Create your views here.
def tools(request):
    dict = {'title':'Tools - Code Alap'}
    return render(request, 'toolsApp/tools.html', context=dict)

def githubUserView(request):
    dict = {'title':'Github Profile Viewer - Code Alap',}
    user = False
    if request.method == 'POST':
        username = request.POST.get('username')
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()

        repo_url = 'https://api.github.com/users/%s/repos' % username
        repo_response = requests.get(repo_url)
        repos = repo_response.json()

        dict.update({'user':user, 'repos':repos, 'viewUser':True})

    return render(request, 'toolsApp/githubUserViewer.html', context=dict)