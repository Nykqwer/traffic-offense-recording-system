
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def view_info():
    viewInfo()
    
    
class viewInfo(Frame):
       def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        
        self.data = {
            "id": StringVar(),
            "d_name": StringVar(), 
            "d_license": StringVar(),
            "address": StringVar(),
            "p_no": StringVar(),
            "email": StringVar(),
            "v_reg": StringVar(),
            "v_model": StringVar(),
            "v_no": StringVar(),
            "off_name": StringVar(),
            "e_agency": StringVar(),
            "offense": StringVar(),
            "date": StringVar(),
            "time": StringVar(),
            "location": StringVar(),
            "description": StringVar(),
            "off_code": StringVar(),
            "court_no": StringVar(),
            "hearing_date": StringVar(),
            "outcome": StringVar(),
            "fines": StringVar(),
            "payment": StringVar()
        }

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 644,
            width = 1200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            600.0,
            321.0,
            image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("view"),
            relief="flat"
        )
        button_1.place(
            x=1043.0,
            y=33.0,
            width=123.0,
            height=62.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            600.0,
            364.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            600.0,
            205.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            597.0,
            433.0,
            image=self.image_image_4
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            291.0,
            332.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            textvariable=self.data["d_name"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_1.place(
            x=168.0,
            y=322.0,
            width=246.0,
            height=19.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            291.0,
            373.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            self,
            bd=0,
            textvariable=self.data["d_license"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_2.place(
            x=168.0,
            y=363.0,
            width=246.0,
            height=19.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            291.0,
            413.5,
            image=entry_image_3
        )
        entry_3 = Entry(
            self,
            bd=0,
            textvariable=self.data["address"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_3.place(
            x=168.0,
            y=403.0,
            width=246.0,
            height=19.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            291.0,
            453.5,
            image=entry_image_4
        )
        entry_4 = Entry(
            self,
            bd=0,
            textvariable=self.data["p_no"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_4.place(
            x=168.0,
            y=443.0,
            width=246.0,
            height=19.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            291.0,
            492.5,
            image=entry_image_5
        )
        entry_5 = Entry(
            self,
            bd=0,
            textvariable=self.data["email"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_5.place(
            x=168.0,
            y=482.0,
            width=246.0,
            height=19.0
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
            291.0,
            533.5,
            image=entry_image_6
        )
        entry_6 = Entry(
            self,
            bd=0,
            textvariable=self.data["v_reg"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_6.place(
            x=168.0,
            y=523.0,
            width=246.0,
            height=19.0
        )

        entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(
            291.0,
            575.5,
            image=entry_image_7
        )
        entry_7 = Entry(
            self,
            bd=0,
            textvariable=self.data["v_model"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_7.place(
            x=168.0,
            y=565.0,
            width=246.0,
            height=19.0
        )

        entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_8.png"))
        entry_bg_8 = self.canvas.create_image(
            600.0,
            332.5,
            image=entry_image_8
        )
        entry_8 = Entry(
            self,
            bd=0,
            textvariable=self.data["v_no"],
            bg="#FFFFFF",
            justify='center',
            fg="#000716",
            highlightthickness=0
        )
        entry_8.place(
            x=477.0,
            y=322.0,
            width=246.0,
            height=19.0
        )

        entry_image_9 = PhotoImage(
            file=relative_to_assets("entry_9.png"))
        entry_bg_9 = self.canvas.create_image(
            600.0,
            373.5,
            image=entry_image_9
        )
        entry_9 = Entry(
            self,
            bd=0,
            textvariable=self.data["off_name"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_9.place(
            x=477.0,
            y=363.0,
            width=246.0,
            height=19.0
        )

        entry_image_10 = PhotoImage(
            file=relative_to_assets("entry_10.png"))
        entry_bg_10 = self.canvas.create_image(
            600.0,
            413.5,
            image=entry_image_10
        )
        entry_10 = Entry(
            self,
            bd=0,
            textvariable=self.data["e_agency"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_10.place(
            x=477.0,
            y=403.0,
            width=246.0,
            height=19.0
        )

        entry_image_11 = PhotoImage(
            file=relative_to_assets("entry_11.png"))
        entry_bg_11 = self.canvas.create_image(
            600.0,
            453.5,
            image=entry_image_11
        )
        entry_11 = Entry(
            self,
            textvariable=self.data["offense"],
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_11.place(
            x=477.0,
            y=443.0,
            width=246.0,
            height=19.0
        )

        entry_image_12 = PhotoImage(
            file=relative_to_assets("entry_12.png"))
        entry_bg_12 = self.canvas.create_image(
            600.0,
            492.5,
            image=entry_image_12
        )
        entry_12 = Entry(
            self,
            textvariable=self.data["date"],
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_12.place(
            x=477.0,
            y=482.0,
            width=246.0,
            height=19.0
        )

        entry_image_13 = PhotoImage(
            file=relative_to_assets("entry_13.png"))
        entry_bg_13 = self.canvas.create_image(
            600.0,
            533.5,
            image=entry_image_13
        )
        entry_13 = Entry(
            self,
            textvariable=self.data["time"],
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_13.place(
            x=477.0,
            y=523.0,
            width=246.0,
            height=19.0
        )

        entry_image_14 = PhotoImage(
            file=relative_to_assets("entry_14.png"))
        entry_bg_14 = self.canvas.create_image(
            600.0,
            575.5,
            image=entry_image_14
        )
        entry_14 = Entry(
            self,
            bd=0,
            textvariable=self.data["location"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_14.place(
            x=477.0,
            y=565.0,
            width=246.0,
            height=19.0
        )

        entry_image_15 = PhotoImage(
            file=relative_to_assets("entry_15.png"))
        entry_bg_15 = self.canvas.create_image(
            907.0,
            575.5,
            image=entry_image_15
        )
        entry_15 = Entry(
            self,
            bd=0,
            textvariable=self.data["payment"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_15.place(
            x=784.0,
            y=565.0,
            width=246.0,
            height=19.0
        )

        entry_image_16 = PhotoImage(
            file=relative_to_assets("entry_16.png"))
        entry_bg_16 = self.canvas.create_image(
            907.0,
            533.5,
            image=entry_image_16
        )
        entry_16 = Entry(
            self,
            bd=0,
            textvariable=self.data["fines"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_16.place(
            x=784.0,
            y=523.0,
            width=246.0,
            height=19.0
        )

        entry_image_17 = PhotoImage(
            file=relative_to_assets("entry_17.png"))
        entry_bg_17 = self.canvas.create_image(
            907.0,
            492.5,
            image=entry_image_17
        )
        entry_17 = Entry(
            self,
            bd=0,
            textvariable=self.data["outcome"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_17.place(
            x=784.0,
            y=482.0,
            width=246.0,
            height=19.0
        )

        entry_image_18 = PhotoImage(
            file=relative_to_assets("entry_18.png"))
        entry_bg_18 = self.canvas.create_image(
            907.0,
            453.5,
            image=entry_image_18
        )
        entry_18 = Entry(
            self,
            bd=0,
            textvariable=self.data["hearing_date"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_18.place(
            x=784.0,
            y=443.0,
            width=246.0,
            height=19.0
        )

        entry_image_19 = PhotoImage(
            file=relative_to_assets("entry_19.png"))
        entry_bg_19 = self.canvas.create_image(
            907.0,
            413.5,
            image=entry_image_19
        )
        entry_19 = Entry(
            self,
            bd=0,
            textvariable=self.data["court_no"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_19.place(
            x=784.0,
            y=403.0,
            width=246.0,
            height=19.0
        )

        entry_image_20 = PhotoImage(
            file=relative_to_assets("entry_20.png"))
        entry_bg_20 = self.canvas.create_image(
            907.0,
            373.5,
            image=entry_image_20
        )
        entry_20 = Entry(
            self,
            bd=0,
            textvariable=self.data["off_code"],
            bg="#FFFFFF",
            fg="#000716",
            justify='center',
            highlightthickness=0
        )
        entry_20.place(
            x=784.0,
            y=363.0,
            width=246.0,
            height=19.0
        )

        entry_image_21 = PhotoImage(
            file=relative_to_assets("entry_21.png"))
        entry_bg_21 = self.canvas.create_image(
            907.0,
            332.5,
            image=entry_image_21
        )
        entry_21 = Entry(
            self,
            bd=0,
            textvariable=self.data["description"],
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            justify='center',
        )
        entry_21.place(
            x=784.0,
            y=322.0,
            width=246.0,
            height=19.0
        )
        
        self.id_text =self.canvas.create_text(
            111.0,
            470.0,
            anchor="nw",
            text="01",
            fill="#FFFFFF",
            font=("Montserrat SemiBold", 17 * -1)
        )
        
        
       def initialize_info(self):
        self.record_data = db_controller.get_record()
        self.selected_r_id = self.parent.selected_rid

        if self.record_data is not None:
            self.selected_record_data = list(
                filter(lambda x: str(x[0]) == self.selected_r_id, self.record_data)
            )

            if self.selected_record_data:
                self.selected_record_data = self.selected_record_data[0]

                self.canvas.itemconfigure(self.id_text, text=self.selected_record_data[0])
                self.data["d_name"].set(self.selected_record_data[1])
                self.data["d_license"].set(self.selected_record_data[2])
                self.data["address"].set(self.selected_record_data[3])
                self.data["p_no"].set(self.selected_record_data[4])
                self.data["email"].set(self.selected_record_data[5])
                self.data["v_reg"].set(self.selected_record_data[6])
                self.data["v_model"].set(self.selected_record_data[7])
                self.data["v_no"].set(self.selected_record_data[8])
                self.data["off_name"].set(self.selected_record_data[9])
                self.data["e_agency"].set(self.selected_record_data[10])
                self.data["offense"].set(self.selected_record_data[11])
                self.data["date"].set(self.selected_record_data[12])
                self.data["time"].set(self.selected_record_data[13])
                self.data["location"].set(self.selected_record_data[14])
                self.data["description"].set(self.selected_record_data[15])
                self.data["off_code"].set(self.selected_record_data[16])
                self.data["court_no"].set(self.selected_record_data[17])
                self.data["hearing_date"].set(self.selected_record_data[18])
                self.data["outcome"].set(self.selected_record_data[19])
                self.data["fines"].set(self.selected_record_data[20])
                self.data["payment"].set(self.selected_record_data[21])
      
