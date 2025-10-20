#include <iostream>
#include <iomanip>
#include <locale>
using namespace std;
int main(void) {
    setlocale(LC_ALL, "RU");
    cout << "Введите сумму кредита и проценты за год: ";
    double summ, per;
    cin >> summ >> per;
    cout << endl;

    cout << "Введите прибыль за год: ";
    double profit;
    cin >> profit;

    if (cin) {
        if (per / 100 * summ >= profit) {
            cout << "Погасить кредит невозможно ";
        }
        else {
            int year = 0;
            int final = 0;
            while (final < summ) {
                final += profit;
                summ += summ * per / 100;
                ++year;
                if (year >= 100) {
                    cout << "Погасить кредит невозможно";
                    return 0;
                }
            }

            cout << "Вы погасите кредит за " << year << " лет.";
        }
    }
    else {
        cout << endl << endl << "Введены неправильные значения";
    }
    return 0;
}
