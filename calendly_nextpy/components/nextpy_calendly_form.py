import nextpy as xt


def form_calendy(form_1,form1_name,form_2,form2_name):
    return xt.box(
        xt.box(
            xt.text("Enter Detail",class_name="font-bold text-lg"),
            xt.form(
                xt.box(
                    xt.text(form_1,class_name="font-bold mb-2"),
                    xt.input(name=form1_name,class_name="w-10"),
                    class_name="mt-4"
                ),
                xt.box(
                    xt.text(form_2,class_name="font-bold mb-2"),
                    xt.input(name=form2_name,class_name="w-10"),
                    class_name="mt-4"
                ),
                xt.box(
                    xt.box(
                        xt.text("Add Guests",class_name="text-sm text-sky-600"),
                        class_name="w-24 h-8 text-center my-auto rounded-2xl border border-sky-600 pt-1 cursor-pointer hover:bg-sky-100 transition-colors"
                    ),
                    class_name="my-2"
                ),
                xt.box(
                    xt.text("Please share anything that will help prepare for our meeting.",class_name="font-bold mb-2"),
                    xt.text_area(),
                    class_name="mt-4"
                ),
                xt.box(
                    xt.text("By proceeding, you confirm that you have read and agree to Calendly's Terms of Use and Privacy Notice.",class_name="text-sm my-4 w-[80%]")
                ),
                xt.box(
                    xt.text("Schedule Event",class_name="font-bold text-white"),
                    class_name="w-36 h-12 pt-3 cursor-pointer bg-sky-500 rounded-2xl text-center hover:bg-sky-600 transition-colors"
                ),
            ),
        ),
        class_name="p-4 w-[35rem]"
    )