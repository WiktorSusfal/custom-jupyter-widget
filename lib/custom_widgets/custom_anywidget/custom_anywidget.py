import anywidget
import pathlib
from traitlets import Unicode

dir_path = pathlib.Path( __file__ ).parent.absolute()
jss_path = dir_path.joinpath('custom_anywidget.js')
css_path = dir_path.joinpath('custom_anywidget.css')

class CustomAnyWidget(anywidget.AnyWidget):
    """
    Python class defining custom widget to be used in Jupyter Notebook. 
    Act like an interface for the widget in python code.
    """
    
    # read javascript and css code from associated files
    _esm = jss_path.read_text()
    _css = css_path.read_text()

    text_1 = Unicode('').tag(sync=True)
    text_2 = Unicode('').tag(sync=True)

    def __init__(self, text_1: str = str(), text_2: str = str()):
        super(CustomAnyWidget, self).__init__()
        self.text_1 = text_1
        self.text_2 = text_2