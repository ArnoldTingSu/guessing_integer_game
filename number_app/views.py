from django.shortcuts import render, redirect
import random
# Create your views here.

def home(request):
    return render(request, "landing.html")

def assign(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['username'])
        request.session['username'] = request.POST['username']
        return redirect('/game')
    else:
        return render(request, "landing.html")

def game(request):
    context = {
        'values': [1,2,3,4,5,6,7,8,9,10]
        #is this a string or an integer#
    }
    return render(request, "game.html", context)

def process_game(request):
    if request.method == 'POST':
        print(request.POST)
        guess = request.POST['guess']
        random_num = round(random.random()*9+1) # definitely an integer #
        print(random_num)
        print(guess)
        request.session['result'] = None
        if random_num == guess:
            request.session['result'] = f"{request.session['username']}, you guessed the right number {random_num}!! WOOOO!"
        else:
            request.session['result'] = f"{request.session['username']}, you selected the number {guess} bro! It was {random_num}. Try again!"
        return redirect('/game')
    else:
        return redirect('/')
        