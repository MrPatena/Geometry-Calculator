# Libaries
import math
import time
import sys

history = []
calculations = [
  "1) Circle_area",
  "2) Circle_circumference",
  "3) Circle_area_sector",
  "4) Arc_length",
  "5) Area_segment",
  "6) Volume_sphere",
  "7) Surface_Area_Sphere",
  "8) Volume_cone",
  "9) Volume_prism",
  "10) Surface_Area_cone",
  "11) Cosine_rule_angle",
  "12) Cosine_rule_side",
  "13) Sine_rule_angle"
]

# Function for animate text ----credits---- https://www.youtube.com/watch?v=GCccNX7F5Tg&t=172s&ab_channel=GolbargCode
def animateText(text, delay):
  for char in str(text):
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
    
  print()


animateText("Running Geometry Calculator...\n", 0.1)
animateText("Welcome to my Geometry Calculator!", 0.05)

count = 0

# 
while count <= len(calculations):
  for calculation in calculations:
    count += 1
    time.sleep(0.5)
    print(calculation)
  break

while True:
  # Adds a time delay of 1 sec between each time the program loops
  time.sleep(1)

  ##############
  #calculations#
  ##############

  def geometryCalculator():
    animateText(
      "Type the number corresponding to the calculation you would like to calculate: ",
      0.02)
    type = str(input())

    if type == "1":
      # circle_area
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      return (math.pi * (radius)**2)

    elif type == "2":
      # circle_circumference
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      return (2 * math.pi * radius)

    elif type == "3":
      # circle_area_sector
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      animateText("Enter angle: ", 0.05)
      angle = float(input())
      return ((angle / 360) * math.pi * (radius)**2)

    elif type == "4":
      # arc_length
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      animateText("Enter angle: ", 0.05)
      angle = float(input())
      return ((angle / 360) * (2 * math.pi * radius))

    elif type == "5":
      # Area_segment
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      animateText("Enter angle: ", 0.05)
      angle = float(input())
      return (((angle / 360) * math.pi * (radius)**2) -
              ((1 / 2) * math.sin(math.radians(angle)) * (radius)**2))

    elif type == "6":
      # Volume_sphere
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      return (4 / 3 * math.pi * (radius)**3)

    elif type == "7":
      # Surface_Area_Sphere
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      return (4 * math.pi * (radius)**2)

    elif type == "8":
      # Volume_cone
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      animateText("Enter vertical height: ", 0.05)
      v_height = float(input())
      return (1 / 3 * math.pi * (radius)**3 * v_height)

    elif type == "9":
      # Volume_prisim
      animateText("Enter length: ", 0.05)
      length = float(input())
      animateText("Enter area of cross-section: ", 0.05)
      cross_section = float(input())
      return (cross_section * length)

    elif type == "10":
      # Surface_Area_cone
      animateText("Enter radius: ", 0.05)
      radius = float(input())
      animateText("Enter slant-height: ", 0.05)
      slant_height = float(input())
      return ((math.pi * radius * slant_height) + (math.pi * (radius)**2))

    elif type == "11":
      # Cosine_rule_angle
      animateText("Enter side AB: ", 0.05)
      AB = float(input())
      animateText("Enter side BC: ", 0.05)
      BC = float(input())
      animateText("Enter side AC: ", 0.05)
      AC = float(input())

      animateText("Enter missing angle (A, B or C): ", 0.05)
      missing_angle = str(input()).upper()

      sum_of_sqr = {"A": AB**2 + AC**2, "B": AB**2 + BC**2, "C": BC**2 + AC**2}
      sqr_of_opp_side = {"A": BC**2, "B": AC**2, "C": AB**2}
      denominator_sum = {"A": 2 * AB * AC, "B": 2 * BC * AB, "C": 2 * AC * BC}

      fraction = (sum_of_sqr[missing_angle] - sqr_of_opp_side[missing_angle]
                  ) / denominator_sum[missing_angle]

      return (math.degrees(math.acos(fraction)))

    elif type == "12":
      #Cosine_rule_side
      
      print("Before you enter any values, LABEL your triangle CORRECTLY with the letter A as your angle!")
      
      animateText("Enter side AB: ", 0.05)
      AB = float(input())
      animateText("Enter side AC: ", 0.05)
      AC = float(input())
      animateText("Enter angle A: ", 0.05)
      angle_A = math.radians(float(input()))

      missing_side = "A"

      sum_of_sqr = {"A": AB**2 + AC**2}
      sum_of_opp_side = {"A": 2 * AB * AC * math.cos(angle_A)}

      answer = sum_of_sqr[missing_side] - sum_of_opp_side[missing_side]

      return (math.sqrt(answer))

    elif type == "13":
      # Sine_rule_angle ----credits----https://stackoverflow.com/questions/61845928/problems-with-calculating-law-of-sines
      animateText("Enter GIVEN angle in degrees: ", 0.05)
      x = float(input())
      animateText("Length of side opposite GIVEN angle: ", 0.05)
      y = float(input())
      animateText("Length of side opposite UNKOWN angle: ", 0.05)
      z = float(input())

      a = (math.sin(math.radians(x)) / y) * z
      b = math.degrees(math.asin(a))

      return (b)

    else:
      return ("Error")

      ##########
      #rounding#
      ##########

  def rounding(calc_answer):
    if calc_answer != "Error":
      # Checks if there is no errors in geometryCalculator()
      animateText("Would you like to round your answer (Y/N): ", 0.05)
      round_answer = str(input()).upper()

      if round_answer == "Y":
        animateText(
          "Enter the number of decimal places you would like to round up by: ",
          0.05)
        places = int(input())

        rounded_answer = round(calc_answer, places)
        animateText(f"\nYour answer is: {str(rounded_answer)}", 0.05)

        history.append(rounded_answer)

      elif round_answer == "N":
        animateText(f"\nYour answer is: {calc_answer}", 0.05)

        history.append(calc_answer)

      else:
        animateText("Please try again", 0.05)
        pass

    elif calc_answer == "Error":
      animateText("\nPlease try again", 0.05)

      #########
      #history#
      #########

  def calc_history():
    animateText("\nDo you want to check your history (Y/N): ", 0.05)
    checker = str(input()).upper()

    if checker == "Y":
      animateText(str(history), 0.02)

    elif checker == "N":
      pass

    else:
      animateText("\nPlease try again", 0.05)
      pass

  rounding(geometryCalculator())
  calc_history()

  animateText("\nDo you want to repeat the program? (Y/N)", 0.05)
  repeat = input().upper()

  

  if repeat.upper() != 'Y':
    animateText("\nGeometry Calculator exit...", 0.2)
    break
