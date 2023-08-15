from ipywidgets import VBox, Label, Button
from traitlets import directional_link

from lib.view_models.sample_view_model import SampleViewModel

from lib.custom_widgets.custom_anywidget.custom_anywidget import CustomAnyWidget

class CustomWidgetView(VBox):
    """
    CustomWidgetView View class subscribing to a SampleViewModel. 
    Represents GUI elements built with the use of custom widget - developed using javascript and css code, 
    integrated with jupyter notebook using anywidget library.
    """

    def __init__(self, sample_vmodel: SampleViewModel):
        super(CustomWidgetView, self).__init__()

        self._vmodel = sample_vmodel

        self._title_label = Label(value = 'View created from custom widgets (js + css)', disabled=True)

        # replacing two predefined labels from SampleView class with new custom widget
        self._custom_widget = CustomAnyWidget()

        self._button = Button(description="Get Data")
        self._button.on_click(self._get_data)

        self.children = [self._title_label, self._custom_widget, self._button]

        self._set_value_subscriptions()

    def _set_value_subscriptions(self):
        """
        Subscribes to changes of data interface of assigned View Model. 
        """

        directional_link(
            (self._vmodel, 'string_value')
            ,(self._custom_widget, 'text_1')
        )

        directional_link(
            (self._vmodel, 'int_value')
            ,(self._custom_widget, 'text_2')
            ,lambda x: str(x) or str()
        )

    def _get_data(self, button):
        """
        Calls get_model() method from View Model when assigned button in pressed on the UI screen.
        """
        self._vmodel.get_model()