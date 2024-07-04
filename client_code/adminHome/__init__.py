from ._anvil_designer import adminHomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..borrowerSlipPage import borrowerSlipPage


class adminHome(adminHomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def cmdUBorrowerLogBtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass