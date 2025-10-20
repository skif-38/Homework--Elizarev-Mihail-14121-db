#include <iostream>
#include <iomanip>
#include <locale>
using namespace std;
int main(void) {
    setlocale(LC_ALL, "RU");
    double a, b;
    cout << "¬ведите a, b дл€ определени€ функции: ";
    cin >> a >> b;

    if (a != 0 && b != 0 && cin && a < 100 && b < 100) {
        for (double y = b; y >= -b; --y) {
            for (double x = -a; x <= a; ++x) {
                if (x * x / a / a + y * y / b / b <= 1.0) {
                    cout << setfill(' ') << "(" << setw(3) << x << "," << setw(3) << y << ")";
                }
                else {
                    cout << "         ";
                }
            }
            cout << endl;
        }
    }
    else {
        cout << "a и b должны быть числами, которые больше 0 и меньше 100";
    }
    return 0;
}