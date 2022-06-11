import joblib

from django.shortcuts import render
from django.http import JsonResponse

from sklearn.feature_extraction.text import TfidfVectorizer

from fake_news_detection.models import NewsArticle
from fake_news_detection.forms import NewsArticleForm


tfidf_vectorizer = joblib.load('vectorizer.sav')
pac = joblib.load('model.sav')

def index(request):
	form = NewsArticleForm()
	if request.is_ajax and request.method == "POST":
		newspaper = request.POST.get("newspaper")
		category = request.POST.get("category")
		news_text = request.POST.get("news_text")
		vec_news_text = tfidf_vectorizer.transform([news_text])
		ans = pac.predict(vec_news_text)

		return JsonResponse({"prediction": ans[0]}, status=200)

	return render(request, 'fake_news_detection/index.html', {'form': form})

def satisfaction(request):

	if request.is_ajax and request.method == "POST":
		newspaper = request.POST.get("newspaper")
		category = request.POST.get("category")
		news_text = request.POST.get("news_text")
		label = request.POST.get("label")
		NewsArticle.objects.create(newspaper=newspaper, category=category, news_text=news_text, label=label)
		return JsonResponse({}, status=200)
	return JsonResponse({}, status=400)

