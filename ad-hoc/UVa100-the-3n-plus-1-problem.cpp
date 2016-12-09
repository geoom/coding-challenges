#include <iostream>
#include <stdio.h>

using namespace std;

int cycle_length(int x){
	int length = 1;
	while( x!=1 ){
		if ( x%2 == 0 ){
			x = x/2;
		}else{
			x = 3*x + 1;
		}
		length++;
	}
	return length;
}

int max_cycle_length(int a, int b){
	if(a>b){
		int temp = a;
		a = b;
		b = temp;
	}

	int max_length = 0;

	while(a<=b){
		int current_cycle_length = cycle_length(a);
		if (current_cycle_length > max_length){
			max_length = current_cycle_length;
		}
	}

	return max_length;
}

int main(){
	int a, b;

	while (scanf("%d %d", &a, &b) != EOF) {
		printf("%d %d %d\n", a, b, maxCycleSizeBetween(a, b));
    }
	
	return 0;
}

