def on_button_pressed_a():
    global int1, int2
    int1 = randint(0, 10)
    int2 = randint(0, 10)
    basic.show_number(int1)
    basic.pause(1000)
    if operator == 0:
        basic.show_string("+")
    elif operator == 1:
        basic.show_string("-")
    elif operator == 2:
        basic.show_string("x")
    else:
        basic.show_string("/")
    basic.pause(1000)
    basic.show_number(int2)
    basic.pause(1000)
    basic.show_string("=?")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if operator == 0:
        basic.show_number(int1 + int2)
    elif operator == 1:
        basic.show_number(int1 - int2)
    elif operator == 2:
        basic.show_number(int1 * int2)
    else:
        basic.show_number(int1 / int2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global operator
    if operator > 3:
        operator = 0
    else:
        operator += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

int2 = 0
int1 = 0
operator = 0
operator = 0