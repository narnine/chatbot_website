from django.shortcuts import render
from .models import Article_One
from .models import Article_Two
from .models import Article_Three
from .models import Article_Fourth
# Create your views here.
def index(request):
    article_one = Article_One.objects.filter(title='Чат-боты. Что это такое?')
    article_two = Article_Two.objects.filter(title='Где они живут?')
    article_three = Article_Three.objects.filter(title='Преимущества и недостатки')
    return render(request, 'chatbot_website/index.html', {'article_one': article_one, 'article_two': article_two, 'article_three': article_three})

def begin(request):
    article_three = Article_Three.objects.filter(title='Первые чат-боты.')
    return render(request, 'chatbot_website/begin.html', {'article_three': article_three})

def ourtime(request):
    article_one = Article_One.objects.filter(title='Siri')
    article_two = Article_One.objects.filter(title='Melody')
    article_three = Article_One.objects.filter(title='AdmitHub')
    article_four = Article_One.objects.filter(title='Duolingo')
    article_five = Article_Fourth.objects.filter(title_first='Rose')
    return render(request, 'chatbot_website/ourtime.html', {'article_one': article_one, 'article_two': article_two, 'article_three': article_three, 'article_four': article_four, 'article_five': article_five})
