#include <stdio.h>

// This test should result in a grammar error due to the for loop!

int main() 
{
  int i;
  for(i = 0; i < 10; i++){
    printf("hello\n");
  }
  return 0;
}
