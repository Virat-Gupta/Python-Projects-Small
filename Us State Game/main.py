import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATE QUIZ")

IMAGE = "Us State Game\\blank_states_img.gif"
screen.addshape(IMAGE)

turtle.shape(IMAGE)
data = pandas.read_csv("Us State Game\\50_states.csv")
all_states = data["state"].to_list()
states_done = set()

writing_Turtle = turtle.Turtle()
writing_Turtle.penup()
writing_Turtle.hideturtle()


while len(states_done) < 50 :
    guessed_word = str(screen.textinput(title=f"{len(states_done)}/50 done", prompt="Guess Another state")).title()
    if guessed_word == "Exit":
        missing_states = []
        for state in all_states:
            if state not in states_done:
                missing_states.append(state)
        
        new_data = pandas.DataFrame(missing_states).to_csv("Us State Game\\states_to_learn.csv")
        break

    if guessed_word in all_states and guessed_word not in states_done :
        state_data = data[data.state == guessed_word]
        writing_Turtle.goto(int(state_data.x),int(state_data.y)) # type: ignore
        
        writing_Turtle.write(f"{guessed_word}", align="center", font=("Courier",8,"normal"))

        states_done.add(guessed_word)
screen.exitonclick()