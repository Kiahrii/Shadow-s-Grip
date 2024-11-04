from tkinter import *
from time import *
import pygame

# main window
window = Tk()
window.geometry("1000x700")
window.resizable(width=False, height=False)

pygame.mixer.init()

# window logo
window.title("Shadow's Grip")
logo = PhotoImage(file="E:\Practice Html\python\MAZE(01\logo2.png")
window.iconphoto(True,logo)

# canvas for background image
canvas = Canvas(window, width=1000, height=700)
canvas.pack(fill="both", expand=True)

screen_title_image = PhotoImage(file="E:\Practice Html\python\MAZE\itle_screen_rectangle.png")
canvas.create_image(0, 0, image=screen_title_image, anchor="nw")

# BACKGROUND MUSIC, EFFECTS
main_background_music = pygame.mixer.Sound('E:\Practice Html\python\MAZE(01\MusicBox.mp3')
button_click = pygame.mixer.Sound('E:\Practice Html\python\MAZE(01\Button Click.mp3')
timer_sound = pygame.mixer.Sound('E:\Practice Html\python\MAZE(01\TickClock.mp3')
timer_music = pygame.mixer.Sound('E:\Practice Html\python\MAZE(01\Dun.mp3')

# clear dynamic widgets function
dynamic_widgets = []
photo = None    

def clear_dynamic_widgets():
    global dynamic_widgets
    for widget in dynamic_widgets: 
        widget.destroy()    
    dynamic_widgets = []

# Lay out for the maze
def display(text):
    text_holder = canvas.create_text(95,100, text=text, font=('Times New Roman', 40, 'bold'), fill='white', anchor='nw', justify='center', width=850)  
    return text_holder
  
# Lay out for Buttons
def buttons(window, text, command, x, y):
    button = Button(window, command=command, text=text, font=('Times New Roman', 25, 'bold'), fg='white', bg='gray', activeforeground='gold', activebackground='black', relief=RAISED, borderwidth=5, padx=10, pady=10)
    button.place(x=x, y=y)
    dynamic_widgets.append(button)
    return button

# End Menu Button
def end_menu():
    global end_menu_button
    end_menu_button = Button(window, command=lambda: [play_button_sound(), title_screen()], text='Main Menu', font=('Times New Roman', 20, 'bold'), fg='gold', bg='black', activeforeground='white',activebackground='gray', relief=RAISED, borderwidth=5, padx=5, pady=5)
    end_menu_button.place(x=425, y=510)
    dynamic_widgets.append(end_menu_button)
    main_background_music.stop()
    timer_sound.stop()

# Back Button for Credits
def back():
    back_button = Button(window, text='Back', command=lambda: [play_button_sound(), title_screen()], font=('Wide Latin', 15,), fg='black', bg='gray', relief=RAISED)
    back_button.bind("<Enter>", on_enter)
    back_button.bind("<Leave>", on_leave)
    back_button.place(x=50, y=620)
    dynamic_widgets.append(back_button)

# TIMER function
my_timer = 5
timer_id = None

def timer():
    global my_timer, timer_id
    if my_timer > 0:
        my_timer = my_timer - 1
        print(f'Timer: {my_timer}') # To check if it works
        timer_id = window.after(1000, timer)
    else:
        global photo
        clear_dynamic_widgets()
        canvas.delete('all')
        photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image26.png')
        canvas.create_image(0, 0, image=photo, anchor='nw')

        timer_sound.play()

        game_over = display("You are caught! You hesitated too long.")
        canvas.itemconfigure(game_over, font=('Times New Roman', 30, 'bold'), fill='red')
        canvas.coords(game_over, 200, 380)
        print("Game over") # To check if it works
        timer_sound.stop()
        end_menu()

timer_label = None # Global variable to store the timer label

def reset_timer():
    global my_timer, timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
    my_timer = 5 
    timer_music.play(loops=-1) # Start timer music, loops=-1 makes it repeat
    print("I'm resetting") # To check if it works
    timer_id = window.after(1000, timer)

def stop_timer():
    global my_timer, timer_id, timer_label
    if timer_id is not None:
        window.after_cancel(timer_id)
        print("Timer stopped")
    if timer_label:
        timer_label.destroy()
        timer_label = None
    timer_music.stop() #Stop timer music
    my_timer = 0
    timer_id = None

# ---------- MAIN MAZE ----------

