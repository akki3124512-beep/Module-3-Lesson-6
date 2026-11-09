import time
import random

def randomTimeGenerator(startTime, endTime):
    print("The inbetween date of", startTime, " and ", endTime, "is: ")
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startDate = time.mktime(time.strptime(startTime, dateFormat))
    endDate = time.mktime(time.strptime(endTime, dateFormat))
    randomTime = startDate + randomGenerator * (endDate - startDate)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return (randomDate)

print("Random date = ", randomTimeGenerator("1/1/2016", "12/5/2026"))