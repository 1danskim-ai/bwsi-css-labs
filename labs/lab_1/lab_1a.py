"""
lab_1a.py

The first lab in the BWSI CSS course. To complete this lab, fill out the variable on line 10
with your name. Then, save the code, add it to the staging area, and commit it to the Git tree.

This is to simulate a change made on a robot: robot_speed = 3 # m/s
"""

def main():
    print("Hello World!")

    name = "Daniel Kim" # TODO: Insert your name between the double quotes
    intro = "Hello all! My name is Daniel Kim, and I am a junior at Southern Lehigh High School (near Bethlehem, Pennsylvania). I am on my schools FRC team, mainly as a programmer, with a passion for physics and calculus. My visit to the Kennedy Space Center when I was around 10 made me really interested in all things space and engineering. This course seems like an exciting step in translating my interest and coursework into something tangible, beyond competition robotics."

    print(f"{name}, Welcome to the CSS course!")
    print("My introduction: " + intro)

if __name__ == "__main__":
    main()
