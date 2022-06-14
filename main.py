from PIL import Image
from PIL import ImageTk
import tkinter as tk
import tkinter.font as font
import time
import random

window = tk.Tk()
window.title("GAME!")
window.geometry("704x400")
window.configure(bg="white")
window.resizable(False, False)

rectangle_color = "red"

rectangle = tk.Label(
  window,
  width = 7,
  height = 1,
  bg = rectangle_color,
  bd = 1,
  relief = "solid",
)

start_text = tk.Label(
  window,
  width = 8,
  height = 4,
  bg = "white",
  bd = 1,
  relief = "solid", 
  text = "Start?")

class creating_ColorPopup:
  def create_Popup(self):
    popup = self.popup = tk.Toplevel(window)
    label = self.label = tk.Label(popup, text = "Enter a hex number")
    label.pack()
    self.entry_box = tk.Entry(popup)
    self.entry_box.pack()
    confirmation_Button = self.confirmation_Button = tk.Button(popup, text = "Confirm?", command = self.whenButtonClicked)
    confirmation_Button.pack()
  def whenButtonClicked(self):
    global rectangle
    value = self.entry_box.get()
    try:
      rectangle.configure(bg = value)
    except:
      self.label.configure(text = "Incorrect input, try again!")
    else:
      self.popup.destroy()
    
popup_instance = creating_ColorPopup()

high_score = 0

highscore_display = tk.Label(
  window,
  text = "Highscore:\n" + str(high_score),
  bg = "white"
)
highscore_display.pack(
  side = "right",
  padx = (0,155)
)
color_button = tk.Button(
  window,
  text = "Change color?",
  command = popup_instance.create_Popup
)
start_text.place(
  bordermode = "outside", 
  relx = .45, 
  rely = .42
)
rectangle.pack(
  side = "left",
  padx = 145, 
  pady = (0,38)
)
color_button.place(
  relx = .165, 
  rely = .5
)

def hide_all():
  start_text.place_forget()
  rectangle.pack_forget()
  color_button.place_forget()
  highscore_display.pack_forget()

def start_Button(event):
  timer_seconds = tk.IntVar()
  timer_seconds.set(4)
  hide_all()
  countdown_font = font.Font(size = "50", weight = "bold")
  countdown = tk.Label(
    window,
    textvariable = timer_seconds,
    # textvariable = timer_seconds,
    bg = "white",
    fg = "black",
  )
  countdown['font'] = countdown_font
  countdown.place(relx = .44, rely = .40)
  while timer_seconds.get() > 1:
    timer_seconds.set(timer_seconds.get() - 1)
    window.update()
    time.sleep(1.3)
  timer_seconds.set("Go!")
  window.update()
  time.sleep(.5)
  countdown.destroy()
  score_Display()

score = tk.IntVar()
score.set(0)
def score_Display():
  global rectangle
  global highscore_display
  global score_label
  score_label = tk.Label(
    window,
    bg = "white",
    font = "bold",
    text = "Score:\n" + str(score.get())
  )
  score_label.place(anchor = "nw")
  highscore_display.place(relx = 1.0, anchor = "ne")
  highscore_display.config(font = "bold")
  rectangle.place(x = 352, y = 360)
  window.update()
  ball_Physics()

def ball_Physics():
  global rectangle, score, highscore_display, ball, high_score, gameover_popup
  game_State = False # false means that the player has not lost yet
  random_location = random.randint(0, 665)
  i = Image.open("images/LANDMAN.png")
  i = i.resize((40,40))
  circle = ImageTk.PhotoImage(i)
  ball = tk.Label(
    window,
    bg = "white",
    image = circle,
    anchor = "n"
  )
  ball.image = circle
  ball.place(x = random_location, y = 10)
  window.update()
  x_change = 10
  y_change = 10
  while game_State != True:
    if ball.winfo_rootx() <= 0:
      x_change = -10
    elif ball.winfo_rootx() >= 665:
      x_change = 10
    if ball.winfo_rooty() - 21 <= 0:
      y_change = 10
    window.update()
    for x in range(rectangle.winfo_rootx() - 10, rectangle.winfo_rootx() + 10):
      window.update()
      if ball.winfo_rootx() == x and ball.winfo_rooty() >= 348:
        y_change = -10
        window.update()
        score.set(score.get() + 1)
        score_label.config(text = "Score:\n" + str(score.get()))
        # print(score.get())
        window.update()
    window.update()
    ball.place(x = ball.winfo_rootx() - x_change, y = (ball.winfo_rooty() - 21) + y_change)
    # print(f"({rectangle.winfo_rootx()}, {rectangle.winfo_rooty()}) , ({ball.winfo_rootx()}, {ball.winfo_rooty()})")  to test location of ball and paddle
    window.update()
    time.sleep(.3)
    if ball.winfo_rooty() >= 375:
      game_State = True
      rectangle.pack_forget()
      if score.get() > high_score:
        high_score = score.get()
        highscore_display.config(text = "Highscore:\n" + str(high_score))
      gameover_popup = tk.Toplevel(window)
      gameover_popup.title("LOSER LOL")
      gameover_popup.geometry("200x100")
      gameover_label = tk.Label(
        gameover_popup,
        text = "GAME OVER! Play again?"
      )
      gameover_label.pack()
      gameover_button1 = tk.Button(
        gameover_popup,
        text = "Yes?",
        command = yes_continue
      )
      gameover_button1.pack(side = "left")
      gameover_button2 = tk.Button(
        gameover_popup,
        text = "No?",
        command = no_continue
      )
      gameover_button2.pack(side = "right")
      

def right_key(event):
  window.update()
  rectangle.place(x = rectangle.winfo_rootx() + 20)

def left_key(event):
  window.update()
  rectangle.place(x = rectangle.winfo_rootx() - 20)

def yes_continue():
  global start_text
  gameover_popup.destroy()
  ball.place_forget()
  rectangle.pack_forget()
  score_label.place_forget()
  highscore_display.place_forget()

  highscore_display.pack(
  side = "right",
  padx = (0,155)
  )
  start_text.place(
  bordermode = "outside", 
  relx = .45, 
  rely = .42
  )
  rectangle.pack(
  side = "left",
  padx = 145, 
  pady = (0,38)
  )
  color_button.place(
  relx = .165, 
  rely = .5
  )
  score.set(0)

def no_continue():
  quit()

window.bind("<Right>", right_key)
window.bind("<Left>", left_key)
start_text.bind("<Button-1>", start_Button)




window.mainloop()

