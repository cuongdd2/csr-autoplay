from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
sys.path.append('C:\\csr')
import r8, util

print('connect device')
device = MonkeyRunner.waitForConnection()
print('connected')

for n in range(1000):
	if n%9 == 0:
		MonkeyRunner.sleep(1)
		util.change_date(device, n)
	MonkeyRunner.sleep(1.5)
	print 'go race'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(7)
	print 'skip'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	print 'skip'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	r8.r0(device)
	MonkeyRunner.sleep(4)
	print 'skip'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	print 'next'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(3)
	print 'level up'
	device.touch(700, 525, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	print 'skip ad'
	device.touch(425, 770, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(3)
	print 'next'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	