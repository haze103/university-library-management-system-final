from ._anvil_designer import updateBorrowerLogStatusTemplate
from anvil import *
import anvil.server
from ..payFees import payFees
from datetime import date

class updateBorrowerLogStatus(updateBorrowerLogStatusTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.txtDatLost.visible = False
    self.lblDatReportLost.visible = False
    self.cmdPayBtn.visible = False

  def validate_credentials(self, intBorrowerLogID, dtmReturned, strStatusName):
    result = anvil.server.call("update_existing_borrower_log_status", intBorrowerLogID, dtmReturned, strStatusName)
    return result

  def cmdConfirmBtn_click(self, **event_args):
    intBorrowerLogID = self.txtBorrowerLogID.text.strip()
    strStatusName = self.txtBorrowerStat.selected_value
    dtmReturned = self.txtRetDate.date

    if self.validate_credentials(intBorrowerLogID, dtmReturned, strStatusName) is True:
      alert("Successfully Updated!")
      self.show_payment(strStatusName)
    else:
      alert(self.validate_credentials(intBorrowerLogID, dtmReturned, strStatusName))

  def show_payment(self, strStatusName):
    if strStatusName == 'Lost':
      self.txtDatLost.visible = True
      self.lblDatReportLost.visible = True
      self.cmdPayBtn.visible = True
      self.cmdConfirmBtn.enabled = False

  def cmdPayBtn_click(self, **event_args):
    datLost = self.txtDatLost.date
    intBorrowerLogID = self.txtBorrowerLogID.text.strip()

    result = anvil.server.call('update_lost_status', intBorrowerLogID, datLost)
    
    if result is True:
        alert("Successfully updated.")
        self.secContentPanel.clear()
        self.secContentPanel.add_component(payFees())
    else:
        alert(result)


  def cmdHomeBtn_click(self, **event_args):
    from ..adminHome import adminHome
    self.secContentPanel.clear()
    self.secContentPanel.add_component(adminHome())
      