from ._anvil_designer import adminSignInTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..adminPage import adminPage

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
      self.secContentPanel.add_component(adminPage())
    else:
      alert("Invalid email or password. Please try again.")