def riddle_2_choices(): # TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image2.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    reset_timer()
    riddle_text = Label(window, text='"I speak without a mouth and hear without ears. I have no body, but I come alive with wind. Who am I?"',
                        font=('Lucida Handwriting', 33), fg='gold', bg='black', wraplength=850, relief=RAISED, borderwidth=5, justify='center', padx=10, pady=5)
    riddle_text.place(x=85, y=100)
    dynamic_widgets.append(riddle_text)
    button_A = buttons(window, text='ECHO', command=lambda: [play_button_sound(), echo()], x=250, y=400)
    button_B = buttons(window, text='SILENCE', command=lambda: [play_button_sound(), silence()], x=600, y=400)

def silence(): # TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image23.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    reset_timer()
    display("As you proceed, you hear footsteps getting louder behind you.")
    button_A = buttons(window, text='RUN', command=lambda: [play_button_sound(), run()], x=450, y=410)
    button_B = buttons(window, text='Hide in a dark hollow', command=lambda: [play_button_sound(), hide()], x=340, y=520)

def leave_magazine(): # TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image19.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    reset_timer()
    display("You proceed ahead and find that the walls surrounds you and there's no other way. The growl intensifies signaling danger.")
    button_A = buttons(window, text='SHOOT', command=lambda: [play_button_sound(), shoot_no_magazine()], x=250, y=400)
    button_B = buttons(window, text='ESCAPE', command=lambda: [play_button_sound(), fail_escape()], x=600, y=400)    

def two_path(): # TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image4.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    reset_timer()
    display("You find two paths ahead. One leads to death. Choose wisely.")
    button_A = buttons(window, text='LEFT', command=lambda: [play_button_sound(), search()], x=250, y=400)
    button_B = buttons(window, text='RIGHT', command=lambda: [play_button_sound(),leave_magazine()], x=600, y=400)

def left_path2(): #TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image22.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    reset_timer()
    display("As you moved deeper into the maze, a low growl echoes behind you. The atmosphere thickens with tension.")
    button_A = buttons(window, text='Keep moving cautiously', command=lambda: [play_button_sound(), two_path()], x=300, y=410)
    button_B = buttons(window, text='Hide in a dark hollow', command=lambda: [play_button_sound(), hide()], x=320, y=520) 

def pick_magazine(): # TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image3.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    reset_timer()
    text_holder = display(text="You confront the lurking shadow, now armed with a loaded gun! Your heart races as you prepare for worst.")
    canvas.itemconfig(text_holder, fill='red')
    canvas.coords(text_holder, 90, 250)

    button_A = buttons(window, text='SHOOT', command=lambda: [play_button_sound(), shoot_magazine()], x=450, y=470)
    button_B = buttons(window, text='Throw the gun at his face', command=lambda: [play_button_sound(), throw_gun()], x=350, y=550)
    button_A.config(font=('Times New Roman', 20, 'bold'), padx=5, pady=5)
    button_B.config(font=('Times New Roman', 20, 'bold'), padx=5, pady=5)

def run(): # BAD ENDING
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image19.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    end_menu()
    text_holder = display("The footsteps are now loud and distinct closing the distance. Until you've hit a wall and the pursuer pulled you into darkness. GAME OVER")
    canvas.config(text_holder, fill='gold')

def echo(): # GOOD ENDING
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image1.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    text_holder = display("The light flickered, then vanished, replaced by a vibrant green. As if in response, the wall began to slide. YOU ESCAPED!")
    canvas.itemconfig(text_holder, font=('Times New Roman', 18, 'bold'), fill='gold')
    end_menu()

def throw_gun(): # BAD ENDING
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image3.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    text_holder = display("He dodged it and lunged towards you, pulling you into darkness.")
    canvas.itemconfig(text_holder, fill='red')
    canvas.coords(text_holder, 150,250)
    end_menu() 

def fail_escape(): # BAD ENDING
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image3.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    text_holder = display("You died trying. GAME OVER")
    canvas.itemconfig(text_holder, fill='red')
    canvas.coords(text_holder, 150,250)
    end_menu()

def shoot_no_magazine(): # BAD ENDING
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image3.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    text_holder = display("You fired the gun but the magazine is empty. The creature lunge towards you, pulling you into darkness. GAME OVER.")
    canvas.itemconfig(text_holder, fill='red')
    canvas.coords(text_holder, 90, 250)
    end_menu()

def hide(): # GOOD ENDING
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image18.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    text_holder = display("You successfully hide as the pursuer passes by, your heart pounding. A faint light flickered in the corner of the hollow, drawing your eye. You reached out, your hand brushing against something. It was a false wall! With a surge of hope, you pushed hard enough and the wall gave way, revealing a hidden passage. YOU ESCAPED!!")
    canvas.itemconfig(text_holder, font=('Times New Roman', 18, 'bold'), fill='gold')
    canvas.coords(text_holder, 90, 250)
    end_menu()

