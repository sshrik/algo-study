/* Sorting number with large number. */
#include<cstdio>
#include<algorithm>

using namespace std;

int main()  {
    int n, i;
	int * arr;

    scanf(" %d", &n);
	
	// Make dynamic memory
	arr = new int[n];

    for(i = 0; i < n; i++)  {
        scanf(" %d", &arr[i]);
    }   

    sort(arr, &arr[n]);

    for(i = 0; i < n; i++) {
        printf("%d\n", arr[i]);
    }   

	// delete dynamic memor.
	delete [] arr;
	
    return 0;
}

