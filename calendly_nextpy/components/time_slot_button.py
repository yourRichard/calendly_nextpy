import nextpy as xt
    
def time_slot_button(time):
    return xt.box(
        xt.box(
            xt.text(time,class_name="font-bold text-sky-500"),
            class_name=f"w-44 h-12 p-3 border border-sky-500 cursor-pointer rounded-md hover:bg-sky-100 transition-colors",
        ),
        class_name="m-20"
    )
