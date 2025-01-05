import time, sys
indent = 0 #how many spaces to indent
indentIncreasing = True #increasing or decreasing

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.04) # Pause for 1/10th of a second

        if indentIncreasing:

            indent = indent+1
            if indent == 20:
                #change direction
                indentIncreasing = False

        else:
            #Decrease number of spaces
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
