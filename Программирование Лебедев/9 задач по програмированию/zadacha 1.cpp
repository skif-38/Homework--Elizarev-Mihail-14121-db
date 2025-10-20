#include <iostream>
#include <cmath>
#include <locale>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    double b = 5;
    double step = 0.1;
    double chek1 = 0;
    cout << "Проверка функции x**4:\n";
    for (double x = 0; x <= b; x += step) {
        if (abs(pow(x, 4) - pow(-x, 4)) <= 0.001) chek1 = 2;
        else if (abs(pow(x, 4) + pow(-x, 4)) <= 0.001) chek1 = 1;
    }
    if (chek1 == 2) cout << "Функция чет\n";
    else if (chek1 == 1) cout << "Функция нечёт\n";
    else if (chek1 == 0) cout << "Функция ни чёт и ни нечёт\n";


    double chek2 = 0;
    cout << "Проверка функции tg(x):\n";
    for (double x = 0; x <= b; x += step) {
        if (abs(tan(x) - tan(-x)) <= 0.001) chek2 = 2;
        else if (abs(tan(x) + tan(-x)) <= 0.001) chek2 = 1;
    }
    if (chek2 == 2) cout << "Функция чет\n";
    else if (chek2 == 1)  cout << "Функция нечёт\n";
    else if (chek2 == 0) cout << "Функция ни чет и ни нечёт\n";


    double chek3 = 0;
    cout << "Проверка функции e**x:\n";
    for (double x = 0; x <= b; x += step) {
        if (abs(exp(x) - exp(-x)) <= 0.001) chek3 = 2;
        else if (abs(exp(x) + exp(-x)) <= 0.001) chek3 = 1;
        else chek3 = 0;
    }
    if (chek3 == 2) cout << "Функция чет\n";
    else if (chek3 == 1) cout << "Функция нечёт\n";
    else if (chek3 == 0) cout << "Функция ни четная, ни нечёт\n";


    return 0;
}