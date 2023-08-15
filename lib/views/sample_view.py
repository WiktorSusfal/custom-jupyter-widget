from ipywidgets import VBox, Label, Text, Button
from traitlets import directional_link

from lib.view_models.sample_view_model import SampleViewModel

class SampleView(VBox):
    """
    Sample View class subscribing to a SampleViewModel. Represents GUI elements built only with predefined ipywidgets. 
    """

    def __init__(self, sample_vmodel: SampleViewModel):
        super(SampleView, self).__init__()

        # assign model which this class can subscribe to
        self._vmodel = sample_vmodel

        self._title_label = Label(value = 'View created from predefined ipywidgets', disabled=True)

        self._label_1 = Text(description = 'String Value: ', disabled=True)
        self._label_2 = Text(description = 'Integer Value: ', disabled=True)

        self._button = Button(description="Get Data")
        self._button.on_click(self._get_data)

        self.children = [self._title_label, self._label_1, self._label_2, self._button]

        self._set_value_subscriptions()

    def _set_value_subscriptions(self):
        """
        Subscribes to changes of data interface of assigned View Model. 
        """

        directional_link(
            (self._vmodel, 'string_value')
            ,(self._label_1, 'value')
        )

        directional_link(
            (self._vmodel, 'int_value')
            ,(self._label_2, 'value')
            ,lambda x: str(x) or str()
        )

    def _get_data(self, button):
        """
        Calls get_model() method from View Model when assigned button in pressed on the UI screen.
        """
        self._vmodel.get_model()