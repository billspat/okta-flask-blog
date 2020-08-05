okta-flask-blog
=============== 
A simple Flask blog with user registration and login.


Meta
----

- forked from Randall Degges
- see original blog post https://developer.okta.com/blog/2018/07/23/build-a-simple-crud-app-with-flask-and-python
- slight modifications for Azure/Python

Purpose
-------

This example app showcases how to build simple Flask web apps. It demonstrates
how to work with databases and handle user management (registration, login,
etc.) using OpenID Connect and `Okta <https://developer.okta.com>`_.


Installation
------------

To install the sample app you need to have Python 2.7 or 3.4+ installed. You can
then install the project dependencies by running:

.. code-block:: console

    $ pip install -r requirements.txt

This will install all the project dependencies.


Running the App
---------------

This app requires Okta to run. Okta is a free-to-use API service that stores
user accounts and makes authentication and authorization simpler. Go create a
free Okta developer account before continuing: https://developer.okta.com/signup

Next, you need to create a ``client_secrets.json`` file. This holds the OpenID
Connect information necessary for the app to function. Create a file named
``client_secrets.json`` in the root of your project folder and add the following
contents.

.. code-block:: json

    {
      "web": {
        "client_id": "{{ OKTA_CLIENT_ID }}",
        "client_secret": "{{ OKTA_CLIENT_SECRET }}",
        "auth_uri": "{{ OKTA_ORG_URL }}/oauth2/default/v1/authorize",
        "token_uri": "{{ OKTA_ORG_URL }}/oauth2/default/v1/token",
        "issuer": "{{ OKTA_ORG_URL }}/oauth2/default",
        "userinfo_uri": "{{ OKTA_ORG_URL }}/oauth2/default/userinfo",
        "redirect_uris": [
          "http://localhost:5000",
          "http://localhost:5000/oidc/callback"
        ]
      }
    }

.. note::

  Be sure to replace the Okta variables above appropriately.

Next, define some necessary environment variables.

.. code-block:: console

    export FLASK_APP=blog
    export SECRET_KEY={{ RANDOM_STRING_HERE }}
    export OKTA_ORG_URL={{ OKTA_ORG_URL }}
    export OKTA_AUTH_TOKEN={{ OKTA_AUTH_TOKEN }}
    # optional
    FLASK_ENV=development
    
This example also uses python dot-env, so you may create a file ` .env` with the following contents

.. code-block:: console

    # contents of .env file (for MacOS/Linux)
    FLASK_APP=blog
    FLASK_ENV=development
    SECRET_KEY={{ RANDOM_STRING_HERE }}
    OKTA_ORG_URL={{ OKTA_ORG_URL }}
    OKTA_AUTH_TOKEN={{ OKTA_AUTH_TOKEN }}


Set the ``SECRET_KEY`` variable to a long, random string. This will be used to
secure your sessions (cookies). Then set the other two Okta variables
appropriately.

Next, run the web server.

.. code-block:: console

    flask run

Finally, go visit http://localhost:5000 and explore the site!

To use Azure App Service you must have one of a handful of possible application entry points for the automatic platform detection scripts to work (see docs for Oryx), so you may have to adjust the FLASK_APP var

.. code-block:: console

    FLASK_APP=app.py
