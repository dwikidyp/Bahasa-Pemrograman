#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "Ketik sesuatu dan tekan Enter." << endl;
    cout << "Ketik 'exit' untuk keluar dari program." << endl;
    cout << "================================" << endl;
    
    while (true) {
        string input;
        cout << "\nMasukkan 'exit' untuk berhenti: ";
        cin >> input;
        
        if (input == "exit") {
            cout << "Program dihentikan. Terima kasih!" << endl;
            break;
        } else {
            cout << "Anda mengetik: " << input << endl;
            cout << "Silakan coba lagi atau ketik 'exit' untuk keluar." << endl;
        }
    }
    
    return 0;
}