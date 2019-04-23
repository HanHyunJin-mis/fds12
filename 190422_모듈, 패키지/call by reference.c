#include <stdio.h>

void change_value(int * x, int val) {
	*x = val;
	printf("x : %d in change_value \n", *x);
}

int main(void) {
    // 함수를 호출하면 stack frame이 쌓인다.
	int x = 10;
	change_value(&x, 20);
	printf("x : %d in main \n", x);
}