import pygame
import math

#initial game configuration
def initial_game_configuration():
    
    roll_angle = 0
    pitch_angle = 0
    horizontal_speed = 103
    vertical_speed = 0
    actual_speed = 103
    height = 3352.8
    altitude = height * 3.281
    extra_lift_from_flap_setting = 0
    oswald_efficiency_factor = 0.87
    flight_path_angle, AoA, lift_coefficient, drag_coefficient = calculate_lift_drag_coefficient(roll_angle, pitch_angle, horizontal_speed, vertical_speed, extra_lift_from_flap_setting, oswald_efficiency_factor)
    
    return(roll_angle, pitch_angle, horizontal_speed, vertical_speed, actual_speed, height, altitude, extra_lift_from_flap_setting, oswald_efficiency_factor, flight_path_angle, AoA, lift_coefficient, drag_coefficient)

# calculate x, y coordinate of all vertex of sky, ground rectangle background with {roll_angle}, {pitch_angle}, {width_of_visible_screen}, {height_of_visible_screen}
# then draw sky, ground rectangle background with {x_axis_frame}, {y_axis_frame}
def draw_sky_ground_background(roll_angle, pitch_angle, width_of_visible_screen, height_of_visible_screen, x_axis_frame, y_axis_frame, sky_colour, ground_colour):
    
    width_of_background = math.pow(math.pow(width_of_visible_screen, 2) + math.pow(height_of_visible_screen, 2), 0.5)
    height_of_background = height_of_visible_screen * 10
    change_in_action_due_to_height_of_visible_screen = height_of_visible_screen / 100
    x_y_center_of_background = [(width_of_visible_screen / 2) + (math.sin(math.radians(roll_angle)) * pitch_angle * change_in_action_due_to_height_of_visible_screen), (height_of_visible_screen / 2) + math.cos(math.radians(roll_angle)) * pitch_angle * change_in_action_due_to_height_of_visible_screen]
    
    frame_visible_screen_main = pygame.Surface((width_of_visible_screen, height_of_visible_screen))
    x1 = x_y_center_of_background[0] - math.cos(math.radians(roll_angle)) * (width_of_background / 2)
    y1 = x_y_center_of_background[1] + math.sin(math.radians(roll_angle)) * (width_of_background / 2)
    x2 = x_y_center_of_background[0] + math.cos(math.radians(roll_angle)) * (width_of_background / 2)
    y2 = x_y_center_of_background[1] - math.sin(math.radians(roll_angle)) * (width_of_background / 2)
    x3_sky = x2 - math.sin(math.radians(roll_angle)) * (height_of_background / 2)
    y3_sky = y2 - math.cos(math.radians(roll_angle)) * (height_of_background / 2)
    x4_sky = x1 - math.sin(math.radians(roll_angle)) * (height_of_background / 2)
    y4_sky = y1 - math.cos(math.radians(roll_angle)) * (height_of_background / 2)
    x3_ground = x2 + math.sin(math.radians(roll_angle)) * (height_of_background / 2)
    y3_ground = y2 + math.cos(math.radians(roll_angle)) * (height_of_background / 2)
    x4_ground = x1 + math.sin(math.radians(roll_angle)) * (height_of_background / 2)
    y4_ground = y1 + math.cos(math.radians(roll_angle)) * (height_of_background / 2)
    pygame.draw.polygon(frame_visible_screen_main, sky_colour, [(x1, y1), (x2, y2), (x3_sky, y3_sky), (x4_sky, y4_sky)])
    pygame.draw.polygon(frame_visible_screen_main, ground_colour, [(x1, y1), (x2, y2), (x3_ground, y3_ground), (x4_ground, y4_ground)])
    main.blit(frame_visible_screen_main, (x_axis_frame, y_axis_frame))

def draw_primary_flight_display(roll_angle, pitch_angle, airspeed, altitude):
    
    move_x_axis = 0
    move_y_axis = 0
    x_y_center_of_primary_flight_display = [100 + move_x_axis + (250 / 2), 500 + move_y_axis + (250 / 2)]
    pygame.draw.rect(main, (40, 40, 40), (100 + move_x_axis, 500 + move_y_axis, 250, 250))
    draw_sky_ground_background(roll_angle, pitch_angle, 150, 150, 150 + move_x_axis, 550 + move_y_axis, (60, 134, 189), (137, 73, 34))
    pygame.draw.rect(main, (0, 0, 0), (x_y_center_of_primary_flight_display[0] - 5, x_y_center_of_primary_flight_display[1] - 5, 10, 10))
    #pygame.draw.polygon(main, (0, 0, 0), [(x_y_center_of_primary_flight_display[0] - 120 + move_x_axis, x_y_center_of_primary_flight_display[1] - 5 + move_y_axis), (10, 10), (10, 10)])

