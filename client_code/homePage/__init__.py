from ._anvil_designer import homePageTemplate
from anvil import *
import anvil.server
from ..cancelReservation import cancelReservation
from ..borrowerSlipPage import borrowerSlipPage

class homePage(homePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def cmdBooksBtn_click(self, **event_args):
    from ..browsePage import browsePage
    self.secContentPanel.clear()
    self.secContentPanel.add_component(browsePage())

  def cmdReserveBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(borrowerSlipPage())

  def cmdCancelBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(cancelReservation())