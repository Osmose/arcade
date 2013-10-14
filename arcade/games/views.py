from django.shortcuts import redirect

from braces.views import LoginRequiredMixin
from vanilla import CreateView, DetailView

from arcade.games.forms import NewGameForm
from arcade.games.models import Game


class CreateNewGameView(LoginRequiredMixin, CreateView):
    model = Game
    form_class = NewGameForm
    template_name = 'games/create.html'

    def form_valid(self, form):
        game = Game()
        game.author = self.request.user
        packaged_app_archive = form.cleaned_data['packaged_app_archive']
        game.packaged_app.save(packaged_app_archive.name, packaged_app_archive, save=True)

        return redirect(game)


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/detail.html'