def shoot_magazine(): # GOOD ENDING
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image1.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    text_holder = display("You shot his right knee delaying his chase. You took this opportunity to escape. With one final burst of energy, you leap towards the exit and find yourself back in the safety of daylight. The creature's wail fade into silence. YOU ESCAPED!")
    canvas.itemconfig(text_holder, font=('Times New Roman', 18, 'bold'), fill='gold')
    end_menu()            

def riddle_2(): # NOT TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image2.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    display("You discover a riddle inscribed on the wall and a red light beside it.")
    button_A = buttons(window, text='Read', command=lambda: [play_button_sound(), riddle_2_choices()], x=450, y=350)

def right_path(): #NOT TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image25.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    text_holder = display("You walked into a wide-open chamber. There are two exits.")
    canvas.itemconfig(text_holder, fill='black')
    canvas.coords(text_holder, 170, 100)
    button_A = buttons(window, text='LEFT', command=lambda: [play_button_sound(), riddle_2()], x=250, y=400)
    button_B = buttons(window, text='RIGHT', command=lambda: [play_button_sound(), silence()], x=600, y=400)    

def search(): # NOT TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image7.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    display("You saw a loaded magazine lying on the ground.")
    button_A = buttons(window, text='Pick it up', command=lambda: [play_button_sound(), pick_magazine()], x=250, y=400)
    button_B = buttons(window, text="I don't need it", command=lambda: [play_button_sound(), leave_magazine()], x=600, y=400)  

def walk_deeper(): # NOT TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image6.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    stop_timer()
    display("You stumble upon a gun lying on the ground. You pick it up feeling its weight.")
    button_A = buttons(window, text='LEFT', command=lambda: [play_button_sound(), left_path2()], x=250, y=400)
    button_B = buttons(window, text='RIGHT', command=lambda: [play_button_sound(), search()], x=600, y=400)
    
def check_riddle(): # NOT TIMED
    user_answer = answer_riddle.get().upper()
    if user_answer == "CHASE":
        label_result.config(text="Correct! You can safely go back.")
        submit_button.config(state=DISABLED)
        answer_riddle.config(state=DISABLED)
        end_menu() 
    elif user_answer:
        label_result.config(text="Wrong! You are doomed to finish the maze.")
        proceed = Button(window, text='I will escape', command=lambda: [play_button_sound(), walk_deeper()], font=('Times New Roman', 20, 'bold'), fg='gold', bg='black', activeforeground='white', activebackground='gray', relief=RAISED, borderwidth=5, padx=5, pady=5)
        proceed.place(x=425, y=510)
        dynamic_widgets.append(proceed) 
        submit_button.config(state=DISABLED)
        answer_riddle.config(state=DISABLED)
    else:
        label_result.config(text="Type an answer.")

def riddle(): # NOT TIMED
    global photo
    global submit_button
    global answer_riddle
    clear_dynamic_widgets()  
    canvas.delete('all') 
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image8.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    riddle = Label(window, text='"I am the echo of your footsteps, the whisper of your fear. I am always one step behind, and I will never let you escape. I am a five-letter word, what am I?"',
                          font=('Lucida Handwriting', 30), fg='gold', bg='black', wraplength=850, relief=RAISED, borderwidth=5, justify='center', padx=10, pady=5)
    riddle.place(x=85, y=100)
    dynamic_widgets.append(riddle) 

    global answer_riddle
    answer_riddle = Entry(window, font=('Times New Roman', 18), width=10)
    answer_riddle.place(x=450, y=400)
    dynamic_widgets.append(answer_riddle)  

    submit_button = Button(window, text='Submit', font=('Cambria', 15,), fg='white', bg='gray', command=lambda: [play_button_sound(), check_riddle()])
    submit_button.place(x=465, y=450)
    dynamic_widgets.append(submit_button) 

    global label_result
    label_result = Label(window, text="", font=('Cambria', 15, 'bold'), fg='black', bg='white')
    label_result.place(x=100, y=450)
    dynamic_widgets.append(label_result) 

def turnback(): # NOT TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image8.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    display("Answer a riddle to successfully go back.")
    button_A = buttons(window, text='Alright', command=lambda: [play_button_sound(),riddle()], x=400, y=350)
    button_B = buttons(window, text='I change my mind.', command=lambda: [play_button_sound(),walk_deeper()], x=320, y=450)

