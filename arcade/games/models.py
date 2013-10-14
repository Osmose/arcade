import json
import os
import shutil
from zipfile import ZipFile

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from arcade.base.util import urljoin


class Game(models.Model):
    author = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    developer_name = models.CharField(max_length=255, default='')
    launch_url = models.CharField(max_length=255)

    # NOTE: Because we rely on the pk existing, packaged_app can only be set on an instance that is
    # already saved to the database.
    def _packaged_app_filename(self, filename):
        return 'users/{user_id}/games/{game_id}/game.zip'.format(user_id=self.author.id,
                                                                 game_id=self.id)
    packaged_app = models.FileField(upload_to=_packaged_app_filename)
    extracted_app_url = models.CharField(max_length=255, editable=False)

    def save(self, *args, **kwargs):
        skip_extraction = kwargs.pop('skip_extraction', False)
        old_packaged_app = None
        if not skip_extraction and self.id:
            old_packaged_app = Game.objects.get(id=self.id)

        result = super(Game, self).save(*args, **kwargs)

        if not skip_extraction:
            needs_extraction = old_packaged_app is None or self.packaged_app != old_packaged_app
            if needs_extraction:
                self._extract_packaged_app()
                self.save(skip_extraction=True)
        return result

    @property
    def extracted_app_path(self):
        return os.path.join(os.path.dirname(self.packaged_app.path), 'extracted')

    def _extract_packaged_app(self):
        if self.packaged_app:
            path = self.extracted_app_path
            try:
                shutil.rmtree(path)
            except OSError:
                pass
            os.mkdir(path)

            packaged_app_zipfile = ZipFile(self.packaged_app)
            for zipinfo in packaged_app_zipfile.infolist():
                packaged_app_zipfile.extract(zipinfo, path)

            url = self.packaged_app.url.rsplit('/', 1)[0]
            self.extracted_app_url = urljoin(url, 'extracted')
            self._parse_manifest()

    def _parse_manifest(self):
        manifest_path = os.path.join(self.extracted_app_path, 'manifest.webapp')
        with open(manifest_path, 'r') as manifest_file:
            manifest = json.loads(manifest_file.read())
        launch_path = manifest['launch_path'].lstrip('/')
        self.launch_url = urljoin(self.extracted_app_url, launch_path)
        self.name = manifest['name']

        developer = manifest.get('developer')
        if developer:
            self.developer_name = developer.get('name', 'Unknown')


    def get_absolute_url(self):
        return reverse('games.GameDetailView', args=(self.id,))
