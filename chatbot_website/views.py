from django.shortcuts import render, get_object_or_404, redirect
from .models import Article_One, News, Category
from .models import Article_Two
from .models import Article_Three
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin

import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin


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

class BlogNews(MyMixin, ListView):
    model = News
    template_name = 'chatbot_website/blog_news_list.html'
    context_object_name = 'news'
    mixin_prop = 'hello world'
    # extra_context = {'title': 'Блог'}
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published = True).select_related('category')

class NewsByCategory(MyMixin, ListView):
    # model from we get all data
    model = News
    # template page
    template_name = 'chatbot_website/blog_news_list.html'
    # default object using in foreach considering all data
    context_object_name = 'news'
    # forbid show a news doesn't exits
    allow_empty = False

    # override context of data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk = self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'],
                                   is_published = True).select_related('category')
    paginate_by = 4

def blog(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='chatbot_website/blog.html', context=context)

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # required slug or id
    # pk_url_kwarg = 'news_id'

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'chatbot_website/add_news.html'
    login_url = '/admin/'


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, template_name='chatbot_website/category.html', context=context)

# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, template_name='chatbot_website/view_news.html', context={"news_item": news_item})

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, template_name='chatbot_website/add_news.html', context={'form': form})

cloudinary.config(
  cloud_name = "dutifxbda",
  api_key = "333126896845945",
  api_secret = "IShvaI-vLwXGI-ckJl35rDkM9VY"
)


