import random
from django.shortcuts import render

def guess_number(request):
    if request.method == 'POST':
        if 'reset' in request.POST:
            del request.session['secret_number']
            del request.session['attempts']
            message = 'Гру скинуто! Вгадайте нове число.'
            hint = ''
            request.session['secret_number'] = random.randint(0, 500)
            request.session['attempts'] = []
        else:
            guess = int(request.POST.get('guess', 0))
            if 'secret_number' not in request.session:
                request.session['secret_number'] = random.randint(0, 500)
                request.session['attempts'] = []

            secret_number = request.session['secret_number']
            attempts = request.session['attempts']
            attempts.append(guess)
            request.session['attempts'] = attempts

            if guess == secret_number:
                message = f'Вітаємо! Ви вгадали число {secret_number}!'
                del request.session['secret_number']
                del request.session['attempts']
            else:
                if guess < secret_number:
                    hint = 'Спробуйте більше!'
                else:
                    hint = 'Спробуйте менше!'
                message = 'Спробуйте ще раз!'

    else:
        request.session['secret_number'] = random.randint(0, 500)
        request.session['attempts'] = []
        message = ''
        hint = ''

    attempts = request.session.get('attempts', [])

    return render(request, 'guess_game/guess_game.html', {'message': message, 'attempts': attempts, 'hint': hint})
