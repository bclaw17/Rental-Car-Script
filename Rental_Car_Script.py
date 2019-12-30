import sys
'''##################################################################
################ THE RENTAL CAR SCRIPT DRAFT 1 #################################
'''##################################################################

#RENTAL TYPE? - Assigning string to variable
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

if rentalCode == 'D' or rentalCode == 'B':
  rentalPeriod = int(input("Number of Days Rented:\n"))### Assigning integer to variable
elif rentalCode == 'W':
  rentalPeriod = int(input("Number of Weeks Rented:\n"))
#CHARGE - BASE - Assigning float to variable
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00
#CHARGE - Base Charge * Period - Integer * Float - Results in float
if rentalCode == 'B':
  baseCharge = rentalPeriod * budget_charge
elif rentalCode == 'D':
    baseCharge = rentalPeriod * daily_charge
else:
    baseCharge = rentalPeriod * weekly_charge
#MILES DRIVEN START & END INPUT
odoStart = int(input("Starting Odometer Reading:\n"))
odoEnd = int(input("Ending Odometer Reading:\n"))
totalMiles = odoEnd - odoStart
#HEAD OF RENTAL SUMMARY
print("Rental Summary")
#TOTAL MILES CALCULATION BASED ON AVERAGE MILES DRIVEN AND RENTAL TYPE
if rentalCode == 'B':
  mileCharge = totalMiles * 0.25 ###Integer * float

if rentalCode == 'D':
  averageDayMiles = totalMiles / rentalPeriod
  if averageDayMiles <= 100:
    mileCharge = 0
    extraMiles = 0
  elif averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
    mileCharge = extraMiles * 0.25

if rentalCode == 'W':
    averageWeekMiles = totalMiles / rentalPeriod
    if averageWeekMiles <= 900:
      mileCharge = 0
      extraMiles = 0
    elif averageWeekMiles > 900:
      mileCharge = rentalPeriod * 100

## CUSTOMER GIVEN PRINTOUT OF PERTINENT INFORMATION 
print("Rental Code:" + " " + " " + " " + " " + " " + " " + " " + " " + str(rentalCode))
print("Rental Period:" + " " + " " + " " + " " + " " + " " + " " + " " + str(rentalPeriod))
print("Starting Odometer:" + " " + " " + str(odoStart))
print("Ending Odometer:"  + " " + " " + " " + " " + str(odoEnd))
print("Miles Driven:"  + " " + " " + " " + " " + " " + " " + " " + str(totalMiles))
amtDue = baseCharge + mileCharge
print("Amount Due:" + " " + " " + " " + " " + " " + " " + " " + " " + " " '$%.2f' % amtDue)
