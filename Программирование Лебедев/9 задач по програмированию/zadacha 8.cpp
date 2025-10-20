#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>
#include <iomanip>
#include <locale>
using namespace std;
int main(void) {
    setlocale(LC_ALL, "RU");
    double e;
    cout << "Введите допустимую разницу: ";
    cin >> e;

    if (cin && e < 1) {
        double res = 0;
        int n1;
        for (double n = 1; M_E - res >= e; n++) {
            res = pow(1 + 1 / n, n);
            n1 = n;
        }
        cout << setprecision(20) << fixed << "n: " << n1 << ", resualt: " << res << ", difference: " << M_E - res << endl;
    }
    else cout << "Допустимая разница должна быть меньше 1";
    return 0;
}