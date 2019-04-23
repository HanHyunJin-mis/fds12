#include <stdio.h>

void change_value(int a, int vlaue) {
	a = value;
	printf("%d in change_value \n", a);
}

int main(void) {
	int a = 10;
	change_value(a, 30);
	printf("%d in main \n", a);
    return 0;
}

// 매개 변수는 오른쪽에서 왼쪽으로 쌓이고 위에서 밑으로 쌓인다.
void change_value(int x, int val) {
	x = val;
	printf("x : %d in change_value \n", x);
}

int main(void) {
	int x = 10;
	change_value(x, 20);
	printf("x : %d in main \n", x);
}

// call by value : 값을 단순하게 복사함, 인자를 값으로 전달했기 때문에
