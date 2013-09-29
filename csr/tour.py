from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
sys.path.append('E:\\work\\csr-autoplay\\csr')
import z4

print('connect device')
device = MonkeyRunner.waitForConnection()
print('connected')
#device.startActivity(new Intent(android.provider.Settings.ACTION_DATE_SETTINGS))
print 'hire team'
device.touch(300, 700, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1.5)
print 'pro tuner'
device.touch(300, 600, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
print '5min'
device.touch(600, 500, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
print 'buy'
device.touch(750, 550, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
print 'blogger'
device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
print '5min'
device.touch(600, 500, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
print 'buy'
device.touch(750, 550, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1)
print 'back'
device.touch(425, 770, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(3)

for n in range(1, 1000):
	print 'select'
	if n < 5 :
		device.touch(1000, 150 + (n-1)*140, MonkeyDevice.DOWN_AND_UP)
	else :
		device.drag((50, 440), (50, 440 - (n-4)*140))
		MonkeyRunner.sleep(0.5)
		device.touch(1000, 150 + 3*140, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(4)
	print 'race'
	device.touch(1000, 600, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(6.5)
	print 'skip'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	print 'skip'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	z4.r1(device)
	print 'next'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(3)
	print 'next'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(3)
	print 'next'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(6)
	print 'next'
	device.touch(1200, 690, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(5)
	
	