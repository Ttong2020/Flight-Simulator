import pygame
import math

def matrix_calculation(*args):
    
    matrices_to_calculate_tuple = args
    matrix_1 = matrices_to_calculate_tuple[0]
    matrices_to_calculate_tuple = matrices_to_calculate_tuple[1:]
    for matrix in range(1, len(matrices_to_calculate_tuple), 2):
        operation = matrices_to_calculate_tuple[matrix - 1]
        matrix_2 = matrices_to_calculate_tuple[matrix]
        if (len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]) and operation == "+") or (len(matrix_1[0]) == len(matrix_2) and operation == "*"):
            result_matrix = []
            for matrix_1_row in range(len(matrix_1)):
                result_matrix.append([])
                for matrix_2_column in range(len(matrix_2[0])):
                    result_matrix[matrix_1_row].append(0)
            
            for matrix_1_row in range(len(matrix_1)):
                for matrix_2_column in range(len(matrix_2[0])):
                    if operation == "+":
                        result_matrix[matrix_1_row][matrix_2_column] = matrix_1[matrix_1_row][matrix_2_column] + matrix_2[matrix_1_row][matrix_2_column]
                    if operation == "*":
                        for matrix_1_column in range(len(matrix_1[0])):
                            result_matrix[matrix_1_row][matrix_2_column] = result_matrix[matrix_1_row][matrix_2_column] + (matrix_1[matrix_1_row][matrix_1_column] * matrix_2[matrix_1_column][matrix_2_column])
            
            matrix_1 = result_matrix
    
    return(result_matrix)



def matrix_multiplication(*args):
    matrices_to_multiply_tuple = args
    matrix_1 = matrices_to_multiply_tuple[0]
    matrices_to_multiply_tuple = matrices_to_multiply_tuple[1:]
    for matrix in range(len(matrices_to_multiply_tuple)):
        matrix_2 = matrices_to_multiply_tuple[matrix]
        if len(matrix_1[0]) == len(matrix_2):
            result_matrix = []
            for matrix_1_row in range(len(matrix_1)):
                result_matrix.append([])
                for matrix_2_column in range(len(matrix_2[0])):
                    result_matrix[matrix_1_row].append(0)
            for matrix_1_row in range(len(matrix_1)):
                for matrix_2_column in range(len(matrix_2[0])):
                    for matrix_1_column in range(len(matrix_1[0])):
                        result_matrix[matrix_1_row][matrix_2_column] = result_matrix[matrix_1_row][matrix_2_column] + (matrix_1[matrix_1_row][matrix_1_column] * matrix_2[matrix_1_column][matrix_2_column])
            
            matrix_1 = result_matrix
    
    return(result_matrix)




matrix_2 = [[4,3],[2,1]]
matrix_1 = [[5,6],[7,8]]
matrix_3 = [[5,6],[7,8]]
#matrix_addition(matrix_1, matrix_2, matrix_3)

def initial_game_configuration():

    roll_angle = 0
    pitch_angle = 0
    yaw_angle = 0
    horizontal_speed = 103
    vertical_speed = 0
    actual_speed = 103
    indicated_airspeed = 170
    height = 3352.8
    altitude = height * 3.281
    extra_lift_from_flap_setting = 0
    oswald_efficiency_factor = 0.87
    flight_path_angle, AoA, lift_coefficient, drag_coefficient = calculate_lift_drag_coefficient(pitch_angle, horizontal_speed, vertical_speed, extra_lift_from_flap_setting, oswald_efficiency_factor)
    AoA = -3
    fps = 70
    time_per_frame = 1 / fps
    
    return(roll_angle, pitch_angle, yaw_angle, horizontal_speed, vertical_speed, actual_speed, indicated_airspeed, height, altitude, extra_lift_from_flap_setting, oswald_efficiency_factor, flight_path_angle, AoA, lift_coefficient, drag_coefficient, fps, time_per_frame)

