DjangoPBX Applications
--------------------------------------
This repository is for additional applications for the DjangoPBX project,
that are not part of the core distribution.

### Additional functionality
These applications are designed to provide additional functionality for DjangoPBX.
Contributions are always very welcome.

## Installation
Installation of an application is fairly straightforward, the basic steps are listed below.
Most applications should contain an install.txt file that will guide you through and specific
steps you may need to undertake for an individula application.
* Clone this repository.
* Copy the application(s) you are interested in to /home/django-pbx/pbx/
* Add your new application to the INSTALLED_APPS list in /home/django-pbx/pbx/pbx/settings.py

Here are the steps in alittle more detail, we will use the fsterminal application as an example.
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




## License Agreement

If you contribute code to this project, you implicitly allow your code to be distributed under the MIT license. You are also implicitly verifying that all code is your original work.

Copyright (c) 2016-2024, [The DjangoPBX authors](https://github.com/djangopbx/djangopbx-applications/graphs/contributors) (MIT License)<br>
