import math
import sys

print("""
Supported system types:
  1. <NORMAL SYSTEMS / TBD>
  2. P-Type Systems
  3. S-Type Systems <TBD>

2. P-Type Systems

A P-Type star system is a binary star system (a star system with two suns) where the planets orbit
the 'barrycentre'.

UNITS AND OTHER EXPLANATIONS
Solar masses:
  - 1 solar mass is equal to the mass of our own sun.
  - 0.5 solar masses are equal to half the mass of our own sun.

Eccentricity:
  - An excentricity of 0 means a perfect circular orbit.
  - An excentricity of 1 means a parabola shaped orbit (this would be an impossible orbit).

Astronomical Units:
  - One astronomical unit is 1.495979e+8 kilometre.

VALID VALUES
Star A:
  - Mass should be less than 0.6 solar masses.
  - Mass should not exceed 1.4 solar masses.

Star B:
  - Mass should not be less than 0.08 solar masses (the minimum for it to be considered a star).
  - Mass should not exceed the mass of Star A

Average separation:
  - The average separation should not be less than 0.15 astronomical units and should not exceed 6
    astronomical units.
  - Lower values within this range are reccomended

Eccentricity:
  - Eccentricity should not be les than 0.4.
  - Eccentricity should not exceed 0.7.
  - Lower values within this range are reccomended
  - Without external forces, eccentricity should be the same for both stars.
""")

system_type = input("Star system type [<NORMAL>/P/S]: ").lower()

if system_type == "p":
  # Get required data
  mass_a       = float(input("Mass A (primary star, solar masses)   : "))
  mass_b       = float(input("Mass B (secondary star, solar masses) : "))
  average_sep  = float(input("Average separation (astronical units) : "))
  eccentric_a  = float(input("Eccentricity A                        : "))
  eccentric_b  = float(input("Eccentricity B                        : "))
  print()

  # Check for invalid values
  if mass_a < 0.6 or mass_a > 1.4:
    print("Mass of star A is invalid!")
    print()

  if mass_b < 0.08:
    print("Mass of star B is invalid!")
    print()

  if mass_b > mass_a:
    sys.exit("Star B is your primary star, please swap the values for star A and B!")

  if average_sep < 0.15 or average_sep > 6:
    print("Average separation is invalid!")
    print()

  # Calculate luminosity
  luminosity_a = pow(mass_a, 4)
  print(f"Star A has a luminosity of {luminosity_a}.")
  luminosity_b = pow(mass_b, 4)
  print(f"Star B has a luminosity of {luminosity_b}.")
  print()

  # Calculate diameter
  diameter_a = pow(mass_a, 0.74)
  print(f"Star A has a diameter of {diameter_a}.")
  diameter_b = pow(mass_b, 0.74)
  print(f"Star B has a diameter of {diameter_b}.")
  print()

  # Calculate temperature
  temp_a = pow(mass_a, 0.505)
  print(f"Star A has a surface temperature of {temp_a}.")
  temp_b = pow(mass_b, 0.505)
  print(f"Star B has a surface temperature of {temp_b}.")
  print()

  # Calculate lifetime
  lifetime_a = pow(mass_a, -2.5)
  print(f"Star A has a lifetime of {lifetime_a}.")
  lifetime_b = pow(mass_b, -2.5)
  print(f"Star B has a lifetime of {lifetime_b}.")
  print()

  # Calculate distance from the barrycentre
  barry_dist_a = average_sep * (mass_b / (mass_a + mass_b))
  barry_dist_b = average_sep - barry_dist_a
  print(f"Star A is {barry_dist_a} astronomical units from the barrycentre")
  print(f"Star B is {barry_dist_b} astronomical units from the barrycentre")
  print()

  # Calculate maximum and minimum separation
  max_sep_a = barry_dist_a * (1 + eccentric_a)
  print(f"Maximum separation for star A is {max_sep_a} astronomical units.")
  max_sep_b = barry_dist_b * (1 + eccentric_b)
  print(f"Maximum separation for star B is {max_sep_b} astronomical units.")
  max_sep_ab = max_sep_a + max_sep_b
  print(f"Total maximum separation is {max_sep_ab} astronomical units.")
  print()

  min_sep_a = barry_dist_a * (1 - eccentric_a)
  print(f"Minimum separation for star A is {min_sep_a} astronomical units.")
  min_sep_b = barry_dist_b * (1 - eccentric_b)
  print(f"Minimum separation for star B is {min_sep_b} astronomical units.")
  min_sep_ab = min_sep_a + min_sep_b
  print(f"Total minimum separation is {min_sep_ab} astronomical units.")
  print()

  # Check if stars would merge
  if min_sep_ab < 0.1:
    sys.exit("Overall minimum separation is lower than 0.1 astronimcal units, your stars will merge!")

  # Calculate planet boundaries
  sys_inner_bound = 0.1 * (mass_a + mass_b)
  print(f"Your inner planet boundary is {sys_inner_bound} astronomical units.")
  sys_outer_bound = 40 * (mass_a + mass_b)
  print(f"Your outer planet boundary is {sys_outer_bound} astronomical units.")
  print()

  # Calculate frost line
  frost_line = 4.8 * (math.sqrt(luminosity_a + luminosity_b))
  print(f"Your frost line is at {frost_line} astronomical units.")
  print()

  # Calculate habitable zone boundaries
  habitable_zone = math.sqrt(luminosity_a + luminosity_b)
  hab_inner_bound = 0.95 * habitable_zone
  print(f"Your inner habitable zone boundary is {hab_inner_bound} astronomical units.")
  hab_outer_bound = 1.37 * habitable_zone
  print(f"Your outer habitable zone boundary is {hab_outer_bound} astronomical units.")
  print()

  # Calculate forbidden zone boundaries
  frb_inner_bound = min_sep_ab / 3
  print(f"Your inner forbidden zone boundary is {frb_inner_bound} astronomical units.")
  frb_outer_bound = max_sep_ab * 3
  print(f"Your outer forbidden zone boundary is {frb_outer_bound} astronomical units.")
  print()

  # Calculate habitable planet orbit
  hab_orbit = 4 * max_sep_ab
  print(f"Your habitable planet(s) should orbit at least {hab_orbit} astronomical units from the stars.")