def left_path(): # NOT TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\woods3.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    display("You find yourself on a tight, shadowy trail. The air is thick with moisture, and the damp ground squelches underfoot.")
    button_A = buttons(window, text='Walk in Deeper', command=lambda: [play_button_sound(), walk_deeper()], x=150, y=400)
    button_B = buttons(window, text='Turnback', command=lambda: [play_button_sound(),turnback()], x=600, y=400)

# NEW PATH function
def maze_start(): # NOT TIMED
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\woods8.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    display("You find yourself at the entrance of a dark forest labyrinth. Which path will you choose?")
    button_A = buttons(window, text='LEFT', command=lambda: [play_button_sound(), left_path()], x=250, y=400)
    button_B = buttons(window, text='RIGHT', command=lambda: [play_button_sound(), right_path()], x=600, y=400)

# ---------- END MAZE -----------

# ---------- CREDITS function ----------

def scrolling_text():
    clear_dynamic_widgets()
    canvas.delete('all')
    canvas.configure(bg='black')

    credits_text = """

    SHADOW'S GRIP

    DEVELOPED BY:

    Arlene Zoe Almonte
    Eduard Miguel Gonzales
    Keziah Garcia
    Kirk Nathaniel Alilano
    Niño Emman Nativadid

    
    DIRECTED BY:

    Keziah Garcia

    
    STORY AND SCRIPT:

    Keziah Garcia
    Niño Emman Nativadid

    
    ART AND GRAPHICS:

    Arlene Zoe Almonte
    Eduard Miguel Gonzales
    Kirk Nathaniel Alilano

    MUSIC and SOUND EFFECTS:

    Niño Emman Nativadid

    
    Thank you for playing!
    
    """

    text_holder = canvas.create_text(500, 700, text=credits_text, font=('Cambria', 20), fill='white', justify='center')

    def scroll_animation():
        nonlocal text_holder
        canvas.move(text_holder, 0, -2)
        current_position = canvas.coords(text_holder)[1]
        if current_position < -300:
            canvas.coords(text_holder, 500, 700)

        window.after(50, scroll_animation)
    
    scroll_animation()
    back()

# ---------- END of CREDITS ----------

# ---------- HOW TO PLAY function ---------

def check_sample_riddle():
    global scenario3 

    answer_sample = answer_riddle.get().lower()

    if 'scenario3' in globals() and scenario3 is not None:
        scenario3.destroy()

    if answer_sample == "shadow":
        label_result.config(text='Correct! You are now ready.')
        submit_button.config(state=DISABLED)
        answer_riddle.config(state=DISABLED)

        start_button = Button(window, text='Start', command=lambda: [play_button_sound(), maze_start()],
                              font=('Times New Roman', 20, 'bold'), fg='gold', bg='black',
                              activeforeground='gray', activebackground='white',
                              relief=RAISED, borderwidth=5, padx=5, pady=5)
        start_button.place(x=460, y=550)
        dynamic_widgets.append(start_button)
        
        text_id_b = display("Remember, you have only one-time chance to answer the riddle right.")
        canvas.itemconfig(text_id_b, font=('Times New Roman', 18, 'bold'), fill='red')
        canvas.coords(text_id_b, 130, 640)

        scenario3 = None
    elif answer_sample:
        label_result.config(text='Try Again.')
        
        scenario3 = Label(window, text="Type 'shadow' to finish the tutorial.",
                           font=('Times New Roman', 20, 'bold'), fg='white', bg='black',
                           wraplength=900, padx=10, pady=5)
        scenario3.place(x=300, y=550)
        dynamic_widgets.append(scenario3)
    else:
        label_result.config(text='Type an answer.')

def next():
    global submit_button
    global label_result
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image9.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    text_holder = display("You might also stumble upon riddles which requires you to answer it like this:")
    canvas.itemconfig(text_holder, font=('Times New Roman', 18, 'bold'))
    canvas.coords(text_holder, 110, 60)

    text_id_a=display("If you didn't answer, it will prompt you to type one. Try clicking 'SUBMIT' without typing anything.")
    canvas.itemconfig(text_id_a, font=('Times New Roman', 18, 'bold'))
    canvas.coords(text_id_a, 110, 470 )

    riddle_sample = Label(window, text='"I follow you closely, yet I have no form. In light, I grow longer, in darkness, I swarm. I twist through the pathways, both silent and near. What am I that brings both dread and fear?"',
                          font=('Lucida Calligraphy', 25), fg='black', bg='#7e8260', wraplength=850, relief=RAISED, borderwidth=5, justify='center', padx=10, pady=5)
    riddle_sample.place(x=85, y=100)
    dynamic_widgets.append(riddle_sample) 

    global answer_riddle
    answer_riddle = Entry(window, font=('Times New Roman', 18), width=10)
    answer_riddle.place(x=450, y=350)
    dynamic_widgets.append(answer_riddle)  

    submit_button = Button(window, text='Submit', font=('Cambria', 15,), fg='white', bg='gray', command=lambda: [play_button_sound(), check_sample_riddle()])
    submit_button.place(x=475, y=400)
    dynamic_widgets.append(submit_button) 

    global label_result
    label_result = Label(window, text="", font=('Cambria', 15, 'bold'), fg='black', bg='white')
    label_result.place(x=85, y=350)
    dynamic_widgets.append(label_result) 