# calculate x, y coordinate of all vertex of sky, ground rectangle background with {roll_angle}, {pitch_angle}, {width_of_visible_screen}, {height_of_visible_screen}
# then draw sky, ground rectangle background with {x_axis_frame}, {y_axis_frame}
def draw_sky_ground_background(roll_angle, pitch_angle, yaw_angle, width_of_visible_screen, height_of_visible_screen, x_axis_frame, y_axis_frame, sky_colour, ground_colour):
    
    background_pitch_yaw_angle = pitch_angle + -(yaw_angle) * math.sin(math.radians(roll_angle))
    change_in_action_due_to_height_of_visible_screen = height_of_visible_screen / 100
    #x_y_center_of_background = [(width_of_visible_screen / 2) + (math.sin(math.radians(roll_angle)) * (pitch_angle - yaw_angle) * change_in_action_due_to_height_of_visible_screen), (height_of_visible_screen / 2) + math.cos(math.radians(roll_angle)) * (pitch_angle - yaw_angle) * change_in_action_due_to_height_of_visible_screen]
    
    frame_visible_screen_main = pygame.Surface((width_of_visible_screen, height_of_visible_screen))
    
    if 0 == 1:
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
    
    x_axis_to_translate = math.sin(math.radians(roll_angle)) * background_pitch_yaw_angle * 16
    y_axis_to_translate = math.cos(math.radians(roll_angle)) * background_pitch_yaw_angle * 16
    rotate_matrix = [[math.cos(math.radians(roll_angle)), math.sin(math.radians(roll_angle))], [-(math.sin(math.radians(roll_angle))), math.cos(math.radians(roll_angle))]]
    translate_matrix = [[x_axis_to_translate, x_axis_to_translate, x_axis_to_translate, x_axis_to_translate, x_axis_to_translate, x_axis_to_translate], [y_axis_to_translate, y_axis_to_translate, y_axis_to_translate, y_axis_to_translate, y_axis_to_translate, y_axis_to_translate]]
    result_matrix = matrix_calculation(rotate_matrix, "*", origin_coordinate_matrix, "+", translate_matrix, "+", translate_matrix_to_final_coordinate)
    
    pygame.draw.polygon(frame_visible_screen_main, sky_colour, [(result_matrix[0][0], result_matrix[1][0]), (result_matrix[0][1], result_matrix[1][1]), (result_matrix[0][3], result_matrix[1][3]), (result_matrix[0][2], result_matrix[1][2])])
    pygame.draw.polygon(frame_visible_screen_main, ground_colour, [(result_matrix[0][2], result_matrix[1][2]), (result_matrix[0][3], result_matrix[1][3]), (result_matrix[0][5], result_matrix[1][5]), (result_matrix[0][4], result_matrix[1][4])])
    main.blit(frame_visible_screen_main, (x_axis_frame, y_axis_frame))

def draw_primary_flight_display(roll_angle, pitch_angle, indicated_airspeed, altitude):
    
    move_x_axis = 0
    move_y_axis = 0
    x_y_center_of_primary_flight_display = [100 + move_x_axis + (250 / 2), 500 + move_y_axis + (250 / 2)]
    pygame.draw.rect(main, (40, 40, 40), (100 + move_x_axis, 500 + move_y_axis, 250, 250))
    draw_sky_ground_background(roll_angle, pitch_angle, yaw_angle, 150, 150, 150 + move_x_axis, 550 + move_y_axis, (60, 134, 189), (137, 73, 34))
    pygame.draw.rect(main, (0, 0, 0), (x_y_center_of_primary_flight_display[0] - 5, x_y_center_of_primary_flight_display[1] - 5, 10, 10))
    #pygame.draw.polygon(main, (0, 0, 0), [(x_y_center_of_primary_flight_display[0] - 120 + move_x_axis, x_y_center_of_primary_flight_display[1] - 5 + move_y_axis), (10, 10), (10, 10)])

# function to calculate {roll_angle}, {pitch_angle}
def calculate_roll_angle_pitch_angle_yaw_angle(roll_angle, pitch_angle, yaw_angle, roll_input, pitch_input, yaw_input, yaw_angle_limit, indicated_airspeed, AoA):
    global fps, time_per_frame
    
    change_in_action_due_to_fps = 1 / (fps / 20)
    roll_angle = roll_angle + roll_input * time_per_frame * indicated_airspeed * 0.1
    pitch_angle_change_joystick = math.cos(math.radians(roll_angle)) * pitch_input
    pitch_angle = pitch_angle + (time_per_frame * indicated_airspeed * pitch_input * math.cos(math.radians(roll_angle))) / (abs(AoA) + 20)
    yaw_angle = yaw_angle + (time_per_frame * indicated_airspeed) * ((yaw_input * 0.5) / (abs(yaw_angle) + 1.5) - (yaw_angle - yaw_angle_limit * yaw_input) * 0.003)
    if yaw_angle > yaw_angle_limit:
        yaw_angle = yaw_angle_limit
    if yaw_angle < -(yaw_angle_limit):
        yaw_angle = -(yaw_angle_limit)
    return(roll_angle, pitch_angle, yaw_angle)

