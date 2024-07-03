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

      self.error_label = Label(visible=False, foreground='red')
      self.add_component(self.error_label)

      self.populate_component(self.secDataPanel, 'get_book_list')

    def populate_component(self, component, data_fetch_method):
        try:
            data_list = anvil.server.call(data_fetch_method)

            # Assuming that the component's items can be set
            if isinstance(data_list, list):
                component.items = data_list
            else:
                component.items = []  # Clear the data if data_list is not a list
            
            component.refresh_data_bindings()  # Refresh data bindings after populating
            self.error_label.visible = False  # Hide the error label if no error
        except Exception as e:
            error_message = f"Error occurred while populating component: {e}"
            self.error_label.text = error_message  # Display the error message in the error_label
            self.error_label.visible = True  # Make the error label visible

    def cmdSearchBtn_click(self, **event_args):
      strSearchItem = self.txtSearchBox.text
      self.secDataPanel.items = anvil.server.call('search_books', strSearchItem)

    def cmdHomeBtn_click(self, **event_args):
      from ..homePage import homePage
      self.secContentPanel.clear()
      self.secContentPanel.add_component(homePage())


  
    



    