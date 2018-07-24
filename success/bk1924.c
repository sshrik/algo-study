/* 2007 1/1 == MON, than X/Y == ?? */
#include<stdio.h>

void printDay(int passDay);
int getMonthDay(int month);

int main()	{
	int i, x, y, passDay = 0;

	scanf(" %d %d", &x, &y);
	for(i = 1; i < x; i++) {	
		passDay += getMonthDay(i);
	}
	passDay += y;
	printDay(passDay - 1 + 7); // If 0, error occured && -1 because it start with 1.
	
	return 0;
}

void printDay(int passDay)	{
	switch(passDay % 7) {
		case 0:
			printf("MON");
			break;
		case 1:
			printf("TUE");
			break;
		case 2:
			printf("WED");
			break;
		case 3:
			printf("THU");
			break;
		case 4:
			printf("FRI");
			break;
		case 5:
			printf("SAT");
			break;
		case 6:
			printf("SUN");
			break;
		default:
			break;
	}
}

int getMonthDay(int month)	{
	switch(month)	{
		case 1:
			return 31;
			break;
		case 2:
			return 28;
			break;
		case 3:
			return 31;
			break;
		case 4:
			return 30;
			break;
		case 5:
			return 31;
			break;
		case 6:
			return 30;
			break;
		case 7:
			return 31;
			break;
		case 8:
			return 31;
			break;
		case 9:
			return 30;
			break;
		case 10:
			return 31;
			break;
		case 11:
			return 30;
			break;
		case 12:
			return 31;
			break;
		default:
			break;
	}
	return -1;
}
