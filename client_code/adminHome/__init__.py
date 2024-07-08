from ._anvil_designer import adminHomeTemplate
from anvil import *
import anvil.server
from ..updateBorrowerLog import updateBorrowerLog
from ..updateBorrowerLogStatus import updateBorrowerLogStatus
from ..adminPage import adminPage
from ..payFees import payFees


class adminHome(adminHomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def cmdUpdateRetDate_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(updateBorrowerLog())

  def cmdUpdateTrans_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(updateBorrowerLogStatus())

  def cmdCancelBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(adminPage())

  def cmdPayBtn_click(self, **event_args):
    self.secContentPanel.clear()
    self.secContentPanel.add_component(payFees())



  
 
