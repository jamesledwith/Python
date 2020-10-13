#long jump competition, the jumper jumps 6 times, the avg, max and minimum is recorded

maximum_jump = 0
total = 0
    
for i in range(6):
    
    distance = float(input("Enter your distance: "))
    
    #first distance entered is the minimum
    minimum_jump = distance
    
    # check for the maximum jump
    if distance > maximum_jump:
        maximum_jump = distance
    
    # check for the minimum jump
    if distance < minimum_jump:
        minimum_jump = distance
    
    #calculate the average
    total += distance
    average = total/6
    
#print results
print(f"The total distance was {total}, the average was {average}, maximum was {maximum_jump}, and the minumum was {minimum_jump}")
    