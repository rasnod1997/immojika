
from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch, MovieYear, MovieMostWatched, MovieTopRated,  MovieRecentlyAdded


app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('most_watched/', MovieMostWatched.as_view(), name='most_watched'),
    path('top_rated/', MovieTopRated.as_view(), name='top_rated'),
    path('recently_added/', MovieRecentlyAdded.as_view(), name='recently_added'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('year/<int:year>', MovieYear.as_view(), name='movie_year'),

]

