import nextpy as xt
from calendly_nextpy.components.nextpy_calendly_form import form_calendy
from calendly_nextpy.components.time_slot_button import time_slot_button

def index() -> xt.Component:
    return xt.box(
         form_calendy(form_1="Name *",form1_name="first_name",form_2="Gmail *",form2_name="account"),
        time_slot_button("11:30")
    )



app = xt.App()
app.add_page(index)
