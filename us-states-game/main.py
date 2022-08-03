import turtle
import pandas


def write_state_name(name, x, y):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(x, y)
    state.write(name)


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

states = pandas.read_csv("50_states.csv")
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states['state'].to_list())} states Correct",
                                    prompt="What's another state's name?")
    if answer_state.title() == "Exit":
        incorrect_state = [state for state in states["state"].to_list() if state not in guessed_states]
        incorrect_states = {
            "State": incorrect_state
        }
        states_to_learn = pandas.DataFrame(incorrect_states)
        states_to_learn.to_csv("states_to_learn")
        break
    elif answer_state.title() in states["state"].to_list():
        state_name = answer_state.title()
        state_xcor = int(states[states["state"] == answer_state.title()].x)
        state_ycor = int(states[states["state"] == answer_state.title()].y)
        write_state_name(state_name, state_xcor, state_ycor)
        guessed_states.append(state_name)

