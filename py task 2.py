print("Swallow Speed Analysis: Version 1.0")
def datavalid_readings(reading):
    if (reading.capitalize()[0] != ("U" or "E")) or any(char.isalpha() for char in reading[1:]):
        return False
    else:
        return True

#converting miles into km
def convert_miles_into_km(z):
    return z * 1.60934

setofData = []

while True:
    reading = input("Enter the next reading : ")
    if reading == "":
        break
    if datavalid_readings(reading) == False:
        print("Invalid Input !")
        continue
    print("Reading saved.")
    setofData.append(float(reading[1:]) if reading[0] == "U" else float(reading[1:])/1.60934)

if setofData == []:
    print("No readings \n Nothing to do.")
else:
    print(f"{len(setofData)} Readings.")
    maximumReadingMiles = max(setofData)
    maximumReadingKm = convert_miles_into_km(maximumReadingMiles)
    minimumReadingMiles = min(setofData)
    minimumReadingKm = convert_miles_into_km(minimumReadingMiles)
    avReadingMiles = sum(setofData)/len(setofData)
    avReadingKm = convert_miles_into_km(avReadingMiles)

    print("Results Summary")
    print(f"Max : {maximumReadingMiles} mph, {maximumReadingKm} kph")
    print(f"Min : {minimumReadingMiles} mph, {minimumReadingKm} kph")
    print(f"Avg : {avReadingMiles} mph, {avReadingKm} kph")





    
