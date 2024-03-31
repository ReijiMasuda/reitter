from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Tweet
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404

def index(request):
    tweet_list = Tweet.objects.all()
    return render(
        request,
        'index.html',
        {'tweet_list': tweet_list}
    )

def post(request):
    message = request.POST['message']
    name = request.POST['name']
    tweet = Tweet(message=message, name=name)
    tweet.save()
    return HttpResponseRedirect(reverse('a:index'))

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        emailMessage = EmailMessage(
            to=['fko2347041@stu.o-hara.ac.jp'],
            subject='お問い合わせがありました：{0}'.format(subject),
            body='名前: {0}\nメールアドレス: {1}\n本文: {2}'.format(name, email, message),
        )
        emailMessage.send()
        return HttpResponseRedirect('/contact')
    else:
        return render(request, 'contact.html')
    
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    tweet.delete()
    return HttpResponseRedirect(reverse('a:index'))

def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    if request.method == 'POST':
        tweet.message = request.POST['message']
        tweet.name = request.POST['name']
        tweet.save()
        return redirect('a:index')

    return render(request, 'edit_tweet.html', {'tweet': tweet})