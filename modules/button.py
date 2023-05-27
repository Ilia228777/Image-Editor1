import customtkinter, modules.app, modules.button_functions

open_picture = customtkinter.CTkButton(
    master = modules.app.main_app.FILE, 
    width = 100, 
    height = 50, 
    command = modules.button_functions.picture, 
    border_width= 3,
    text = "Відкрити",
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538"
)

save_picture = customtkinter.CTkButton(
    master = modules.app.main_app.FILE, 
    width = 100, 
    height = 50, 
    command = modules.button_functions.save, 
    border_width= 3,
    text = "Зберегти",
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538"
)

crop = customtkinter.CTkButton(
    master=modules.app.main_app.TOOLS,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=50,
    text="Обрiзати",
    border_width=3,
    command = modules.button_functions.picture_crop
)

filters = customtkinter.CTkButton(
    master=modules.app.main_app.TOOLS,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=50,
    text="Фiльтри",
    border_width=3,
    command = modules.button_functions.filters
)

rotate = customtkinter.CTkButton(
    master=modules.app.main_app.TOOLS,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=50,
    text="Поворот",
    border_width=3,
    command = modules.button_functions.rotate
)

write = customtkinter.CTkButton(
    master=modules.app.main_app.TOOLS,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=50,
    text="Текст",
    border_width=3,
    command = modules.button_functions.text
)

new_picture = customtkinter.CTkButton(
    master=modules.app.main_app.FILE,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=50,
    text="Нова картинка",
    border_width=3,
    command = modules.button_functions.new_picture
)

draw = customtkinter.CTkButton(
    master=modules.app.main_app.TOOLS,
    fg_color = "#302f2b",
    border_color = "#d36f23",
    hover_color = "#c67538",
    width=100,
    height=50,
    text="Малювати",
    border_width=3,
    command = modules.button_functions.draw
)

open_picture.place(x=20, y=80)
save_picture.place(x=20, y=140)
crop.place(x=20, y=200)
filters.place(x=20, y=140)
rotate.place(x=20, y=80)
write.place(x=20, y=20)
new_picture.place(x=20, y=20)
draw.place(x=20, y=260)