import customtkinter, requests, modules.app
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont

counter = 0
url_loading = None
point_counter = 0
x1, y1 = None, None
x2, y2 = None, None
mouse_x = None
mouse_y = None

def picture():
    frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 720)
    def url():
        global url_loading
        url_loading = True
        button_file.place_forget()
        button_url.place_forget()
        window.place(x=100, y=150)
        button_open.place(x = 400, y = 150)
    def local_file():
        global url_loading
        url_loading = False
        button_file.place_forget()
        button_url.place_forget()
        pressing_button_file()
        
    
    def pressing_button_url():
        global counter
        try:
            filename = requests.get(url=text.get(), stream=True).raw
            modules.app.main_app.CURRENT_IMAGE = Image.open(filename)                
            counter += 1
            # new_tab = modules.app.main_app.TABVIEW.add(f"Вкладка {counter}")
            b = customtkinter.CTkImage(light_image=modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
            try:
                modules.app.main_app.IMAGE_LABEL.place_forget()
            except AttributeError:
                pass
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=b, width = 450, height = 400)
            modules.app.main_app.IMAGE_LABEL.place(x=150, y=0)
            window.place_forget()
            button_open.place_forget()
            info_frame = customtkinter.CTkFrame(master=modules.app.main_app, width=140, height=100)
            info_frame.place(x=5, y=655)
            info_dict = {
                "Size": modules.app.main_app.CURRENT_IMAGE.size, 
                "Format": modules.app.main_app.CURRENT_IMAGE.format, 
                "Mode": modules.app.main_app.CURRENT_IMAGE.mode
            }
            label_y = 0
            for info in info_dict.items():
                label = customtkinter.CTkLabel(master=info_frame, text=info)
                label.place(x=0, y=label_y)
                label_y += 20
            # return a
        except:
            print("ахахахахха ти какашка")
        
        frame.place_forget()

    def pressing_button_file():
        global counter
        try:
            filename = customtkinter.filedialog.askopenfilename()
            img = Image.open(filename)
            modules.app.main_app.CURRENT_IMAGE = img
            counter += 1
            # new_tab = modules.app.main_app.TABVIEW.add(f"Вкладка {counter}")
            try:
                modules.app.main_app.IMAGE_LABEL.place_forget()
            except AttributeError:
                pass
            b = customtkinter.CTkImage(light_image=img, size = (930, 720))
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=b)
            modules.app.main_app.IMAGE_LABEL.place(x=150, y=0)
            # window.unbind('<Return>')
            info_frame = customtkinter.CTkFrame(master=modules.app.main_app, width=140, height=70)
            info_frame.place(x=5, y=655)
            info_dict = {
                "Size": img.size, 
                "Format": img.format, 
                "Mode": img.mode
            }
            label_y = 0
            for info in info_dict.items():
                label = customtkinter.CTkLabel(master=info_frame, text=info)
                label.place(x=0, y=label_y)
                label_y += 20
            # return a
        except:
            print("ахахахахха ти какашка")
        
        frame.place_forget()
        # window.bind('<Return>', pressing_button)
    
        
    button_file = customtkinter.CTkButton(
        master = frame, 
        width=190, 
        height=100, 
        text="Обрати файл з комп'ютера",
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3,
        command = local_file
    )
    button_url = customtkinter.CTkButton(
        master = frame, 
        width = 190, 
        height = 100, 
        text="URL",
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3,
        command = url
    )   
    button_file.place(x = 5, y = 50)
    button_url.place(x = 5, y = 160)

    frame.place(x = 880, y = 0)
    
    text = customtkinter.StringVar()
    window = customtkinter.CTkEntry(master=modules.app.main_app, width=300, height=50, textvariable=text)
    button_open = customtkinter.CTkButton(
        master=modules.app.main_app, 
        width=150, 
        height=50, 
        text="Відкрити",
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3,
        command = pressing_button_url
    )   

        # Dimka Perdimka

