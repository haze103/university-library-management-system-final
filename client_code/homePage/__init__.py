from ._anvil_designer import homePageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..borrowerSlipPage import borrowerSlipPage
from ..adminIDConf import adminIDConf

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

  def cmdAdminBtn_click(self, **event_args):
    alert(content=adminIDConf(), title="Confirm your access level", large=True, buttons=[])
    strEmail = self.txtEmail.text.strip()
    strPassword = self.txtPassword.text.strip()

    if self.validate_credentials(strEmail, strPassword):
        intISBN = # Replace this with the ISBN of the reserved book
        intBookID = anvil.server.call('get_book_id_from_isbn', intISBN)

        if intBookID is not None:
            if anvil.server.call('update_reservation_tables', strEmail, intBookID):
                alert("Reservation Confirmed")
                return True
            else:
                alert("Failed to update reservation tables. Please try again.")
        else:
            alert("Book ID not found for the given ISBN.")
    else:
        alert("Invalid email or password. Please try again.")