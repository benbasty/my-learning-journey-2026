import time, sys
try:
    while True:
        #draw lines with increasing lenght
        # i variable is set to 1, then 2, then 3,
        # and so on, up to but not including 9
        for i in range(1, 9):
            # print() call replicates the '-' strings by 1 * 1 (that is, 1),
            # then 2 * 2 (that is, 4), then 3 * 3 (that is, 9), and so on.
            # 1, 4, 9, 16, 25, 36, 49, and then 64 dashes long...
            print('-' * (i * i))
            time.sleep(0.1)

        # Draw lines with decreasing length:
        # i starts at 7 and then decrease down to 1, not including 1:
        for i in range(7, 1, -1):
            print('-' * (i * i))
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()