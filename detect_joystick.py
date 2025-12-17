import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print(" No joystick detected.")
    exit()

js = pygame.joystick.Joystick(0)
js.init()

print(" Using joystick:", js.get_name())
print("Axes:", js.get_numaxes(), "| Buttons:", js.get_numbuttons())

while True:
    pygame.event.pump()
    x = js.get_axis(0)  # Roll (left/right)
    y = js.get_axis(1)  # Pitch (forward/back)
    print(f"Roll: {x:.2f}, Pitch: {y:.2f}", end="\r")
    
    
    

# if program crash
# then it runs this procedure
def global_exception_handler(type, value, traceback):
    global main, frame_all_main

    
    def destroy_frame():
        frame_reload_main.destroy()
        configure_screen()
    
    try:
        f = open("bug_saver.txt", "x")
        f.close()
    except:
        pass
    f = open("bug_saver.txt", "a")
    f.write(f"{value}")
    f.write("\n")
    f.close()
    
    frame_all_main.destroy()
    frame_reload_main = Frame(main, bg = bg_choice)
    frame_reload_main.pack()
    empty_reload_1_label_error = Label(frame_reload_main, text = "", font = ("Calibri",80), bg = bg_choice, fg = "black")
    empty_reload_1_label_error.pack()
    bug_found_label_error = Label(frame_reload_main, text = "Click reload below to restart the application", font = ("Calibri",50), bg = bg_choice, fg = "black")
    bug_found_label_error.pack()
    reload_button_error = Button(frame_reload_main, text = "Reload", font = ("Calibri",40), bg = bg_choice, fg = "black", bd = 0,  activebackground="light grey", activeforeground="black", highlightbackground="black", command = lambda: destroy_frame())
    reload_button_error.pack(pady = 10)

def start_program():
    def detect_joystick_change():
        global roll_angle, pitch_angle
        pygame.event.pump()
        roll_angle = roll_angle + float(joystick_1.get_axis(0))
        pitch_angle = pitch_angle + float(joystick_1.get_axis(1))
        canvas_background_main.delete("all")
        x1_sky = 1800 - math.cos(math.radians(roll_angle)) * 1800
        y1_sky = 1800 + math.sin(math.radians(roll_angle)) * 1800
        x2_sky = 1800 + math.cos(math.radians(roll_angle)) * 1800
        y2_sky = 1800 - math.sin(math.radians(roll_angle)) * 1800
        x3_sky = x2_sky + math.sin(math.radians(roll_angle)) * 1800
        y3_sky = y2_sky + math.cos(math.radians(roll_angle)) * 1800
        x4_sky = x1_sky + math.sin(math.radians(roll_angle)) * 1800
        y4_sky = y1_sky + math.cos(math.radians(roll_angle)) * 1800
        x1_ground = 1800 - math.cos(math.radians(roll_angle)) * 1800
        y1_ground = 1800 + math.sin(math.radians(roll_angle)) * 1800
        x2_ground = 1800 + math.cos(math.radians(roll_angle)) * 1800
        y2_ground = 1800 - math.sin(math.radians(roll_angle)) * 1800
        x3_ground = x2_ground - math.sin(math.radians(roll_angle)) * 1800
        y3_ground = y2_ground - math.cos(math.radians(roll_angle)) * 1800
        x4_ground = x1_ground - math.sin(math.radians(roll_angle)) * 1800
        y4_ground = y1_ground - math.cos(math.radians(roll_angle)) * 1800
        canvas_background_main.create_polygon(x1_sky, y1_sky, x2_sky, y2_sky, x3_sky, y3_sky, x4_sky, y4_sky, fill = "#87CEEB", outline = "")
        canvas_background_main.create_polygon(x1_ground, y1_ground, x2_ground, y2_ground, x3_ground, y3_ground, x4_ground, y4_ground, fill = "#4CAF50", outline = "")
        
        main.after(500, detect_joystick_change)
        
        
    
    canvas_background_main = Canvas(frame_all_main, width = 3600, height = 3600, bg = "light grey", bd = 0, highlightthickness = 0)
    canvas_background_main.place(relx = 0.5, rely = 0.5, anchor = "center")
    canvas_background_main.create_rectangle(0, 0, 3600, 1800, fill = "#87CEEB", outline = "")
    canvas_background_main.create_rectangle(0, 1800, 3600, 3600, fill = "#4CAF50", outline = "")
    main.after(500, detect_joystick_change)


# this procedure will run whenever program first run and whenever after program crashes to reset everything, except screen {main}
def configure_screen():
  main.configure(bg = bg_choice)
  frame_all_main.place(relx = 0.5, rely = 0.5, anchor = "center")
  start_program()
