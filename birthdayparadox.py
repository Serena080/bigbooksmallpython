
import datetime, random



def getBirthdays(numberOfBirthdays):
     """Returns a list of number random date objects for birthdays."""
birthdays = []


for i in range(numberOfBirthdays):
        #The year is not relevant for the simulations
        
        # Get a random day of the year
        dayOfYear = random.randint(1, 365)
        birthday = datetime.date.fromordinal(dayOfYear)
        birthdays.append(birthday)
     return birthdays
