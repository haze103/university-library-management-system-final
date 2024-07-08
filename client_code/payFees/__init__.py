from ._anvil_designer import payFeesTemplate
from anvil import *
import anvil.server
from datetime import date


class payFees(payFeesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

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

  def cmdHomeBtn_click(self, **event_args):
    from ..adminHome import adminHome
    self.secContentPanel.clear()
    self.secContentPanel.add_component(adminHome())