# function to calculate {roll_angle}, {pitch_angle}
def calculate_roll_angle_pitch_angle(roll_angle, pitch_angle, change_in_roll_angle, change_in_pitch_angle):
    global fps, time_per_frame
    
    change_in_action_due_to_fps = 1 / (fps / 20)
    roll_angle = roll_angle + change_in_roll_angle * change_in_action_due_to_fps
    
    pitch_angle_change_joystick = math.cos(math.radians(roll_angle)) * change_in_pitch_angle
    pitch_angle = pitch_angle + (pitch_angle_change_joystick) * change_in_action_due_to_fps
    
    return(roll_angle, pitch_angle)

# function to calculate {flight_path_angle}, {AoA}, {lift_coefficient}, {drag_coefficient}
def calculate_lift_drag_coefficient(roll_angle, pitch_angle, horizontal_speed, vertical_speed, extra_lift_from_flap_setting, oswald_efficiency_factor):
    
    flight_path_angle = math.degrees(math.atan(vertical_speed / horizontal_speed))
    # AoA = pitch_angle - flight_path_angle
    #AoA = (pitch_angle - flight_path_angle) * math.cos(math.radians(roll_angle))
    AoA = pitch_angle - flight_path_angle
    # lift_coefficient = (lift_coefficient_for_clean_configuration + extra_lift_from_flap_setting) + lift_curve_slope * (AoA - zero_lift_angle_of_attack)
    lift_coefficient = (0.45 + extra_lift_from_flap_setting) + 0.09 * (AoA - (-3))
    # induced_drag_factor = 1 / (math.pi * oswald_efficiency_factor * aspect ratio)
    induced_drag_factor = 1 / (math.pi * oswald_efficiency_factor * 9.61)
    # drag_coefficient = drag_coefficient_for_clean_configuration + (induced_drag_factor * math.pow(lift_coefficient, 2))
    drag_coefficient = 0.033 + (induced_drag_factor * math.pow(lift_coefficient, 2))
    
    return(flight_path_angle, AoA, lift_coefficient, drag_coefficient)