# function to calculate {flight_path_angle}, {AoA}, {lift_coefficient}, {drag_coefficient}
def calculate_lift_drag_coefficient(pitch_angle, horizontal_speed, vertical_speed, extra_lift_from_flap_setting, oswald_efficiency_factor):
    
    flight_path_angle = math.degrees(math.atan(vertical_speed / horizontal_speed))
    # AoA = pitch_angle - flight_path_angle
    #AoA = (pitch_angle - flight_path_angle) * math.cos(math.radians(roll_angle))
    AoA = pitch_angle - flight_path_angle
    critical_AoA = 13
    if AoA >= critical_AoA:
        # lift_coefficient = (extra_lift_from_flap_setting) + lift_curve_slope * ((critical_AoA - (AoA - critical_AoA) / 3) - zero_lift_angle_of_attack)
        lift_coefficient = (extra_lift_from_flap_setting) + 0.09 * ((13 - (AoA - 13) / 3) - (-3))
    else:
        # lift_coefficient = (extra_lift_from_flap_setting) + lift_curve_slope * (AoA - zero_lift_angle_of_attack)
        lift_coefficient = (extra_lift_from_flap_setting) + 0.09 * (AoA - (-3))
    # induced_drag_factor = 1 / (math.pi * oswald_efficiency_factor * aspect ratio)
    induced_drag_factor = 1 / (math.pi * oswald_efficiency_factor * 9.61)
    # drag_coefficient = drag_coefficient_for_zero_lift + (induced_drag_factor * math.pow(lift_coefficient, 2))
    drag_coefficient = 0.0212 + (induced_drag_factor * math.pow(lift_coefficient, 2))
    
    if AoA == 0:
        AoA = 0.00000000001
    
    return(flight_path_angle, AoA, lift_coefficient, drag_coefficient)

# function to calculate {height}, {actual_speed}, {horizontal_speed}, {vertical_speed}, {indicated_airspeed}, {altitude}
def calculate_indicated_airspeed_altitude(flight_path_angle, height, roll_angle, pitch_angle, actual_speed, lift_coefficient, drag_coefficient, horizontal_speed, vertical_speed, throttle):

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
    # convert actual_speed(m/s) to actual_speed(knots), then convert to true indicated_airspeed(knots)
    indicated_airspeed = ((actual_speed * 3.6) / 1.852) * math.pow((air_density_at_sea_level / air_density_at_altitude), 0.5)
    # convert m to feet
    altitude = height * 3.281
    
    return(height, actual_speed, horizontal_speed, vertical_speed, indicated_airspeed, altitude)

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
wing_reference_area = 427.8
mass_of_plane = 134300
weight_of_plane = mass_of_plane * gravitational_acceleration
maximum_thrust_at_sea_level_static_conditions = 1024000
yaw_angle_limit = 15

#initial game configuration
roll_angle, pitch_angle, yaw_angle, horizontal_speed, vertical_speed, actual_speed, indicated_airspeed, height, altitude, extra_lift_from_flap_setting, oswald_efficiency_factor, flight_path_angle, AoA, lift_coefficient, drag_coefficient, fps, time_per_frame = initial_game_configuration()
width_of_background = math.pow(math.pow(1440, 2) + math.pow(900, 2), 0.5)
height_of_background = 900 * 10
translate_matrix_to_final_coordinate = [[1440 / 2, 1440 / 2, 1440 / 2, 1440 / 2, 1440 / 2, 1440 / 2],[900 / 2, 900 / 2, 900 / 2, 900 / 2, 900 / 2, 900 / 2]]
origin_coordinate_matrix = [[-(width_of_background / 2), width_of_background / 2, -(width_of_background / 2), width_of_background / 2, -(width_of_background / 2), width_of_background / 2],[-(height_of_background / 2), -(height_of_background / 2), 0, 0, height_of_background / 2, height_of_background / 2]]

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

roll_input = 0
pitch_input = 0
yaw_input = 0
throttle = 0.07
is_running = True

