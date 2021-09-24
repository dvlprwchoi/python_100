# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

###
# Old codes
###

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def one():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right() == True:
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while wall_in_front() != True:
#         move()
#     turn_left()

# #for step in range (6):
# #    one()

# #number_of_hurdles = 6
# #while number_of_hurdles > 0:
# #    one()
# #    number_of_hurdles -= 1
# #    print(number_of_hurdles)

# #while at_goal() != True:
# #    one()


# while at_goal() != True:
#     if wall_in_front():
#         jump()
#     else:
#         move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


# Come back after Day 15 to debug
