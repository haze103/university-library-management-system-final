from ._anvil_designer import updateBorrowerLogStatusTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..payFees import payFees


class updateBorrowerLogStatus(updateBorrowerLogStatusTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.txtDatLost.visible = False
    self.lblDatReportLost.visible = False
    self.cmdPayBtn.visible = False

  def validate_credentials(self, intBorrowerLogID, dtmReturned, strBorrowerStatusCode):
    result = anvil.server.call("update_existing_borrower_log_status", intBorrowerLogID, dtmReturned, strBorrowerStatusCode)
    return result

  def cmdConfirmBtn_click(self, **event_args):
    intBorrowerLogID = self.txtBorrowerLogID.text.strip()
    strBorrowerStatusCode = self.txtBorrowerStat.selected_value
    dtmReturned = self.txtRetDate.date

    if self.validate_credentials(intBorrowerLogID, dtmReturned, strBorrowerStatusCode):
      alert("Successfully Updated!")
      return True
    else:
      alert("Error Updating!")

  def show_payment(self, strBorrowerStatus):
    if strBorrowerStatus == 'Lost':
      self.txtDatLost.visible = True
      self.lblDatReportLost.visible = True
      self.cmdPayBtn.visible = True

      datLost = self.txtDatLost.date
      intBorrowerLogStatusID = self.txtBorrowerLogStatusID.text.strip()
      
      anvil.server.call('update_lost_status', intBorrowerLogStatusID, datLost)

  def cmdPayBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(payFees())

  def cmdHomeBtn_click(self, **event_args):
    from ..adminHome import adminHome
    self.secContentPanel.clear()
    self.secContentPanel.add_component(adminHome())
      