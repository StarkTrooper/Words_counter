from tkinter import *
from tkinter import ttk
import time

LARGE_FONT = ("Arial", 35, "bold")
FONT = ("Arial", 20, "bold")
FONT_TYPE_WORD = ("Arial", 30, "bold")
input_text = ''
typing_text = "Two members of the 1984 class of Jefferson High School are chairing a group of 18 to look for a resort" \
              " for the 20-year class reunion. A lovely place 78 miles from the city turns out to be the best. It " \
              "has 254 rooms and a banquet hall to seat 378. It has been open 365 days per year since opening on May" \
              " 30, 1926. They will need 450 to reserve the resort. Debbie Holmes was put in charge of buying 2,847" \
              " office machines for the entire firm. Debbie visited more than 109 companies in 35 states in 6 months." \
              " She will report to the board today in Room 2784 at 5 p.m. The board will consider her report about" \
              " those 109 firms and recommend the top 2 or 3 brands to purchase. Debbie must decide before August 16." \
              " Lynn Greene said work started on the project March 27, 2003. The 246 blueprints were mailed to the" \
              " office 18 days ago. The prints had to be 100 percent accurate before they were acceptable." \
              " The project should be finished by May 31, 2025. At that time there will be 47 new condominiums, each" \
              " having at least 16 rooms. The building will be 25 stories."
typing_list = typing_text.split()
words_typed = 0


class App(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.pack()

        self.main_labelitem = Label(text="CHECK YOUR TYPING SPEED", font=LARGE_FONT, background="blue")
        self.main_labelitem.pack(pady=20)

        self.instructions_label = Label(text="Type the word highlighted in yellow and hit spacebar to continue typing."
                                             " You have 60 seconds.", font=FONT, wraplength=600, background="white")
        self.instructions_label.pack(pady=40)

        global words_typed
        self.typing_text_label = Label(text=f"{typing_list[words_typed]}", font=FONT_TYPE_WORD, background="Yellow")
        self.typing_text_label.pack(pady=40)

        self.entrythingy = Entry(width=25, font=FONT)
        self.entrythingy.pack(pady=60)
        self.entrythingy.focus_set()

        self.button = ttk.Button(text="Restart", command=self.restart)
        self.button.pack(pady=20)

        # Define a callback for when the user hits space.
        self.entrythingy.bind('<Key-space>', self.test_function)

    def test_function(self, event):
        self.entrythingy.after(60000, self.result)
        global input_text, words_typed
        words_typed += 1
        input_text += self.entrythingy.get()
        self.entrythingy.delete(0, END)
        self.typing_text_label.configure(text=f"{typing_list[words_typed]}")

    def result(self):
        global typing_list, words_typed, input_text
        input_list = input_text.split()
        correct_words = 0
        wrong_words = ''
        for ind in range(0, words_typed):
            if typing_list[ind] == input_list[ind]:
                correct_words += 1
            else:
                wrong_words += f"{typing_list[ind]}, "
        accuracy = round(100 * correct_words / words_typed, 2)
        self.typing_text_label.destroy()
        self.entrythingy.destroy()
        self.instructions_label.configure(text=f"Test is Over.\nYour speed is: {words_typed} WPM \nAccuracy: "
                                               f"{accuracy}% \nWrongly typed words were: {wrong_words}",
                                          background="yellow")

    def restart(self):
        global input_text, words_typed, time_out
        input_text = ''
        words_typed = 0
        self.main_labelitem.destroy()
        self.instructions_label.destroy()
        self.typing_text_label.destroy()
        self.entrythingy.destroy()
        self.button.destroy()
        App(root)


# Create an instance of tkinter frame
root = Tk()
# Set the geometry of tkinter frame
root.geometry("800x700")
# call app function
myapp = App(root)
myapp.mainloop()