while is_running == True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            is_running = False
    
    if pygame.joystick.get_count() > 0:
        roll_input = float(joystick_1.get_axis(0))
        pitch_input = float(joystick_1.get_axis(1))
        yaw_input = float(joystick_1.get_axis(2))
        throttle = (abs((joystick_1.get_axis(3)) - 1) / 2) * 0.93 + 0.07
    else:
        yaw_input = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            throttle = throttle + 0.6 * time_per_frame
        if keys[pygame.K_s]:
            throttle = throttle - 0.6 * time_per_frame
        if throttle < 0.07:
            throttle = 0.07
        if throttle > 1:
            throttle = 1
        if keys[pygame.K_a]:
            yaw_input = -1
        if keys[pygame.K_d]:
            yaw_input = 1
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        roll_input = (mouse_pos_x - 720) / 720
        pitch_input = (mouse_pos_y - 450) / 450
    
    main.fill((192, 192, 192))
    
    roll_angle, pitch_angle, yaw_angle = calculate_roll_angle_pitch_angle_yaw_angle(roll_angle, pitch_angle, yaw_angle, roll_input, pitch_input, yaw_input, yaw_angle_limit, indicated_airspeed, AoA)
    
    # function to calculate x, y coordinate of all vertex of sky, ground rectangle background with {roll_angle}, {pitch_angle}, {width_of_background}, {height_of_background}
    # then draw sky, ground rectangle background
    
    # funtion to calculate AoA, lift coefficient, and drag coefficient
    flight_path_angle, AoA, lift_coefficient, drag_coefficient = calculate_lift_drag_coefficient(pitch_angle, horizontal_speed, vertical_speed, extra_lift_from_flap_setting, oswald_efficiency_factor)
    
    # funtion to calculate height, actual_speed, horizontal_speed, vertical_speed, indicated_airspeed, altitude
    height, actual_speed, horizontal_speed, vertical_speed, indicated_airspeed, altitude = calculate_indicated_airspeed_altitude(flight_path_angle, height, roll_angle, pitch_angle, actual_speed, lift_coefficient, drag_coefficient, horizontal_speed, vertical_speed, throttle)
    
    draw_sky_ground_background(roll_angle, pitch_angle, yaw_angle, 1440, 900, 0, 0, (135, 206, 235), (34, 139, 34))
    #draw_primary_flight_display(roll_angle, pitch_angle, indicated_airspeed, altitude)
    
    indicated_airspeed_label_main = pygame.font.Font(None, 60).render("AoA: " + str(round(AoA, 0))[:-2], True, (255, 255, 255))
    main.blit(indicated_airspeed_label_main, (0, 0))
    
    indicated_airspeed_label_main = pygame.font.Font(None, 60).render("indicated_airspeed: " + str(round(indicated_airspeed, 0))[:-2] + " kts", True, (255, 255, 255))
    main.blit(indicated_airspeed_label_main, (0, 50))
    
    altitude_label_main = pygame.font.Font(None, 60).render("Altitude: " + str(round(altitude, 0))[:-2] + " fts", True, (255, 255, 255))
    main.blit(altitude_label_main, (0, 100))
    
    indicated_airspeed_label_main = pygame.font.Font(None, 30).render("Horizontal speed: " + str(round(horizontal_speed, 0))[:-2], True, (255, 255, 255))
    main.blit(indicated_airspeed_label_main, (0, 150))
    
    altitude_label_main = pygame.font.Font(None, 30).render("Vertical speed: " + str(round(vertical_speed, 0))[:-2], True, (255, 255, 255))
    main.blit(altitude_label_main, (0, 200))
    
    indicated_airspeed_label_main = pygame.font.Font(None, 30).render("Roll angle: " + str(round(roll_angle, 0))[:-2], True, (255, 255, 255))
    main.blit(indicated_airspeed_label_main, (0, 250))
    
    indicated_airspeed_label_main = pygame.font.Font(None, 30).render("throttle: " + str(throttle), True, (255, 255, 255))
    main.blit(indicated_airspeed_label_main, (0, 300))
    
    indicated_airspeed_label_main = pygame.font.Font(None, 30).render("Yaw angle: " + str(round(yaw_angle, 0))[:-2], True, (255, 255, 255))
    main.blit(indicated_airspeed_label_main, (0, 350))
    
    main.blit(swiss_plane_image, (470, 550))
    
    if altitude <= 0:
        stall_crash_label_main = pygame.font.Font(None, 200).render("Stall / Crash", True, (255, 255, 255))
        main.blit(stall_crash_label_main, (100, 200))
        pygame.display.flip()
        clock.tick(fps / 150)
        roll_angle, pitch_angle, yaw_angle, horizontal_speed, vertical_speed, actual_speed, indicated_airspeed, height, altitude, extra_lift_from_flap_setting, oswald_efficiency_factor, flight_path_angle, AoA, lift_coefficient, drag_coefficient, fps, time_per_frame = initial_game_configuration()
        continue
    
    pygame.display.flip()
    
    clock.tick(fps)




exit()
#global standard_atmospheric_pressure_at_sea_level, standard_temperature_at_sea_level_KELVIN, gravitational_acceleration, molar_mass_of_dry_air, temperature_lapse_rate, ideal_gas_constant, specific_gas_constant_for_dry_air, air_density_at_sea_level
#global wing_reference_area, mass_of_plane, weight_of_plane, maximum_thrust_at_sea_level_static_conditions
