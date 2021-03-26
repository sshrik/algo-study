/* LCD */
#include<stdio.h>

long long int getLCD(long long int a, long long int b); 

int main()  {
    long long int a, b;
    
    scanf(" %lld %lld", &a, &b);
	getLCD(a, b);

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
    
    temp = b / B;
   
	printf("%lld\n%lld", B, a * temp);
 
    return a * temp;
}
