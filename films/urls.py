from django.urls import path
from django.conf.urls import url
from .views import (
	SearchView, 
	SearchResultsListView, 
	SaveMovieView, 
	SavedMoviesListView
	)

urlpatterns = [
	path('search/', SearchView.as_view(), name='search'),
	path('search-results/', SearchResultsListView.as_view(), name='search_results'),
	path('save/<str:title>/<str:year>/', SaveMovieView.as_view(), name='save'),
	path('saved/', SavedMoviesListView.as_view(), name='saved'),
]
