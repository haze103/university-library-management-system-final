from ._anvil_designer import basePageTemplate
from anvil import *
import anvil.server
from ..homePage import homePage
from ..adminSignIn import adminSignIn

class basePage(basePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.secContentPanel.add_component(homePage())

  def cmdAdminBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(adminSignIn())
