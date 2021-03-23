from django.http import HttpResponse
from django.shortcuts import render
from .models import Article_One, News, Category
from .models import Article_Two
from .models import Article_Three

import cloudinary
import cloudinary.uploader
import cloudinary.api
# Create your views here.
def index(request):
    article_one = Article_One.objects.filter(title='Введение')
    article_two = Article_One.objects.filter(title='Чат – боты и области их применения')
    article_three = Article_Three.objects.filter(title='Где они живут?')
    return render(request, 'chatbot_website/index.html', {'article_one': article_one, 'article_two': article_two, 'article_three': article_three})

def begin(request):
    article_one = Article_One.objects.filter(title='Предпосылки')
    article_two = Article_Two.objects.filter(title='Первые чат-боты')
    return render(request, 'chatbot_website/begin.html', {'article_one': article_one, 'article_two': article_two})

def ourtime(request):
    article_one = Article_One.objects.filter(title='Почему за них взялись только сейчас?')
    article_two = Article_One.objects.filter(title='Статистика')
    article_three = Article_One.objects.filter(title='Ложка дёгтя')
    return render(request, 'chatbot_website/ourtime.html', {'article_one': article_one, 'article_two': article_two, 'article_three': article_three})

def future(request):
    article_one = Article_One.objects.filter(title='Чат-боты вытеснят мобильные приложения?')
    return render(request, 'chatbot_website/future.html', {'article_one': article_one})

def simple(request):
    article_one = Article_One.objects.filter(title='Простые чат-боты')
    article_two = Article_Two.objects.filter(title='Преимущества и недостатки простых чат-ботов')
    return render(request, 'chatbot_website/simple.html', {'article_one': article_one, 'article_two': article_two})

def hard(request):
    article_one = Article_One.objects.filter(title='Сложные чат-боты')
    article_two = Article_Two.objects.filter(title='Преимущества и недостатки сложных чат-ботов')
    return render(request, 'chatbot_website/hard.html', {'article_one': article_one, 'article_two': article_two})

def example(request):
    article_one = Article_One.objects.filter(title='Siri')
    article_two = Article_One.objects.filter(title='Евгений Густман')
    article_three = Article_One.objects.filter(title='Duolingo')
    article_four = Article_One.objects.filter(title='A.I. Jim')
    article_five = Article_One.objects.filter(title='Melody')
    return render(request, 'chatbot_website/example.html', {'article_one': article_one,  'article_two': article_two, 'article_three': article_three, 'article_four': article_four, 'article_five': article_five})

def blog(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='chatbot_website/blog.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, template_name='chatbot_website/category.html', context=context)

cloudinary.config(
  cloud_name = "dutifxbda",
  api_key = "333126896845945",
  api_secret = "IShvaI-vLwXGI-ckJl35rDkM9VY"
)


