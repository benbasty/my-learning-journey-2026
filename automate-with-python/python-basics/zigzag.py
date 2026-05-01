import sys, time #import time and sys modules
indent = 0 #how many space to indent
indent_increasing = True #whether the indentation increases on not
try:
    while True: #the main program look
        print(' ' * indent, end= '') #print the correct amount of spaces of indentation
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second.

        if indent_increasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indent_increasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()

