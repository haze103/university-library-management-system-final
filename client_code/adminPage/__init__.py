from ._anvil_designer import adminPageTemplate
from anvil import *
import anvil.server


class adminPage(adminPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.dataPanel.items = anvil.server.call('get_reservation_log_list')
    self.dataPanel1.items = anvil.server.call('get_borrower_log_list')
    self.dataPanel2.items = anvil.server.call('get_borrower_log_status_list')

  def cmdHomeBtn_click(self, **event_args):
    from ..adminHome import adminHome
    self.secContentPanel.clear()
    self.secContentPanel.add_component(adminHome())

  