# function to calculate {height}, {actual_speed}, {horizontal_speed}, {vertical_speed}, {airspeed}, {altitude}
def calculate_airspeed_altitude(flight_path_angle, height, roll_angle, pitch_angle, actual_speed, lift_coefficient, drag_coefficient, horizontal_speed, vertical_speed, throttle):
    global standard_atmospheric_pressure_at_sea_level, standard_temperature_at_sea_level_KELVIN, gravitational_acceleration, molar_mass_of_dry_air, temperature_lapse_rate, ideal_gas_constant, specific_gas_constant_for_dry_air, air_density_at_sea_level
    global wing_reference_area, mass_of_plane, weight_of_plane, maximum_thrust_at_sea_level_static_conditions
    global fps, time_per_frame
    
    temperature_at_altitude_KELVIN = standard_temperature_at_sea_level_KELVIN - temperature_lapse_rate * height
    pressure_at_altitude = standard_atmospheric_pressure_at_sea_level * math.pow((temperature_at_altitude_KELVIN / standard_temperature_at_sea_level_KELVIN), (gravitational_acceleration * molar_mass_of_dry_air) / (ideal_gas_constant * temperature_lapse_rate))
    air_density_at_altitude = pressure_at_altitude / (specific_gas_constant_for_dry_air * temperature_at_altitude_KELVIN)
    thrust = maximum_thrust_at_sea_level_static_conditions * throttle * math.pow((air_density_at_altitude / air_density_at_sea_level), 0.42)
    horizontal_thrust = math.cos(math.radians(pitch_angle)) * thrust
    vertical_thrust = math.sin(math.radians(pitch_angle)) * thrust
    drag = 0.5 * air_density_at_altitude * math.pow(actual_speed, 2) * wing_reference_area * drag_coefficient
    horizontal_drag = -(math.cos(math.radians(flight_path_angle)) * drag)
    vertical_drag = -(math.sin(math.radians(flight_path_angle)) * drag)
    lift = 0.5 * air_density_at_altitude * math.pow(actual_speed, 2) * wing_reference_area * lift_coefficient
    #horizontal_lift = -(math.cos(math.radians(roll_angle)) * math.sin(math.radians(flight_path_angle)) * lift)
    #vertical_lift = math.cos(math.radians(roll_angle)) * math.cos(math.radians(flight_path_angle)) * lift
    #horizontal_lift = -(math.sin(math.radians(flight_path_angle)) * lift)
    #vertical_lift = math.cos(math.radians(flight_path_angle)) * lift
    horizontal_lift = -((lift * math.tan(math.radians(pitch_angle))) / math.pow(1 + math.pow(math.tan(math.radians(roll_angle)), 2) + math.pow(math.tan(math.radians(pitch_angle)), 2), 0.5))
    vertical_lift = lift / math.pow(1 + math.pow(math.tan(math.radians(abs(roll_angle))), 2) + math.pow(math.tan(math.radians(pitch_angle)), 2), 0.5)
    if abs(roll_angle) % 360 >= 90 and abs(roll_angle) % 360 <= 270:
        vertical_lift = -(vertical_lift)
    # find resultant force
    horizontal_force = horizontal_thrust + horizontal_drag + horizontal_lift
    vertical_force = vertical_lift - weight_of_plane + vertical_thrust + vertical_drag
    # a = F/m
    horizontal_acceleration = horizontal_force / mass_of_plane
    vertical_acceleration = vertical_force / mass_of_plane
    # s = ut + 1/2 at^2
    height = height + ((vertical_speed * time_per_frame) + (0.5 * vertical_acceleration * math.pow(time_per_frame, 2)))
    # v = u + at
    horizontal_speed = horizontal_speed + horizontal_acceleration * time_per_frame
    vertical_speed = vertical_speed + vertical_acceleration * time_per_frame
    actual_speed = math.pow(math.pow(horizontal_speed, 2) + math.pow(vertical_speed, 2), 0.5)
    # convert actual_speed(m/s) to actual_speed(knots), then convert to true airspeed(knots)
    airspeed = ((actual_speed * 3.6) / 1.852) * math.pow((air_density_at_sea_level / air_density_at_altitude), 0.5)
    # convert m to feet
    altitude = height * 3.281
    
    return(height, actual_speed, horizontal_speed, vertical_speed, airspeed, altitude)

global standard_atmospheric_pressure_at_sea_level, standard_temperature_at_sea_level_KELVIN, gravitational_acceleration, molar_mass_of_dry_air, temperature_lapse_rate, ideal_gas_constant, specific_gas_constant_for_dry_air, air_density_at_sea_level
# scientific constants
standard_atmospheric_pressure_at_sea_level = 101325
standard_temperature_at_sea_level_KELVIN = 288.15
gravitational_acceleration = 9.80665
molar_mass_of_dry_air = 0.0289644
temperature_lapse_rate = 0.0065
ideal_gas_constant = 8.31432
specific_gas_constant_for_dry_air = 287.05287
air_density_at_sea_level = 1.225

# constants for B777-300ER
global wing_reference_area, mass_of_plane, weight_of_plane, maximum_thrust_at_sea_level_static_conditions
wing_reference_area = 427.8
mass_of_plane = 134300
weight_of_plane = mass_of_plane * gravitational_acceleration
maximum_thrust_at_sea_level_static_conditions = 1024000

#initial game configuration
global fps, time_per_frame
fps = 70
time_per_frame = 1 / fps
roll_angle, pitch_angle, horizontal_speed, vertical_speed, actual_speed, height, altitude, extra_lift_from_flap_setting, oswald_efficiency_factor, flight_path_angle, AoA, lift_coefficient, drag_coefficient = initial_game_configuration()

# initialise pygame
# produce screen {main}
pygame.init()
main = pygame.display.set_mode((1440, 900))
pygame.display.set_caption("Main")

# initialise pygame.joystick
# initialise joystick_1
if pygame.joystick.get_count() > 0:
    pygame.joystick.init()
    joystick_1 = pygame.joystick.Joystick(0)
    joystick_1.init()

# {clock} keeps track of how often the while loop loops
clock = pygame.time.Clock()

# load "swiss_plane.png" as {swiss_plane_image} in a ready format
swiss_plane_image = pygame.image.load("swiss_plane.png").convert_alpha()
width_to_height_ratio = swiss_plane_image.get_width() / swiss_plane_image.get_height()
swiss_plane_image = pygame.transform.scale(swiss_plane_image, (500, 500 / width_to_height_ratio))

change_in_roll_angle = 0
change_in_pitch_angle = 0