def timer_tutorial():
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image9.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    text_holder = display("Every choice must be swift. Hesitate too long, and the shadows may catch up.")
    canvas.itemconfig(text_holder, font=('Times New Roman', 30, 'bold'))
    canvas.coords(text_holder, 80, 90)

    text_id_a = display("Your instincts will be tested. Time moves against you... but you won't see it.")
    canvas.itemconfig(text_id_a, font=('Times New Roman', 30, 'bold'))
    canvas.coords(text_id_a, 80, 200)
    button_A = buttons(window, text='Back', command=lambda: [play_button_sound(), how_to_play()], x=250, y=500)
    button_B = buttons(window, text='Next', command=lambda: [play_button_sound(), next()], x=600, y=500)

    instruction = Label(window, text="Seven seconds, the shadows creep near. Speak your choice, or vanish in fear.", 
                        font=('Times New Roman', 30, 'bold'), fg='red', bg='black', wraplength=900, relief=RAISED, padx=10, pady=5)
    instruction.place(x=50, y=330)
    dynamic_widgets.append(instruction)

def how_to_play():
    global photo
    clear_dynamic_widgets()
    canvas.delete('all')
    photo = PhotoImage(file='E:\Practice Html\python\MAZE(01\Image9.png')
    canvas.create_image(0, 0, image=photo, anchor='nw')

    text_holder = display("A scenario will be given and you have to choose one of the choices.")
    canvas.coords(text_holder, 140, 150)
    button_A = buttons(window, text='Back', command=title_screen, x=250, y=400)
    button_B = buttons(window, text='Next', command=timer_tutorial, x=600, y=400)

# -------- END of HOW TO PLAY ----------

# color highlight for MENU buttons
def on_enter(e):
    e.widget['background'] = 'light gray'

def on_leave(e):
    e.widget['background'] = 'gray'

# add this function to play button sound
def play_button_sound():
    button_click.play()

# MAIN MENU buttons
def title_screen():
    clear_dynamic_widgets()
    main_background_music.play(loops=-1)

    global screen_title_image
    canvas.create_image(0, 0, image=screen_title_image, anchor="nw")

    canvas.create_text(500, 150, text="Shadow's Grip", font=('Curlz MT', 100, 'bold'), fill='white', anchor='center')
    canvas.pack()

    button1 = Button(window, text='New path', font=('Wide Latin', 18), bg='gray', fg='black', relief=RAISED,
                     command=lambda: [play_button_sound(), maze_start()])
    button1.bind("<Enter>", on_enter)
    button1.bind("<Leave>", on_leave)
    button1_window = canvas.create_window(500, 295, window=button1)  

    button2 = Button(window, text='How to Play', font=('Wide Latin', 18), bg='gray', fg='black', relief=RAISED,
                     command=lambda: [play_button_sound(), how_to_play()])
    button2.bind("<Enter>", on_enter)
    button2.bind("<Leave>", on_leave)
    button2_window = canvas.create_window(500, 360, window=button2)

    button3 = Button(window, text='Credits', font=('Wide Latin', 18), bg='gray', fg='black', relief=RAISED,
                     command=lambda: [play_button_sound(), scrolling_text()])
    button3.bind("<Enter>", on_enter)
    button3.bind("<Leave>", on_leave)
    button3_window = canvas.create_window(500, 425, window=button3)

    button4 = Button(window, text='Quit', font=('Wide Latin', 18), bg='gray', fg='black', relief=RAISED,
                     command=lambda: [play_button_sound(), window.destroy()])
    button4.bind("<Enter>", on_enter)
    button4.bind("<Leave>", on_leave)
    button4_window = canvas.create_window(500, 490, window=button4)
    
title_screen()

window.mainloop()
