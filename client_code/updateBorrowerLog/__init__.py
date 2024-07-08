from ._anvil_designer import updateBorrowerLogTemplate
from anvil import *
import anvil.server
from datetime import date


class updateBorrowerLog(updateBorrowerLogTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def validate_credentials(self, intReservationLogID, datDue, intAdminID):
    result = anvil.server.call("update_existing_borrower_log", intReservationLogID, datDue, intAdminID)
    return result

  def cmdConfirmBtn_click(self, **event_args):
    intAdminID = self.txtAdminID.text.strip()
    intReservationLogID = self.txtReservationLogID.text.strip()
    datDue = self.txtDateToRet.date

    if self.validate_credentials(intReservationLogID, datDue, intAdminID):
      alert("Successfully Updated!")
      return True
    else:
      alert("Error Updating!")

  def cmdHomeBtn_click(self, **event_args):
    from ..adminHome import adminHome
    self.secContentPanel.clear()
    self.secContentPanel.add_component(adminHome())
