#include <stdio.h>

#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)

int N;

int Calculate(int cnt) {
  if (cnt > 0) {return Calculate(cnt - 1) + 42;}
  return 0;
}

int main (void) {
  printf("Magic positive number is ");
  read(N);
  printf("The meaning of Life is ");
  write(Calculate(N) / N);
}


