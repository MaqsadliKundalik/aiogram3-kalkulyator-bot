from aiogram.types import CallbackQuery

import keyboards


async def callback_answer(callback: CallbackQuery):


    if callback.message.text == "|":
        if callback.data in "DC": await callback.answer(f"❗ O'chirish uchun ifoda mavjud emas!", show_alert=True)
        elif callback.data in "+-*/=,":
            await callback.answer(f"❗ Siz ifodani {callback.data} belgisi bilan boshlay olmaysiz", show_alert=True)
        else:
            await callback.message.edit_text(callback.data + callback.message.text)

            await callback.message.edit_reply_markup(
                reply_markup=keyboards.calc_builder
            )
    else:
        if callback.data == "D":
            await callback.message.edit_text(callback.message.text[:-2] + "|", reply_markup=keyboards.calc_builder)
        elif callback.data == "C":
            await callback.message.edit_text("|", reply_markup=keyboards.calc_builder)

        elif (callback.message.text[-2].isdigit()) and callback.data == "=" and ("+" in callback.message.text or "-" in callback.message.text or "*" in callback.message.text or "/" in callback.message.text):
            ifoda = callback.message.text.replace(",", ".")

            await callback.message.edit_text(
                str(eval(ifoda[:-1])) + "|"
            )
            await callback.message.edit_reply_markup(
                reply_markup=keyboards.calc_builder
            )
        elif callback.data == "=":
            await callback.answer("❗ Ifoda to'liq emas!", show_alert=True)

        elif callback.message.text[-2].isdigit() or callback.data.isdigit():
            await callback.message.edit_text(
                callback.message.text[:-1] + callback.data + callback.message.text[-1],
            )
            await callback.message.edit_reply_markup(
                reply_markup=keyboards.calc_builder
            )
        elif callback.data in "+-*/":
            await callback.message.edit_text(
                callback.message.text[:-2] + callback.data + "|",
                reply_markup=keyboards.calc_builder
            )
        elif callback.data == ",":
            await callback.answer("❗Noto'g'ri buyruq!", show_alert=True)


