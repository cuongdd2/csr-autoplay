from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def r0(device):
	print 'depa'
	device.touch(1150, 450, MonkeyDevice.DOWN)
	MonkeyRunner.sleep(3.6)
	print 'release depa'
	device.touch(950, 600, MonkeyDevice.UP)
	MonkeyRunner.sleep(1.7)
	print 'gear 2'
	device.touch(950, 600, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1.2)
	print 'gear 3'
	device.touch(950, 600, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.1)
	print 'nitro'
	device.touch(100, 500, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.97)
	print 'gear 4'
	device.touch(950, 600, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1.4)
	print 'gear 5'
	device.touch(950, 600, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1.95)
	print 'gear 6'
	device.touch(950, 600, MonkeyDevice.DOWN_AND_UP)
	