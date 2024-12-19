length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room in feet? "))
#square root metric for final values
metricl = length * 0.09290304


print(f"You entered the dimensions {length} feet by {width} feet.")
print("The are is")
print(f"{length * width} square feet")
print(f"{length * width * 0.09290304} square meters")