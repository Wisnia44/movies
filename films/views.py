from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views import View
from .models import Movie
from .omdbapi_controller import get_movies_by_title_year
from django.core.paginator import Paginator

@method_decorator(login_required, name='dispatch')
class SearchView(View):
	template_name = 'films/movie-search.html'
	def get (self, request, *args, **kwargs):
		return render(request, self.template_name, {})

@method_decorator(login_required, name='dispatch')
class SearchResultsListView(View):
	template_name = 'films/movies-searched.html'

	def get(self, request, *args, **kwargs):
		page = request.GET.get('page', 1)
		context = {}
		context['search_title'] = request.GET.get('t')
		context['search_year'] = request.GET.get('y')
		object_list = get_movies_by_title_year(context['search_title'], context['search_year'])
		paginator = Paginator(object_list, 8)
		context['object_list'] = paginator.page(page)
		page_number = request.GET.get('page')
		context['page_obj'] = paginator.get_page(page_number)
		return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class SaveMovieView(View):
	def get(self, request, *args, **kwargs):
		title=self.kwargs.get('title')[:80]
		year=self.kwargs.get('year')[:4]
		user=self.request.user
		Movie.objects.create(title=title, year=year, user=user)
		return redirect('saved')

@method_decorator(login_required, name='dispatch')
class SavedMoviesListView(ListView):
	template_name = 'films/movies-saved.html'
	paginate_by = 8
	
	def get_queryset(self):
		qs = Movie.objects.filter(user=self.request.user)
		return qs
