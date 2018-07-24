/* Calculate a^k % div at log N time. */
#include<stdio.h>

long long int powerD(long long int a, long long int k, long long int div);

int main()	{
	long long int a, k, div;
	
	scanf(" %lld %lld %lld", &a, &k, &div);
	printf("%lld", powerD(a, k, div));

}

long long int powerD(long long int a, long long int k, long long int div)	{
	long long int temp = 0;
	long long int result;

	printf("powerD(%lld, %lld, %lld) was called.\n", a, k, div);
	if(k == 2) {
		temp = (a % div) * (a % div);
		printf("result was %lld.\n", temp % div);
		return temp % div;
	}
	else if(k == 1)	{
		printf("result was %lld.\n", a % div);
		return a % div;
	}
	else if(k % 2 == 0)	{
		temp = powerD(a, (int)(k / 2), div);
		temp = temp * temp;
		result = temp % div;
		printf("result was %lld.\n", result);
		return result;
	}
	else {
		temp = powerD(a, (int)((k - 1) / 2), div);
		temp = temp * temp * (a % div);
		result = temp % div;
		printf("result was %lld.\n", result);
		return result;
	}
}
