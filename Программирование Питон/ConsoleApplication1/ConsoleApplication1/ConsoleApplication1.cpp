#include <iostream>
#include <fstream>
using namespace std;
int main(void)
{
	int N = 10;
	int mine = 0;
	int maxe = 0;
	int* p_arr = new int[10];
	int r_min = -50;
	int r_max = 50;
	for (int i = 0; i < N; i++) {
		*(p_arr + i) = r_min + rand() % (r_max - r_min + 1);
		cout << *(p_arr + i) << endl <<mine <<maxe;

	}
}