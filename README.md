# custom-jupyter-widget
Template (with sample project) for defining custom gui widgets to use in Jupyter Notebook and register dynamically every time the app starts.
To simplify the development, the anywidget library is used: https://anywidget.dev/en/getting-started/

Project represents folder structure for application in MVVM (Model-View-ViewModel) standard.

Entry point for application is the MainApp.ipynb file in main catalog. This notebook refers to MainView class which represents starting GUI screen. 

MVVM project template part: 
* lib - folder with component scripts
* lib/models - definitions of model classes (business logic and data structure)
* lib/view_models - definitions of view-model classes (transformations of data from models and exposing it for views)
* lib/views - definition of view classes - GUI components (displaying data, handling user actions, subscribing to view-models)

CustomWidget extensions part: 
* lib/custom_widgets - definitions of custom widgets. Every widget definition is stored in separate folder. For readability, the code parts for python, javascript and css are divided into separate files, but this is optional. 

