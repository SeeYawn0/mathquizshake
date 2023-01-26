input.onButtonPressed(Button.A, function () {
    int1 = randint(0, 100)
    int2 = randint(0, 100)
    basic.showNumber(int1)
    basic.pause(1000)
    if (operator == 0) {
        basic.showString("+")
    } else if (operator == 1) {
        basic.showString("-")
    } else if (operator == 2) {
        basic.showString("x")
    } else {
        basic.showString("/")
    }
    basic.pause(1000)
    basic.showNumber(int2)
    basic.pause(1000)
    basic.showString("=?")
})
input.onButtonPressed(Button.B, function () {
    if (operator == 0) {
        basic.showNumber(int1 + int2)
    } else if (operator == 1) {
        basic.showNumber(int1 - int2)
    } else if (operator == 2) {
        basic.showNumber(int1 * int2)
    } else {
        basic.showNumber(int1 / int2)
    }
})
input.onGesture(Gesture.Shake, function () {
    if (operator > 3) {
        operator = 0
    } else {
        operator += 1
    }
})
let int2 = 0
let int1 = 0
let operator = 0
operator = 0