# def save():
def save():
    if modules.app.main_app.CURRENT_IMAGE:
        def finished():             
            try:
                if filename.get() and width_text.get() and height_text.get():
                    width_int = int(width_text.get())
                    height_int = int(height_text.get())
                    a = modules.app.main_app.CURRENT_IMAGE.resize((width_int, height_int))
                    a.save(filename.get())
                    window.place_forget()
            except:
                print("Неправильно заповнено")

        window = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 720, border_width = 3)
        
        filename = customtkinter.StringVar()
        width_text = customtkinter.StringVar()
        height_text = customtkinter.StringVar()
        
        filename_entry = customtkinter.CTkEntry(master=window, width = 190, height = 100, textvariable=filename)
        width_entry = customtkinter.CTkEntry(master=window, width = 190, height = 50, textvariable=width_text)
        height_entry = customtkinter.CTkEntry(master=window, width = 190, height = 50, textvariable=height_text)


        filename_label = customtkinter.CTkLabel(master = window, text = "Ім'я файлу:")
        width_label = customtkinter.CTkLabel(master = window, text = "Ширина зображення:")
        height_label = customtkinter.CTkLabel(master = window, text = "Висота зображення:")

        finish_button = customtkinter.CTkButton(
            master = window,
            width = 190,
            height = 100, 
            text = "Зберегти",
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3, 
            command = finished
        )

        filename_entry.place(x = 5, y = 40)
        filename_label.place(x = 5, y = 5)
        width_entry.place(x=5, y=200)
        width_label.place(x = 5, y = 170)
        height_entry.place(x=5,y=300)
        height_label.place(x = 5, y = 270)
        finish_button.place(x = 5, y = 600)

        window.place(x = 880, y = 0)


def picture_crop():
    if modules.app.main_app.CURRENT_IMAGE:
        frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 720, border_width = 3)

        pointx1 = customtkinter.StringVar()
        pointx2 = customtkinter.StringVar()
        pointy1 = customtkinter.StringVar()
        pointy2 = customtkinter.StringVar()

        entry = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = pointx1) 
        entry2 = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = pointy1) 
        entry3 = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = pointx2) 
        entry4 = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = pointy2)

        left_margin = customtkinter.CTkLabel(master = frame, text = "x1:")
        top_margin = customtkinter.CTkLabel(master = frame, text = "y1:")
        right_margin = customtkinter.CTkLabel(master = frame, text = "x2:")
        bottom_margin = customtkinter.CTkLabel(master = frame, text = "y2:")

        def crop_function():
            modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.crop((int(pointx1.get()), int(pointy1.get()), int(pointx2.get()), int(pointy2.get())))
            img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
            modules.app.main_app.IMAGE_LABEL.place_forget()
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image = img, width = 930, height = 400)
            modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
            frame.place_forget()

        confirm = customtkinter.CTkButton(
            master = frame, width = 190, height = 100, text = "Обрізати", command=crop_function,
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3
        )

        frame.place(x = 880, y = 0)

        entry.place(x = 5, y = 40)
        entry2.place(x = 5, y = 140)
        entry3.place(x = 5, y = 240) 
        entry4.place(x = 5, y = 340)

        left_margin.place(x = 5, y = 5)
        top_margin.place(x = 5, y = 110)
        right_margin.place(x = 5, y = 210)
        bottom_margin.place(x = 5, y = 310)

        confirm.place(x = 5, y = 600)

def filters():
    if modules.app.main_app.CURRENT_IMAGE:
        frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 720)
        def grayscale():
            modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.convert("L")
            img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
            modules.app.main_app.IMAGE_LABEL.place_forget()
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 720)
            modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
            frame.place_forget()

        def blur():
            modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.filter(ImageFilter.BLUR)
            img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
            modules.app.main_app.IMAGE_LABEL.place_forget()
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 720)
            modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
            frame.place_forget()

        def sharpen():
            modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.filter(ImageFilter.SHARPEN)
            img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
            modules.app.main_app.IMAGE_LABEL.place_forget()
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 720)
            modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
            frame.place_forget()

        def smooth():
            modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.filter(ImageFilter.SMOOTH)
            img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
            modules.app.main_app.IMAGE_LABEL.place_forget()
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 720)
            modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
            frame.place_forget()

        def detail():
            modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.filter(ImageFilter.DETAIL)
            img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
            modules.app.main_app.IMAGE_LABEL.place_forget()
            modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 450, height = 720)
            modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
            frame.place_forget()

        grayscale_button = customtkinter.CTkButton(
            master = frame, width = 190, height = 50, text = "Чорно-білий", command=grayscale,
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3
        )

        blur_button = customtkinter.CTkButton(
            master = frame, width = 190, height = 50, text = "Розмиття", command=blur,
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3                                   
        )

        sharpen_button = customtkinter.CTkButton(
            master = frame, width = 190, height = 50, text = "Різкість", command=sharpen,
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3
        )

        smooth_button = customtkinter.CTkButton(
            master = frame, width = 190, height = 50, text = "Згладжування", command=smooth,
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3,                             
        )

        detail_button = customtkinter.CTkButton(
            master = frame, width = 190, height = 50, text = "Деталізація", command=detail,
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3
        )

        grayscale_button.place(x = 5, y = 20)
        blur_button.place(x = 5, y = 80)
        sharpen_button.place(x = 5, y = 140)
        smooth_button.place(x = 5, y = 200)
        detail_button.place(x = 5, y = 260)

        frame.place(x = 880, y = 0)