change_in_action_due_to_fps = 1 / (fps / 20)

throttle = 0.07
is_running = True
while is_running == True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            is_running = False
    
    if pygame.joystick.get_count() > 0:
        change_in_roll_angle = float(joystick_1.get_axis(0))
        change_in_pitch_angle = float(joystick_1.get_axis(1))
        throttle = (abs((joystick_1.get_axis(3)) - 1) / 2) * 0.93 + 0.07
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            throttle = throttle + 0.03 * change_in_action_due_to_fps
        if keys[pygame.K_s]:
            throttle = throttle - 0.03 * change_in_action_due_to_fps
        if throttle < 0.07:
            throttle = 0.07
        if throttle > 1:
            throttle = 1
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        change_in_roll_angle = (mouse_pos_x - 720) / 720
        change_in_pitch_angle = (mouse_pos_y - 450) / 450
    
    main.fill((192, 192, 192))
    
    roll_angle, pitch_angle = calculate_roll_angle_pitch_angle(roll_angle, pitch_angle, change_in_roll_angle, change_in_pitch_angle)
    
    # function to calculate x, y coordinate of all vertex of sky, ground rectangle background with {roll_angle}, {pitch_angle}, {width_of_background}, {height_of_background}
    # then draw sky, ground rectangle background
    
    # funtion to calculate AoA, lift coefficient, and drag coefficient
    flight_path_angle, AoA, lift_coefficient, drag_coefficient = calculate_lift_drag_coefficient(roll_angle, pitch_angle, horizontal_speed, vertical_speed, extra_lift_from_flap_setting, oswald_efficiency_factor)
    
    # funtion to calculate height, actual_speed, horizontal_speed, vertical_speed, airspeed, altitude
    height, actual_speed, horizontal_speed, vertical_speed, airspeed, altitude = calculate_airspeed_altitude(flight_path_angle, height, roll_angle, pitch_angle, actual_speed, lift_coefficient, drag_coefficient, horizontal_speed, vertical_speed, throttle)
    
    draw_sky_ground_background(roll_angle, pitch_angle, 1440, 900, 0, 0, (135, 206, 235), (34, 139, 34))
    draw_primary_flight_display(roll_angle, pitch_angle, airspeed, altitude)
    
    airspeed_label_main = pygame.font.Font(None, 60).render("AoA: " + str(round(AoA, 0))[:-2], True, (255, 255, 255))
    main.blit(airspeed_label_main, (0, 0))
    
    airspeed_label_main = pygame.font.Font(None, 60).render("Airspeed: " + str(round(airspeed, 0))[:-2] + " kts", True, (255, 255, 255))
    main.blit(airspeed_label_main, (0, 50))
    
    altitude_label_main = pygame.font.Font(None, 60).render("Altitude: " + str(round(altitude, 0))[:-2] + " fts", True, (255, 255, 255))
    main.blit(altitude_label_main, (0, 100))
    
    airspeed_label_main = pygame.font.Font(None, 30).render("Horizontal speed: " + str(round(horizontal_speed, 0))[:-2], True, (255, 255, 255))
    main.blit(airspeed_label_main, (0, 150))
    
    altitude_label_main = pygame.font.Font(None, 30).render("Vertical speed: " + str(round(vertical_speed, 0))[:-2], True, (255, 255, 255))
    main.blit(altitude_label_main, (0, 200))
    
    airspeed_label_main = pygame.font.Font(None, 30).render("Roll angle: " + str(round(roll_angle, 0))[:-2], True, (255, 255, 255))
    main.blit(airspeed_label_main, (0, 250))
    
    airspeed_label_main = pygame.font.Font(None, 30).render("throttle: " + str(throttle), True, (255, 255, 255))
    main.blit(airspeed_label_main, (0, 300))
    
    main.blit(swiss_plane_image, (470, 550))
    
    if AoA >= 20 or AoA <= -50 or altitude <= 0:
        stall_crash_label_main = pygame.font.Font(None, 200).render("Stall / Crash", True, (255, 255, 255))
        main.blit(stall_crash_label_main, (100, 200))
        pygame.display.flip()
        clock.tick(fps / 150)
        roll_angle, pitch_angle, horizontal_speed, vertical_speed, actual_speed, height, altitude, extra_lift_from_flap_setting, oswald_efficiency_factor, flight_path_angle, AoA, lift_coefficient, drag_coefficient = initial_game_configuration()
        continue
    
    pygame.display.flip()
    
    clock.tick(fps)
    
# hs