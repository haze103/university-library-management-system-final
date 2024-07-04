from ._anvil_designer import cancelReservationTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date
from ..confirmReservation import confirmReservation


class cancelReservation(cancelReservationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.txtDateCancelled.date = date.today()
    self.txtDateCancelled.enabled = False

  def cmdHomeBtn_click(self, **event_args):
    from ..homePage import homePage
    self.secContentPanel.clear()
    self.secContentPanel.add_component(homePage())

  def cmdConfBtn_click(self, **event_args):
    intReservationLogID = self.txtReservationLogID.text.strip()
    strISBN = self.txtISBN.text.strip()
    datCancelled = self.txtDatPayment.date
    
    anvil.server.call('cancel_reservation', intReservationLogID, strISBN, datCancelled)




