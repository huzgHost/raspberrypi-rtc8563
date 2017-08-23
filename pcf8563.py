import smbus
import time

address = 0x51;
start_ADDR = 0x02;
sec_ADDR = 0x02;
min_ADDR = 0x03;
hour_ADDR = 0x04;
day_ADDR = 0x05;
weekday_ADDR = 0x06;
month_ADDR = 0x07;
year_ADDR = 0x08;

bus = smbus.SMBus(1);

class PCF8563:
	year = 0;
	month = 0;
	weekday = 0;
	day = 0;
	hour = 0;
	minitues = 0;
	sec = 0;
	initTime = [0x30, 0x55, 0x14, 0x23, 0x4, 0x08, 0x17]
	bus = smbus.SMBus(1);

	def __init__(self):
		year = 0;
		month = 0;
		weekday = 0;
		day = 0;
		hour = 0;
		minutes = 0;
		sec = 0;
		#self.setTime();
		
		return;
	# end init

	def setTime(self):
		bus.write_i2c_block_data(address, start_ADDR, self.initTime);
	# end setTime

	def setYear(self):
		bus.write_byte_date(address, year_ADDR, 0x17);
	# end setYear

	def readYear(self):
		year = bus.read_byte_data(address, year_ADDR);
		#print 'year = 20%x' %year;
		return year;
	# end readYear

	def readMonth(self):
		month = bus.read_byte_date(address, month_ADDR);
		
		return month;
	# end readYear

	def readWeek(self):
		week = bus.read_byte_date(address, week_ADDR);
		return week;
	# end readWeek

	def readDay(self):
		day = bus.read_byte_date(address, day_ADDR);
		return day;
	# end readDay

	def readHour(self):
		day = bus.read_byte_date(address, hour_ADDR); 
		return day;
	# end readHour

	def readMin(self):
		day = bus.read_byte_date(address, min_ADDR);
		return day;
	# end readMin

	def readSec(self):
		sec = bus.read_byte_date(address, sec_ADDR);
		return sec;
	# end readSec

	def readTotalTime(self):
		t = bus.read_i2c_block_data(address, start_ADDR, 7);
		print 'year = 20%x' %(t[6]);
		t[0] &= 0x7F;
		t[1] &= 0x7F;
		t[2] &= 0x3F;
		t[3] &= 0x3F;
		t[4] &= 0x07;
		t[5] &= 0x1F;
		t[6] &= 0x7F; 
		
		print ("20%x/%x/%x %x:%x:%x   %s" %(t[6], t[5], t[3], t[2], t[1], t[0], t[4]));
		#end for
	# end readTime
		
#end class	
