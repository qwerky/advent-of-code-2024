def safe(report):
    # Look at the first two to decide which direction
    this = int(report[0])
    next = int(report[1])
    increase = True
    if (next < this):
        increase = False

    # Iterate
    last = -1
    for num in report:
        this = int(num)

        if last == -1:
            last = this
            continue

        if (last == this):
            print(str(report) + " Duplicate at " + str(last) + " and " + str(this))
            return False

        # Check if gradual
        if abs(this - last) > 3:
            print(str(report) + " Not gradual at " + str(last) + " and " + str(this))
            return False
        
        # Check direction
        if increase:
            if this < last:
                print(str(report) + " Change in direction at " + str(last) + " " + str(this))
                return False
        else:
            if this > last:
                print(str(report) + " Change in direction at " + str(last) + " " + str(this))
                return False
        
        last = this
            
    return True