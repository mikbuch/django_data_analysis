# Upload file for data analysis

Example strongly based on [How to Upload Files With Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)

## Running Locally

```bash
git clone https://github.com/mikbuch/django_data_analysis
```

```bash
cd django_data_analysis
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

### Troubleshooting

```
Git fatal: protocol 'https' is not supported
```

Use right-click paste, instead of crtl+V (see [this answer](https://stackoverflow.com/a/55985462/8877692)).
