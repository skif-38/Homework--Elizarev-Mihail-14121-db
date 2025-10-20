#include <iostream>
#include <iomanip>
#include <locale>
using namespace std;
int main(void) {
    setlocale(LC_ALL, "RU");
    double x, m;
    cout << "¬ведите x и m for (1 + x)**m: ";
    cin >> x >> m;

    if (cin) {
        double in = 1.0;
        double out = in;

        for (int i = 0; i < m; i++) {
            in *= (m - i) / (i + 1) * x;
            out += in;
        }

        cout << "Result: " << out;
    }
    else cout << "x и m должны быть числом (m >= 0)";

    return 0;
}