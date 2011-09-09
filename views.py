from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from forms import *
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile, Project, Tag, NewsEntry, Tag, SkillTag
from django.contrib.auth import auth_logout
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
    if not user.is_anonymous:
        context = {'user':user}
        return render_to_response('dashboard.html', context)
    else:
        regForm = UserCreationForm()
        context = RequestContext(request, {'regForm': regForm})
        return render_to_response('main.html', context)

def register_get(request):
    regForm = UserCreationForm()
    context = {'regForm': regForm}
    return render_to_response('register.html', context)

def register_post(request):
    regForm = UserCreationForm(request.POST)
    if regForm.is_valid():
        new_user = regForm.save()
        new_profile = Profile(user=new_user).save()
        success = True
    else:
        success = False
    context = RequestContext(request, {'regForm' : regForm, 'success' : success})
    return render_to_response('register.html', context)

def profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user_obj)
    context = {'profile': profile}
    return render_to_response('profile.html', context)

@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    editForm = ProfileForm(instance=profile)
    context = {'editForm':editForm}
    return render_to_response('profile_edit.html', context)

def project(request, pk_id):
    #TODO news post code to get latest posts
    context = {}
    return render_to_response('project.html', context)

@login_required
def project_edit(request, pk_id):
    context = {}
    return render_to_response('project_edit.html', context)

def search(request):
    query = request.GET.get('q')
    context = {'query' : query}
    return render_to_response('search.html', context)

def logout(request):
    auth_logout(request)
    return render_to_response('main.html', {})
