from traitlets import HasTraits, Int, Unicode, Instance, observe

from lib.models.sample_model import SampleModel

class SampleViewModel(HasTraits):
    """
    Sample View Model class, preparing data from assigned Model to be displayed in View. 
    """

    # traitlet interface to communicate with View class - a View can subscribe to these attributes
    string_value = Unicode(default_value=str())
    int_value = Int(default_value=0)

    # traitlet for subscribing to the assigned Model class' changes - for internal logic purposes
    model = Instance(klass=SampleModel, default_value=SampleModel())

    def __init__(self):
        super(SampleViewModel, self).__init__()
        self._model: SampleModel = SampleModel()

    @observe("model")
    def _model_changed(self, change):
        """
        Method called always when "model" traitlet changes. So there is no need to manually call this method
        in every other one which modifies the "model" traitlet. 

        Regardless of the reason of changing "model" traitlet, the interface to communicate with View will be updated.
        """
        new_model: SampleModel = change['new']

        self.string_value = new_model.var_1
        self.int_value = new_model.var_2

    def get_model(self):
        """
        Method exposed to be used by particular View class - refreshes the data interface.
        """
        self._model = SampleModel()
        self.model = self._model