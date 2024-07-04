from ._anvil_designer import borrowerSlipPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date

class borrowerSlipPage(borrowerSlipPageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.cmdReservationDate.date = date.today() 
        self.cmdReservationDate.enabled = False
        self.secPopUp.visible = False

    def cmdHomeBtn_click(self, **event_args):
        from ..homePage import homePage
        self.secContentPanel.clear()
        self.secContentPanel.add_component(homePage())

    def validate_credentials(self, strEmail, strPassword):
        result = anvil.server.call('validate_user_credentials', strEmail, strPassword)
        return result

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
            self.secPopUp.visible = True
            self.intIsbn = intIsbn  # Store intIsbn for later use
        else:
            alert(strResult)

    def cmdConfirmBtn_click(self, **event_args):
        strEmail = self.txtEmail.text.strip()
        strPassword = self.txtPassword.text.strip()

        if self.validate_credentials(strEmail, strPassword):
            intBookID = self.get_book_id(self.intIsbn)  # Get the intBookID based on the intISBN entered
            if intBookID:
                if anvil.server.call('update_reservation_tables', strEmail, intBookID):
                    alert("Reservation Confirmed")
                else:
                    alert("Failed to update reservation tables.")
            else:
                alert("Book not found or invalid ISBN.")
        else:
            alert("Invalid email or password. Please try again.")
