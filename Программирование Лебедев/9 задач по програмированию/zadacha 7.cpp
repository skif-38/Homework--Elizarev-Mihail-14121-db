#include <iostream>
#include <iomanip>
#include <locale>
using namespace std;
int main(void) {
    setlocale(LC_ALL, "RU");
    double e;
    cout << "������� ���������� �������: ";
    cin >> e;

    if (cin && e < 1) {
        double res = 0;
        for (double x = 0.5; 1 - res >= e; x /= 2) {
            res = sin(x) / x;
            cout << fixed << "x: " << x << ", ���������: " << res << ", �������: " << 1 - res << endl;
        }
    }
    else cout << "���������� ������� ������ ���� ������, ������� ������ 1";
    return 0;
}