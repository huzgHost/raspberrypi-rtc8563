#include <stdio.h>
#include <stdlib.h>
#include <linux/rtc.h> // rtc_time, RCT_RD_TIME
#include <sys/ioctl.h>
//#include <sys/time.h>
#include <sys/types.h>
#include <fcntl.h>
#include <errno.h>
#include <time.h> // time, gmtime, localtime

int main(void){
	int i, fd, retval, irqcount = 0;
	struct rtc_time rtc_tm;
	time_t timep;
	struct tm *p;

	fd = open("/dev/rtc", O_RDONLY);

	if(-1 == fd){
		perror("/dev/rtc");
		exit(errno);
	}

	retval = ioctl(fd, RTC_RD_TIME, &rtc_tm);
	if(-1 == retval) {
		perror("ioctl");
		exit(errno);
	}
	close(fd);
	
	fprintf(stderr, "Current RTC date/time is %d-%d-%d, %02d:%02d:%02d. \n", rtc_tm.tm_mday, rtc_tm.tm_mon + 1, rtc_tm.tm_year + 1900, rtc_tm.tm_hour, rtc_tm.tm_min, rtc_tm.tm_sec);

	time(&timep);  
	p = gmtime(&timep);
	fprintf(stderr, "OS date/time(UTC): %d/%d/%d %02d:%02d:%02d\n",p->tm_mday, p->tm_mon + 1, p->tm_year + 1900, p->tm_hour, p->tm_min, p->tm_sec);  
          
    p = localtime(&timep);  
    fprintf(stderr, "OS date/time(Local): %d/%d/%d %02d:%02d:%02d\n",  p->tm_mday, p->tm_mon + 1, p->tm_year + 1900, p->tm_hour, p->tm_min, p->tm_sec);  

	return 0;
}
