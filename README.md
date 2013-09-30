# topdown

A community for making top-down action-adventure games.

## Developer Setup

Prerequisites:
- Python 2.7
- [pip](http://www.pip-installer.org/en/latest/)
- (Recommended) A [virtualenv](http://www.virtualenv.org/en/latest/)

```sh
# Clone the repo and enter the directory.
git clone https://github.com/Osmose/topdown.git; cd topdown

# Install the development requirements.
pip install -r requirements/dev.txt

# Copy the local settings template and fill it in.
cp topdown/settings/local.py-dist topdown/settings/local.py
vi topdown/settings/local.py

# Start the development server.
python manage.py runserver`
```

## License

topdown is licensed under the [MIT License](http://opensource.org/licenses/MIT). See `LICENSE`
for details.