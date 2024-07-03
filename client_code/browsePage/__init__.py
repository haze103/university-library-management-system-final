from ._anvil_designer import browsePageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class browsePage(browsePageTemplate):
    def __init__(self, **properties):
      # Set Form properties and Data Bindings.
      self.init_components(**properties)

      self.populate_component(self.secDataPanel, 'get_book_list')

    def populate_component(self, component, data_fetch_method):
        try:
            data_list = anvil.server.call(data_fetch_method)
        
            # Assuming that the component's items can be set
            if isinstance(data_list, list):
                component.items = data_list
            else:
                component.items = []  # Clear the data if data_list is not a list
        except Exception as e:
            print("Error occurred while populating component:", e)

    def cmdSearchBtn_click(self, **event_args):
      strSearchItem = self.txtSearchBox.text
      self.secDataPanel.items = anvil.server.call('search_books', strSearchItem)

    def cmdHomeBtn_click(self, **event_args):
      from ..homePage import homePage
      self.secContentPanel.clear()
      self.secContentPanel.add_component(homePage())


  
    



    