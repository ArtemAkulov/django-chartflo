Write a generator
=================

How it works
------------

The dahsboards generation logics lives in generators. These are responsible for processing the data into widgets and charts.

Define a generator
------------------

Define a ``chartflo.py`` file or package in any app with a ``run`` function. This is where the generators live. These
files will be detected at startup and the generators will be registered.

The charts and widgets generation logic is located in a generator. There are 
`example notebooks <https://github.com/synw/django-chartflo-notebooks>`_ available to show how to draw charts.

Click on the badge to run them online:

.. image:: https://mybinder.org/badge.svg :target: https://mybinder.org/v2/gh/synw/django-chartflo-notebooks/master

TODO: More code examples and detailled doc about charts generation

Rendering engines
-----------------

The default rendering engine is Bokeh. To use Altair set it first: ``chart.engine = "altair"``.


Encoding options
----------------

For the ``x`` and ``y`` axis definitions and the ``time_unit`` when using Altair refer to 
the `Altair encoding documentation <https://altair-viz.github.io/documentation/encoding.html>`_

Run the generator
-----------------

Run the generator with a management command to generate the html files: 

.. highlight:: python

::
   
   python3 manage.py gen myapp


Subgenerators
-------------

An app can contain multiple subgenerators: to use this feature create a ``chartflo`` package in an app:

::
   
   __init__.py
   mysubgenerator.py
   
The ``__init__.py`` contains the main generator with its ``run`` function. The ``subgenerator.py`` also has to have a
``run`` function. To launch a subgenerator:

.. highlight:: python

::
   
   python3 manage.py gen myapp.mysubgenerator

