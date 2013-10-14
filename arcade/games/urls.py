from django.conf.urls.defaults import patterns, url

from arcade.games import views


urlpatterns = patterns('',
    url(r'^games/new/$', views.CreateNewGameView.as_view(), name='games.CreateNewGameView'),
    url(r'^games/(?P<pk>\d+)/$', views.GameDetailView.as_view(), name='games.GameDetailView'),
)
