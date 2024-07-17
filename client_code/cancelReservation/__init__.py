from ._anvil_designer import cancelReservationTemplate
from anvil import *
import anvil.server
from datetime import datetime
from ..confirmReservation import confirmReservation


class cancelReservation(cancelReservationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.txtDateCancelled.date = datetime.now()
    self.txtDateCancelled.enabled = False

  def cmdHomeBtn_click(self, **event_args):
    from ..homePage import homePage
    self.secContentPanel.clear()
    self.secContentPanel.add_component(homePage())

  def cmdConfBtn_click(self, **event_args):
    intReservationLogID = self.txtReservationLogID.text.strip()
    strISBN = self.txtISBN.text.strip()
    datCancelled = self.txtDateCancelled.date
    
    result = anvil.server.call('cancel_reservation', intReservationLogID, strISBN, datCancelled)

    if result == "Valid":
       alert(content="Your reservation is now cancelled.", title="Reservation Cancelled")
    else:
        alert(result)
