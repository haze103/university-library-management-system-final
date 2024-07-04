from ._anvil_designer import updateBorrowerLogTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class updateBorrowerLog(updateBorrowerLogTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def validate_credentials(self, strAdmin, strBorrowerLogID, datDue):
    result = anvil.server.call("validate_user_credentials", strAdmin, strBorrowerLogID, datDue)
    return result

  def cmdConfirmBtn_click(self, **event_args):
    strAdmin = self.txtAdminID.text.strip()
    strBorrowerLogID = self.txtBorrowerLogID.text.strip()
    datDue = self.txtDateToRet.date

    if self.validate_credentials(strAdmin, strBorrowerLogID, datDue):
      alert("Successfully Updated!")
      return True
    else:
      alert("Error Updating!")
