#include <iostream>
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
        for (double x = 0.5; 1 - res >= e; x /= 2) {
            res = sin(x) / x;
            cout << fixed << "x: " << x << ", Результат: " << res << ", Разница: " << 1 - res << endl;
        }
    }
    else cout << "Допустимая разница должна быть числом, которое меньше 1";
    return 0;
}