""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Assignment 1 for Tprg 2131 intro week 1-2


ADD YOUR NAME, STUDENT ID and SECTION CRN here.
Ryan Groskopf
Strudent ID: 100880623
date: 2023-09-20

This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency , bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.
"""
import math

print("Series resonant circuit calculator\n(CTRL-C to quit)")
# Looked up example of functions from https://www.geeksforgeeks.org/python-functions/

def ser_calculations(milhurt, micfar, ohms):
    # Calculate the resonant frequency, the bandwidth, and the Q factor of this circuit.
    
    # Convert units.
    hurtz = milhurt / 1000.0  # mH > H
    far = micfar / 1000000  # uF > F
    
    # Calculation for resonant frequency of a SERIES circuit.
    res_freq = 1 / (2 * math.pi * math.sqrt(hurtz * far))

    # BW stands for bandwidth.
    # Calculation for bandwidth of a SERIES circuit.
    BW = ohms / hurtz

    # Calculate the quality factor (Q) of a SERIES circuit.
    FQ = (1 / ohms) * (math.sqrt(hurtz / far))

    return res_freq, BW, FQ

def parl_calculations(milhurt, micfar, ohms):
    # Calculate the resonant frequency, bandwidth, and Q factor for a parallel resonant circuit.
    # Convert units.
    hurtz = milhurt / 1000.0  # mH > H
    far = micfar / 1000000.0  # uF > F
    
    # Calculation for resonant frequency of a parallel circuit.
    res_freq = 1 / (2 * math.pi * math.sqrt(hurtz * far))
    
    # Calculation for bandwidth of a parallel circuit
    BW = ohms * hurtz
    
    # Calculate the quality factor (Q) of a parallel circuit.
    FQ = (ohms) * (math.sqrt(far / hurtz))

    return res_freq, BW, FQ

def series_resistance(res1, res2):
    # Calculats the  series resistance of two resistors.
    return res1 + res2

def parallel_resistance(res1, res2):
    # Calculates the  parallel resistance of two resistors.
    return (res1 * res2) / (res1 + res2)

def rc_time_constant(resistor, capacitor):
    # Calculate the RC time constant of a resistor-capacitor combination.
    return resistor * capacitor

while True:
    while True:
        # This is the menu that asks the user what they would like to select.
        print("Menu:\nOption 1: Series (type 's')\nOption 2: Parallel (type 'p')\nOption 3: Calculate Series Resistance (type 'sr')\nOption 4: Calculate Parallel Resistance (type 'pr')\nOption 5: Calculate RC Time Constant (type 'rc')\nType: 'Q' to exit the program")
        # Learned to use \n from https://www.freecodecamp.org/news/print-newline-in-python/
        menu = input("Enter: ").strip().lower()
        #strip remove leading and trailing whitespace.
        #lower makes anything entered a lowercase letter.
        #lernt these two from https://www.w3schools.com/python/ref_string_strip.asp and https://www.programiz.com/python-programming/methods/string/lower

        if menu == 'q':
            print("Exiting the program.")
            exit()
        
        if menu == 's' or menu == 'p' or menu == 'sr' or menu == 'pr' or menu == 'rc':
            break
        else:
            print("Invalid input. Please enter 's', 'p', 'sr', 'pr', or 'rc'.")
    
    if menu == 's' or menu == 'p':
        # If statement that gathers the inputs from the user whewn asking for LRC.
        milhurt = float(input("What is the inductance in mH? "))
        micfar = float(input("What is the capacitance in uF? "))
        ohms = float(input("What is the resistance in ohms? "))

        # If statement that prevents the user from putting in a negative number.
        # Will not give the Calculations until all positive numbers are added.
        if milhurt <= 0.0 or micfar <= 0.0 or ohms <= 0.0:
            print("All values must be greater than zero. Please re-enter.")
            continue
# Learned the function from https://www.geeksforgeeks.org/python-continue-statement/

# 'sr' is for series resistance, this is for input of series resistance of two resistors
    if menu == 'sr':
        res1 = float(input("Enter the value of resistor 1 in ohms: "))
        res2 = float(input("Enter the value of resistor 2 in ohms: "))
        series_res = series_resistance(res1, res2)
        print("Equivalent Series Resistance:", series_res, "ohms")
        # Input for parallel resistance of two resistors
    elif menu == 'pr':
        res1 = float(input("Enter the value of resistor 1 in ohms: "))
        res2 = float(input("Enter the value of resistor 2 in ohms: "))
        parallel_res = parallel_resistance(res1, res2)
        print("Equivalent Parallel Resistance:", parallel_res, "ohms")
    elif menu == 'rc':
        #input for RC time constant of aresistor-capacitor combination
        resistor = float(input("Enter the value of the resistor in ohms: "))
        capacitor = float(input("Enter the value of the capacitor in uF: "))
        rc_constant = rc_time_constant(resistor, capacitor / 1000000)  # Convert uF to F
        print("RC Time Constant:", rc_constant, "seconds")
    else:
          # Inputs for LRC parallel or series
        if menu == 's':
            res_freq, BW, FQ = ser_calculations(milhurt, micfar, ohms)
            print("Resonant frequency:", res_freq, "Hz", "Bandwidth:", BW, "Hz", "Q factor:", FQ)
        elif menu == 'p':
            res_freq, BW, FQ = parl_calculations(milhurt, micfar, ohms)
            print("Resonant frequency:", res_freq, "Hz", "Bandwidth:", BW, "Hz", "Q factor:", FQ)