def rotate():
    if modules.app.main_app.CURRENT_IMAGE:
        modules.app.main_app.CURRENT_IMAGE = modules.app.main_app.CURRENT_IMAGE.rotate(90)
        img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (720, 930))
        modules.app.main_app.IMAGE_LABEL.place_forget()
        modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width = 930, height = 720)
        modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)

# snus kriminal papararara

def text():
    if modules.app.main_app.CURRENT_IMAGE and modules.app.main_app.IMAGE_LABEL:
        frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 720, border_width = 3)
        
        text_entry = customtkinter.StringVar()
        size_entry_text = customtkinter.StringVar()
        color_entry_text = customtkinter.StringVar()

        entry = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = text_entry) 
        size_entry = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = size_entry_text) 
        color_entry = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = color_entry_text)

        entry.place(x = 5, y = 40) 
        size_entry.place(x = 5, y = 130)
        color_entry.place(x = 5, y = 220)

        text_label = customtkinter.CTkLabel(master = frame, text = "Текст:")
        size_label = customtkinter.CTkLabel(master = frame, text = "Розмір тексту:")
        color_label = customtkinter.CTkLabel(master = frame, text = "HEX-колір:")

        text_label.place(x = 5, y = 10)
        size_label.place(x = 5, y = 100)
        color_label.place(x = 5, y = 190)



        def mouse_pressed(event):
            global mouse_x, mouse_y
            try:
                frame.place_forget()
            except:
                pass
            
            mouse_x = event.x
            mouse_y = event.y
            print(mouse_x, mouse_y)
            
            frame.place(x = 880, y = 0)

        def entry_pressed():
            if text_entry.get() and size_entry_text.get() and color_entry_text.get():
                font = ImageFont.truetype("arial.ttf", size = int(size_entry_text.get()))
                temp = ImageDraw.Draw(modules.app.main_app.CURRENT_IMAGE)
                print(modules.app.main_app.CURRENT_IMAGE)
                temp.text((float(mouse_x), float(mouse_y)), text_entry.get(), font= font, fill = color_entry_text.get())
                print(modules.app.main_app.CURRENT_IMAGE)
                # modules.app.main_app.CURRENT_IMAGE.save("temp.png")
                # modules.app.main_app.CURRENT_IMAGE = Image.open("temp.png")
                img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
                modules.app.main_app.IMAGE_LABEL.place_forget()
                modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image = img, width = 450, height = 400)
                modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
                frame.place_forget()

        # frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 400, border_width = 3)
        confirm_button = customtkinter.CTkButton(
            master = frame, width = 190, height = 100, text = "Підтвердити", command=entry_pressed,
            fg_color = "#302f2b",
            border_color = "#d36f23",
            hover_color = "#c67538",
            border_width = 3
        )
        confirm_button.place(x = 5, y = 600)

        modules.app.main_app.IMAGE_LABEL.bind("<Button-1>", mouse_pressed)
            


def new_picture():
    frame = customtkinter.CTkFrame(master=modules.app.main_app, width=200, height=720)
    
    width_var = customtkinter.StringVar()
    height_var = customtkinter.StringVar()
    
    size_entry1 = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = width_var)
    size_entry2 = customtkinter.CTkEntry(master = frame, width = 190, height = 50, textvariable = height_var)



    # if width_var.get() and height_var.get():
    new_image = Image.new('RGBA', (930, 720), 'white')
    modules.app.main_app.CURRENT_IMAGE = new_image
    img = customtkinter.CTkImage(light_image=modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
    try:
        modules.app.main_app.IMAGE_LABEL.place_forget()
    except AttributeError: 
        pass
    modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image=img, width=450, height=720)
    modules.app.main_app.IMAGE_LABEL.place(x=150, y=0)
    # frame.place_forget()   
    info_frame = customtkinter.CTkFrame(master=modules.app.main_app, width=140, height=100)
    info_frame.place(x=5, y=655)
    info_dict = {
        "Size": modules.app.main_app.CURRENT_IMAGE.size, 
        "Format": modules.app.main_app.CURRENT_IMAGE.format, 
        "Mode": modules.app.main_app.CURRENT_IMAGE.mode
    }
    label_y = 0
    for info in info_dict.items():
        label = customtkinter.CTkLabel(master=info_frame, text=info)
        label.place(x=0, y=label_y)
        label_y += 20

