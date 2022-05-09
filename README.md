# Final

Blog, TP Final CoderHouse

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy final

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

##PRINCIPALES VISTAS DEL PROYECTO
http://127.0.0.1:8000/blog/ esta es la página de inicio, aquí se encuentran los formularios para loguearse o para crear un nuevo usuario.
http://127.0.0.1:8000/usuarios/register/ es la página con el formulario para registrar un nuevo usuario y luego loguearse.
http://127.0.0.1:8000/usuarios/login/ es la página para loguearse.
http://127.0.0.1:8000/home/ es la página de inicio del blog, da la bienvenida y además muestra el avatar, con la foto correspondiente.
http://127.0.0.1:8000/about-us/ muestra información sobre mí.
http://127.0.0.1:8000/pages/ es la página con los accesos a las páginas del blog (receta/detail) y a páginas vinculadas con administración de usuarios (usuarios/).
http://127.0.0.1:8000/receta/detail/ es la página con detalle de las páginas del blog, permite ver los siguientes enlaces:
http://127.0.0.1:8000/receta/receta-new-form/ registrar una nueva receta.
http://127.0.0.1:8000/receta/receta-view-detail/5 muestra el detalle de la receta que queremos ver.
http://127.0.0.1:8000/receta/receta-update/5 permite actualizar la receta.
http://127.0.0.1:8000/receta/receta-delete/5 permite eliminar la receta.
http://127.0.0.1:8000/usuarios/ es la página con detalle de administración de usuarios:
http://127.0.0.1:8000/usuarios/edit/ permite editar el usuario, subir una foto por ejemplo.
http://127.0.0.1:8000/usuarios/logout/ y finalmente desloguearme.








