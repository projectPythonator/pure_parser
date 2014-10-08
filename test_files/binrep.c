#include <stdio.h>

#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)

void recursedigit(int n) {
    int on;
    if (0 == n) {
	return;
    }
    on = 0;
    if (0 != (n-((n/2)*2))) {
        on = 1;
    }
    recursedigit(n/2);
    if (0 == on) {
	printf("0");
    }
    if (1 == on) {
	printf("1");
    }
}

int main() {
    int a;
    a = 0;
    while (0 >= a) {
	printf("Give me a number: ");
	read(a);
	
	if (0 >= a) {
	    printf("I need a positive integer.\n");
	}
    }
    printf("The binary representation of: ");
    write(a);
    printf("is: ");
    recursedigit(a);
    printf("\n\n");
}


