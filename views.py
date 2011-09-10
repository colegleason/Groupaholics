from django.shortcuts import render_to_response, HttpResponseRedirect, get_object_or_404
from django.template import RequestContext
from forms import *
from users.models import Profile, Project, Tag, NewsEntry, Tag, SkillTag
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def method_splitter(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    raise Http404

def main(request):
    user = request.user
    if user.is_authenticated():
        context = RequestContext(request, {'user' : user})
        return render_to_response('dashboard.html', context)
    else:
        regForm = ProfileCreationForm()
        context = RequestContext(request, {'regForm': regForm})
        return render_to_response('main.html', context)

def register_get(request):
    regForm = ProfileCreationForm()
    context = RequestContext(request, {'regForm': regForm})
    return render_to_response('register.html', context)

def register_post(request):
    regForm = ProfileCreationForm(request.POST)
    if regForm.is_valid():
        new_user = regForm.save()
        regSuccess = True
        context = RequestContext(request, {'regSuccess' : regSuccess})
        return render_to_response('success.html', context)  
    else:
        context = RequestContext(request, {'regForm' : regForm})
        return render_to_response('register.html', context)

def profile(request, username):
    profile = get_object_or_404(Profile, username = username)
    context = RequestContext(request, {'profile': profile})
    return render_to_response('profile.html', context)

@login_required
def profile_edit(request):
    profile = Profile.objects.get(username=request.user.username)
    if request.method == 'POST':
        editForm = ProfileEditForm(request.POST, instance=profile)
        if editForm.is_valid():
            editForm.save()
    else:
        editForm = ProfileEditForm(instance=profile)
    context = RequestContext(request, {'editForm':editForm})
    return render_to_response('profile_edit.html', context)

def project(request, pk_id):
    context = Requestcontext(request, {})
    return render_to_response('project.html', context)

@login_required
def project_edit_get(request, pk_id=None):
    if pk_id:
        project = Project.objects.get(pk_id=pk_id)
        editForm = ProjectForm(instance=project)
    else:
        editForm = ProjectForm()
    context = RequestContext(request, {'editForm': editForm})
    return render_to_response('project_edit.html', context)

def project_edit_post(request, pk_id=''):
    if pk_id:
        project = Project.objects.get(pk_id=pk_id)
        editForm = ProjectForm(request.POST, instance=project)
        if editForm.is_valid:
            editForm.save()
            return redirect('/project/'+pk_id)
    else:
        editForm = ProjectForm(request.POST)
        if editForm.is_valid:
            pk_id = editForm.save().pk_id
            return('/project/'+pk_id)
    context = RequestContext=(request, {'editForm': editForm})
    return render_to_response("project_edit.html", context)


def search(request):
    query = request.GET.get('q')
    
    context = RequestContext(request, {'query' : query})
    return render_to_response('search.html', context)

def logout(request):
    auth_logout(request)
    context = RequestContext(request, {})
    return render_to_response('main.html', context)
