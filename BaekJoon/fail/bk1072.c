#include<stdio.h>

long long int getA(long long int x, long long int y, long long int z); 

int main()  {
    long long int x, y, z, a;
    
	while(scanf("%lld %lld",&x, &y)!=EOF){
		z = (y * 100) / x;
    	
    	if(z == 99 || z == 100) {
    	    printf("-1");
    	}   
    	else {
    	    a = getA(x, y, z); 
    	    printf("%lld", a); 
			printf(" %lld %lld %lld\n", x, y, z);
    	}
	}
    return 0;
}

long long int getA(long long int x, long long int y, long long int z) {
    return ((z + 1) * x - 100 * y) / (100 - z - 1) + 1;   
}
