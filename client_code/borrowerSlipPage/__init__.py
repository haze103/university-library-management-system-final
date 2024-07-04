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
        self.txtReservationDate.date = date.today() 
        self.txtReservationDate.enabled = False

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
        datReserved = self.txtReservationDate.date
        strEmail = self.txtEmail.text.strip()
        strPassword = self.txtPassword.text.strip()

        strResult = anvil.server.call('validate_reservation_details', strUserID, strFullName, intIsbn, strTitle, datBorrowed, datReserved, strEmail, strPassword)

        if strResult == "Valid":
            alert(content="Please claim the book on your reserved date. Thank you!", title="Reservation Confirmed")
            self.txtUniqueID.text = ""
            self.txtFName.text = ""
            self.txtMName.text = ""
            self.txtLName.text = ""
            self.txtISBN.text = ""
            self.txtBookTitle.text = ""
            self.txtDateBorrowed.date = None  # Set the date to None to clear it
            self.txtEmail.text = ""
            self.txtPassword.text = ""
        else:
            alert(strResult)
      
