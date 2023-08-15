from ipywidgets import HBox

from lib.view_models.sample_view_model import SampleViewModel
from lib.views.sample_view import SampleView
from lib.views.custom_widget_view import CustomWidgetView

class MainView(HBox):
    """
    MainView View class representing two sets of GUI elements - one created only with predefined ipywidgets, 
    the second created also with custom ones. 

    Initiates View Model classes and assigns them to the Views. 
    """

    def __init__(self):
        super(MainView, self).__init__()

        self._sample_view = SampleView(SampleViewModel())
        self._custom_widget_view = CustomWidgetView(SampleViewModel())

        self.children = [self._sample_view, self._custom_widget_view]