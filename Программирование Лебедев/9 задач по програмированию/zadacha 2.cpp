#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>
#include <iomanip>
#include <locale>

using namespace std;

int main(void) {
    double er = 0.00001;

    cout << "  X    |  sin2(x)  |   tan(x)   | 1/x*sin(x) ";
    for (double x = 0; x <= 10 * M_PI; x += M_PI) {
        cout << endl << fixed << setprecision(3) << setfill(' ') << setw(6) << x << " | ";
        if (sin(x + M_PI) * sin(x + M_PI) - sin(x) * sin(x) <= er) cout << scientific << sin(x) * sin(x) << " | ";
        if (sin(x + M_PI) * sin(x + M_PI) - sin(x) * sin(x) > er) cout << "   " << " | ";
        if (tan(x + M_PI) - tan(x) <= er) cout << setfill(' ') << setw(10) << tan(x) << " | ";
        if (tan(x + M_PI) - tan(x) > er) cout << setfill(' ') << setw(10) << " " << " | ";
        if (1 / x * sin(x + M_PI) - 1 / x * sin(x) <= er) cout << setw(10) << scientific << 1 / x * sin(x);
        if (1 / x * sin(x + M_PI) - 1 / x * sin(x) > er) cout << setw(10) << "  ";
    }
    for (double x = 0; x <= 2 * M_PI; x += M_PI / 10.0) {
        if (!(sin(x) * sin(x) < 10 && sin(x) * sin(x) > -10)) cout << fixed << setprecision(8) << x << "=sin2(x)";
        if ((sin(x) * sin(x) < 10 && sin(x) * sin(x) > -10))
            if (!(tan(x) < 10 && tan(x) > -10)) cout << fixed << setprecision(8) << x << "=tan(x) ";
        if ((tan(x) < 10 && tan(x) > -10))
            if (!(1 / x * sin(x) < 10 && 1 / x * sin(x) > -10)) cout << fixed << setprecision(8) << x << "=1/x*sin(x)";
        if ((1 / x * sin(x) < 10 && 1 / x * sin(x) > -10)) cout;
    }

    return 0;
}