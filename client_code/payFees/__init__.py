from ._anvil_designer import payFeesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class payFees(payFeesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.secPopUp1.visible = False
    self.lblDatReportLost.visible = False

  def validate_credentials(self, intLostStatID, strPaymentMethod, datPayment):
    result = anvil.server.call("update_payment", intLostStatID, strPaymentMethod, datPayment)
    return result

  def cmdConfirmBtn_click(self, **event_args):
    intLostStatID = self.txtLostStatID.text.strip()
    strPaymentMethod = self.txtPaymentMethod.selected_value
    datPayment = self.txtDatPayment.date

    if self.validate_credentials(intLostStatID, strPaymentMethod, datPayment):
      alert("Payment Successful!")
      return True
    else:
      alert("Payment Error!")