def draw():
    frame = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 720, border_width = 3)
    frame.place(x = 880, y = 0)

    def draw_oval():    
        frame.place_forget()
        frame_width = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 720, border_width = 3)

        width_value = customtkinter.StringVar()
        width_entry = customtkinter.CTkEntry(master = frame_width, width = 190, height = 50, textvariable = width_value)
        
        color_value = customtkinter.StringVar()
        color_entry = customtkinter.CTkEntry(master = frame_width, width = 190, height = 50, textvariable = color_value)

        width_label = customtkinter.CTkLabel(master = frame_width, text = "Ширина кола:")
        color_label = customtkinter.CTkLabel(master = frame_width, text = "Колір кола:")


        def draw_oval2(event):
            if width_value.get() and color_value.get():
                draw1 = ImageDraw.Draw(modules.app.main_app.CURRENT_IMAGE)
                draw1.ellipse([(event.x, event.y), (event.x + int(width_value.get()), event.y + int(width_value.get()))], fill = color_value.get())
                img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
                try:
                    modules.app.main_app.IMAGE_LABEL.place_forget()
                except:
                    pass

                modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image = img, width = 930, height = 720)
                modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
                frame_width.place_forget()

        modules.app.main_app.IMAGE_LABEL.bind("<Button-1>", draw_oval2)

        width_label.place(x = 5, y = 50)
        color_label.place(x = 5, y = 160)

        
        width_entry.place(x = 5, y = 90)
        color_entry.place(x = 5, y = 200)
        
        frame_width.place(x = 880, y = 0)

    def draw_rectangle():  
        frame.place_forget()
        frame_width = customtkinter.CTkFrame(master = modules.app.main_app, width = 200, height = 720, border_width = 3)

        height_value = customtkinter.StringVar()
        height_entry = customtkinter.CTkEntry(master = frame_width, width = 190, height = 50, textvariable = height_value)
        
        width_value = customtkinter.StringVar()
        width_entry = customtkinter.CTkEntry(master = frame_width, width = 190, height = 50, textvariable = width_value)

        color_value = customtkinter.StringVar()
        color_entry = customtkinter.CTkEntry(master = frame_width, width = 190, height = 50, textvariable = color_value)

        width_label = customtkinter.CTkLabel(master = frame_width, text = "Ширина:")
        height_label = customtkinter.CTkLabel(master = frame_width, text = "Висота:")
        color_label = customtkinter.CTkLabel(master = frame_width, text = "Колір:")

        def draw_rectangle2(event):
            if width_value.get() and color_value.get() and height_value.get():
                draw1 = ImageDraw.Draw(modules.app.main_app.CURRENT_IMAGE)
                draw1.rectangle([(event.x, event.y), (event.x + int(width_value.get()), event.y + int(height_value.get()))], fill = color_value.get())
                img = customtkinter.CTkImage(light_image = modules.app.main_app.CURRENT_IMAGE, size = (930, 720))
                try:
                    modules.app.main_app.IMAGE_LABEL.place_forget()
                except:
                    pass

                modules.app.main_app.IMAGE_LABEL = customtkinter.CTkLabel(master=modules.app.main_app, text=" ", image = img, width = 930, height = 720)
                modules.app.main_app.IMAGE_LABEL.place(x = 150, y = 0)
                frame_width.place_forget()
    
        modules.app.main_app.IMAGE_LABEL.bind("<Button-1>", draw_rectangle2)

        width_label.place(x = 5, y = 50)
        color_label.place(x = 5, y = 160)
        height_label.place(x = 5, y = 270)

        width_entry.place(x = 5, y = 90)
        color_entry.place(x = 5, y = 200)
        height_entry.place(x = 5, y = 310)
        frame_width.place(x = 880, y = 0)

        
    button_oval = customtkinter.CTkButton(
        master = frame, width = 190, height = 100, text = "Овал", command=draw_oval,
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3
    )
    
    button_oval.place(x = 5, y = 50)
    
    button_rectangle = customtkinter.CTkButton(
        master = frame, width = 190, height = 100, text = "Прямокутник", command=draw_rectangle,
        fg_color = "#302f2b",
        border_color = "#d36f23",
        hover_color = "#c67538",
        border_width = 3
    )
    button_rectangle.place(x = 5, y = 160)