DjangoPBX Applications
--------------------------------------
This repository is for additional applications for the DjangoPBX project
that are not part of the core distribution.

### Additional functionality
These applications are designed to provide additional functionality for DjangoPBX.
Contributions are always very welcome.

## Installation
Installation of an application is fairly straightforward and the basic steps are listed below.
Most applications should contain an install.txt file that will guide you through any specific
steps you may need to undertake for an individual application.
* Clone this repository.
* Copy the application(s) you are interested in to /home/django-pbx/pbx/
* Add your new application to the INSTALLED_APPS list in /home/django-pbx/pbx/pbx/settings.py


Here are the steps in a little more detail; we will use the fsterminal application as an example.
These steps should be done logged in as the django-pbx user:

### Clone the repository
```sh
cd /usr/src
git clone https://github.com/djangopbx/djangopbx-applications.git djangopbx-applications
```

### Copy application to DjangoPBX
```sh
cd /usr/src/djangopbx-applications
cp -r fsterminal/ /home/django-pbx/pbx/fsterminal/
```

### Edit the setting.py file
```sh
nano /home/django-pbx/pbx/pbx/settings.py
```
Add the application to the INSTALLED_APPS list:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
...
    'autoreports.apps.AutoreportsConfig',
    'fsterminal.apps.FsterminalConfig',
]
```
### Additional Steps
Some applications may require additional installation steps.  Always check
the application's `install.txt` file

###  Editing the urls.py file
```sh
nano /home/django-pbx/pbx/pbx/urls.py
```
Add the application to the INSTALLED_APPS list:
```python
urlpatterns = [
    path('', include('portal.urls')),
    path('xmlhandler/', include('xmlhandler.urls')),
    path('httapihandler/', include('httapihandler.urls')),
    path('xmlcdr/', include('xmlcdr.urls')),
...
    path('autoreports/', include('autoreports.urls')),
    path('fsterminal/', include('fsterminal.urls')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```
###  Run post installation processes
You must be logged in as the django-pbx user and ensure the virtual environment is activated.
With a venv activated your prompt should look like: (envdpbx) django-pbx@myserver:~$.
The key thing is the environment shown in brackets.

If the new application makes changes to the database then we must run a migration:
```sh
cd /home/django-pbx/pbx
python3 manage.py migrate
```

If the new application has any static files like javascript libraries or stylesheets then run collectstatic:
```sh
cd /home/django-pbx/pbx
python3 manage.py collectstatic
```

If the new application adds any items to the Navigation bar menu then run menudefaults to
add the new menu items:
```sh
cd /home/django-pbx/pbx
python3 manage.py menudefaults
```

If the new application adds any new dialplans then run dialplandefaults to
add the new dialplans:
```sh
cd /home/django-pbx/pbx
python3 manage.py dialplandefaults
```

###  Finally enable the updated DjangoPBX application
You will need to do this as the root user:
```sh
uwsgi --reload /var/run/uwsgi/app/djangopbx/pid
```

In the unlikely event that a new application affects the dynamic configuration of FreeSWITCH:
```sh
uwsgi --reload /var/run/uwsgi/app/fs_config/pid
```


## License Agreement

If you contribute code to this project, you implicitly allow your code to be distributed under the MIT license. You are also implicitly verifying that all code is your original work.

Copyright (c) 2016-2024, [The DjangoPBX authors](https://github.com/djangopbx/djangopbx-applications/graphs/contributors) (MIT License)<br>
