from django.shortcuts import render_to_response, get_object_or_404

def main(request):
    context = {}
    return render_to_response('main.html', context)

def register(request):
    context = {}
    return render_to_response('register.html', context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render_to_response('profile.html', context)

def profile_edit(request):
    context = {}
    return render_to_response('profile_edit.html', context)

def project(request):
    #TODO news post code to get latest posts
    context = {}
    return render_to_response('project.html', context)

def project_edit(request):
    context = {}
    return render_to_response('project_edit.html', context)
