from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
		
def change_date(device, n):
	print 'change date',n
	device.touch(850, 770, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1.5)
	device.touch(850, 400, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.touch(200, 250, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.touch(340, 475, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.touch(640, 620, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	device.touch(850, 770, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	device.touch(850, 400, MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1.5)
	print 'finish change'