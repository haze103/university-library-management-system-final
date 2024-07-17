from ._anvil_designer import adminSignInTemplate
from anvil import *
import anvil.server
from ..adminHome import adminHome

class adminSignIn(adminSignInTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def validate_credentials(self, strAdminID, strEmail, strPassword):
    strResult = anvil.server.call("validate_admin_credentials", strAdminID, strEmail, strPassword)
    return strResult

  def cmdConfirmBtn_click(self, **event_args):
    strAdminID = self.txtAdminID.text.strip()
    strEmail = self.txtEmail.text.strip()
    strPassword = self.txtPassword.text.strip()

    if self.validate_credentials(strAdminID, strEmail, strPassword):
      alert(title = "Access Granted. ", content = "You now have access to admin page", buttons=[])
      self.secContentPanel.clear()
      self.secContentPanel.add_component(adminHome())
    else:
      alert("Invalid credentials. Please try again.")
