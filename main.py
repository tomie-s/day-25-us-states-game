import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                    prompt='What is another State name?').title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        correct_states.append(answer_state)
        state_pos = data[data['state'] == answer_state].iloc[0]

        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(state_pos.x, state_pos.y)
        pen.write(answer_state)
