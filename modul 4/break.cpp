#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i % 5 == 0) {
            cout << "Angka pertama yang merupakan kelipatan 5 adalah: " << i << endl;
            break;
        }
        cout << "Cek angka: " << i << endl;
    }

    cout << "Perulangan selesai." << endl;
    return 0;
}
