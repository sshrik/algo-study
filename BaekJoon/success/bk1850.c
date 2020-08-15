/* Get 1111...`s LCD */
#include<stdio.h>

long long int getLCD(long long int a, long long int b);

int main()	{
	long long int x, y, i, temp;

	scanf(" %lld %lld", &x, &y);
	
	temp = getLCD(x, y);

	for(i = 0; i < temp; i++) {
		printf("1");
	}
	
	return 0;
}

long long int getLCD(long long int a, long long int b)    {   
    long long int A = a;
    long long int B = b;
    long long int temp;

    if(B > A) {
        temp = A;
        A = B;
        B = temp;
    }   

    while(A % B != 0) {
        A = A % B;

        if(B > A) {
            temp = A;
            A = B;
            B = temp;
        }   
    }   
    
    return B;
}
