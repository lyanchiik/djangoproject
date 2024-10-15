from django.shortcuts import render


def hello_world(request):
    name = None
    greeting = None

    if 'visit_count' in request.session:
        request.session['visit_count'] += 1
    else:
        request.session['visit_count'] = 1

    visit_count = request.session['visit_count']

    if request.method == 'POST':
        name = request.POST.get('name')
        greeting = f"Привіт, {name}!"

    context = {
        'greeting': greeting,
        'name': name,
        'visit_count': visit_count,
        'cookies': request.COOKIES,
    }

    response = render(request, 'hello_app/hello_app.html', context)
    response.set_cookie('author', 'Lyanchik')

    return response
