# raspberrypi-rtc8563
I2C PCF8563时钟，支持离线时间。

一，插入8563,通过i2c-dectect -y 1 ,看到我们的设备挂在0x51上。此时还是不能工作的。 然后我们查看/boot/overlay/README文件

查看/boot/overlay/README文件
Name:   i2c-rtc
Info:   Adds support for a number of I2C Real Time Clock devices
Load:   dtoverlay=i2c-rtc,<param>=<val>
Params: abx80x                  Select one of the ABx80x family:
                                  AB0801, AB0803, AB0804, AB0805,
                                  AB1801, AB1803, AB1804, AB1805
 
 		ds1307                  Select the DS1307 device
 
        ds1339                  Select the DS1339 device

        ds3231                  Select the DS3231 device

        mcp7940x                Select the MCP7940x device

        mcp7941x                Select the MCP7941x device

        pcf2127                 Select the PCF2127 device

        pcf8523                 Select the PCF8523 device

        pcf8563                 Select the PCF8563 device

        trickle-diode-type      Diode type for trickle charge - "standard" or
                                "schottky" (ABx80x only)

        trickle-resistor-ohms   Resistor value for trickle charge (DS1339,
                                ABx80x)

        wakeup-source           Specify that the RTC can be used as a wakeup
                                source                       
通过README文件，我们知道可以在/boot/config.txt添加"dtoverlay=i2c-rtc,fcp8563"，

重启，再通过i2c-dectec -y 1,可以看到设备变成UU了，如下：
pi@raspberrypi:/boot/overlays $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- UU -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                         

这时候，我们的设备已经开始工作了，
----------------------------------------------------------------------------
查看开机日志,可知设备是正常注册上了。
pi@raspberrypi:/boot/overlays $ dmesg | grep rtc
[    3.916341] rtc-pcf8563 1-0051: low voltage detected, date/time is not reliable.
[    3.916660] rtc-pcf8563 1-0051: rtc core: registered rtc-pcf8563 as rtc0

----------------------------------------------------------------------------
读取时间
pi@raspberrypi:/boot/overlays $ sudo hwclock -r
2017年08月23日 星期三 10时44分11秒  -0.799940 seconds
---------------------------------------------------------------------------
