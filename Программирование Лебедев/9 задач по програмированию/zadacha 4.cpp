#include <iostream>
#include <iomanip>
#include <locale>
using namespace std;
int main(void) {
    setlocale(LC_ALL, "RU");
    cout << "������� ����� ������� � �������� �� ���: ";
    double summ, per;
    cin >> summ >> per;
    cout << endl;

    cout << "������� ������� �� ���: ";
    double profit;
    cin >> profit;

    if (cin) {
        if (per / 100 * summ >= profit) {
            cout << "�������� ������ ���������� ";
        }
        else {
            int year = 0;
            int final = 0;
            while (final < summ) {
                final += profit;
                summ += summ * per / 100;
                ++year;
                if (year >= 100) {
                    cout << "�������� ������ ����������";
                    return 0;
                }
            }

            cout << "�� �������� ������ �� " << year << " ���.";
        }
    }
    else {
        cout << endl << endl << "������� ������������ ��������";
    }
    return 0;
}
