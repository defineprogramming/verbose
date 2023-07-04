from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm

@login_required
def tweet_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets')
    else:
        form = TweetForm()
    return render(request, 'tweet.html', {'form': form})

@login_required
def tweets_list(request):
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tweets.html', {'tweets': tweets})

@login_required
def tweet_detail(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})

@login_required
def delete_tweet(request, id):
    tweet = Tweet.objects.get(id=id)
    if request.user == tweet.user:
        tweet.delete()
    return redirect('tweets')