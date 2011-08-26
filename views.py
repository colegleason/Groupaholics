from django.shortcuts import render_to_response

def main(request):
    context = {}
    return render_to_response('main.html', context)
