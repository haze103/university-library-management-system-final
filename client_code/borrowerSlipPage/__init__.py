from ._anvil_designer import borrowerSlipPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date
from ..confirmReservation import confirmReservation

class borrowerSlipPage(borrowerSlipPageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.cmdReservationDate.date = date.today() 
        self.cmdReservationDate.enabled = False

    def cmdHomeBtn_click(self, **event_args):
        from ..homePage import homePage
        self.secContentPanel.clear()
        self.secContentPanel.add_component(homePage())

    def cmdConfBtn_click(self, **event_args):
        strUserID = self.txtUniqueID.text.strip()
        strFullName = self.txtFName.text.strip() + " " + self.txtMName.text.strip() + " " + self.txtLName.text.strip()
        intIsbn = self.txtISBN.text.strip()
        strTitle = self.txtBookTitle.text.strip()
        datBorrowed = self.txtDateBorrowed.date

        strResult = anvil.server.call('validate_reservation_details', strUserID, strFullName, intIsbn, strTitle, datBorrowed)

        if strResult == "Valid":
            alert(content="Confirm your reservation", title="Reservation Received")
            self.cmdConfBtn.visible = False
            alert(content=confirmReservation(), title="Confirm your reservation", large=True, buttons=[])
            self.intIsbn = intIsbn  # Store intIsbn for later use
        else:
            alert(strResult)

    def validate_credentials(self, strEmail, strPassword):
      strResult = anvil.server.call("validate_user_credentials", strEmail, strPassword)
      return strResult
      
