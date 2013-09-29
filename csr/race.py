from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
sys.path.append('C:\\csr')
import z4

print('connect device')
device = MonkeyRunner.waitForConnection()
print('connected')
z4.tuner(device)
