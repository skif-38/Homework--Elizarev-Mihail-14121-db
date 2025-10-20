#include <iostream>
#include <iomanip>
#include <locale>
using namespace std;
int main(void) {
    setlocale(LC_ALL, "RU");
    double k;
    cout << "Введите киллометраж: ";
    cin >> k;

    cout << setfill(' ') << setw(6) << "Милли" << "   " << setw(5) << "Киллометры" << endl;
    double cons = 1.60934;
    double k_m[1000];
    double m_m[1000];

    int count = 0;
    for (double n = 1; n <= k; ++n) {
        k_m[count] = n;
        m_m[count] = n / cons;
        ++count;
    }

    int max_m = k / cons;
    for (double n = 1; n <= max_m; ++n) {
        k_m[count] = n * cons;
        m_m[count] = n;
        ++count;
    }

    for (int i = 0; i < count - 1; ++i) {
        for (int j = 0; j < count - i - 1; ++j) {
            if (m_m[j] > m_m[j + 1]) {
                swap(m_m[j], m_m[j + 1]);
                swap(k_m[j], k_m[j + 1]);
            }
        }
    }

    for (int n = 0; n < count; ++n) {
        cout << setprecision(4) << setfill(' ') << setw(6) << m_m[n] << "    " << setw(6) << k_m[n] << endl;
    }

    return 0;
}
