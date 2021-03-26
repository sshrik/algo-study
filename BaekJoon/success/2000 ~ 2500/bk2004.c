#include<stdio.h>

long long int getFac5(long long int i);
long long int getFac2(long long int i);

int main()	{
	long long int n, m;
	long long int a2, a5, b2, b5, c2, c5;
	long long int r2, r5;
	
	scanf(" %lld %lld", &n, &m);
	
	a2 = getFac2(n);
	a5 = getFac5(n);
	b2 = getFac2(m);
	b5 = getFac5(m);
	c2 = getFac2(n - m);
	c5 = getFac5(n - m);

	r2 = a2 - b2 - c2;
	r5 = a5 - b5 - c5;

	if(r2 > r5) printf("%lld", r5);
	else printf("%lld", r2);
	
	return 0;
}

long long int getFac5(long long int i)  {
    long long int mul5 = 5;
    long long int result = 0;
    while(mul5 <= i)    {   
        result += (long long int)((i - (i % mul5)) / mul5);
        mul5 *= 5;
    }   
    return result;
}

long long int getFac2(long long int i)  {
    long long int mul2 = 2;
    long long int result = 0;
    while(mul2 <= i)    {   
        result += (long long int)((i - (i % mul2)) / mul2);
        mul2 *= 2;
    }   
    return result;
}

