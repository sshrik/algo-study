/* Count Croatia Arphabet. */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define WORD_MAX 105

int main()	{
	char str[WORD_MAX];
	int i, len, indx = 0;
	int used[34], ans = 0;
	/* used[26] : c=	used[27] : c-	used[28] : dz=
	 * used[29] : d-	used[30] : lj	used[31] : nj
	 * used[32] : s=	used[33] : z=	*/

	memset(used, 0x00, sizeof(int) * 34);
	scanf(" %s", str);
	len = strlen(str);

	while(indx < len)	{
		switch(str[indx])	{
			case 'c':
				if(indx + 1 < len) {
					switch(str[indx+1])	{
						case '=':	used[26]++;	indx = indx + 2;	break;
						case '-':	used[27]++;	indx = indx + 2;	break;
						default:	used[str[indx] - 'a']++;	indx++;	break;
					}	
				}
				else {
					used[str[indx] - 'a']++;
					indx++;
				}
				break;
			case 'd':
				if(indx + 1 < len) {
					if(indx + 2 < len)	{
						if(str[indx+1] == 'z' && str[indx+2] == '=')	{
							used[28]++;
							indx = indx + 3;
						}
						else if(str[indx+1] == '-')	{
							used[29]++;
							indx = indx + 2;
						}
						else {
							used[str[indx] - 'a']++;
							indx++;
						}
					}
					else {
						if(str[indx+1] == '-')	{
							used[29]++;
							indx = indx + 2;
						}
						else {
							used[str[indx] - 'a']++;
							indx++;
						}
					}
				}
				else {
					used[str[indx] - 'a']++;
					indx++;
				}
				break;
			case 'l':
				if(indx + 1 < len) {
					if(str[indx+1] == 'j')	{
						used[30]++;
						indx = indx + 2;
					}
					else {
						used[str[indx] - 'a']++;
						indx++;
					}
				}
				else {
					used[str[indx] - 'a']++;
					indx++;
				}
				break;
			case 'n':
				if(indx + 1 < len) {
					if(str[indx+1] == 'j')	{
						used[31]++;
						indx = indx + 2;
					}
					else {
						used[str[indx] - 'a']++;
						indx++;
					}
				}
				else {
					used[str[indx] - 'a']++;
					indx++;
				}
				break;
			case 's':
				if(indx + 1 < len) {
					if(str[indx+1] == '=')	{
						used[32]++;
						indx = indx + 2;
					}
					else {
						used[str[indx] - 'a']++;
						indx++;
					}
				}
				else {
					used[str[indx] - 'a']++;
					indx++;
				}
				break;
			case 'z':
				if(indx + 1 < len) {
					if(str[indx+1] == '=')	{
						used[33]++;
						indx = indx + 2;
					}
					else {
						used[str[indx] - 'a']++;
						indx++;
					}
				}
				else {
					used[str[indx] - 'a']++;
					indx++;
				}
				break;
			default:
				used[str[indx] - 'a']++;
				indx++;
				break;
		}
	}
	for(i = 0; i < 34; i++)	ans += used[i]; 
	printf("%d\n", ans);

	return 0;
}
