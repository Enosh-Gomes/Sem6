#include <iostream>
using namespace std;


string binarySum(string a, string b){
    string sum(4,'0');
    int carry=0;
    for(int i=3;i>=0;i--){
        int bit=a[i]-'0'+b[i]-'0'+carry;
        sum[i]=(bit%2)+'0'; ///its sum[i] not sum
        carry=bit/2; //its bit here not sum
    }
    while(carry){
        int bit=sum[3]-'0'+carry;
        sum[3]=(bit%2)+'0';
        carry=bit/2; //its bit here not sum
    }
    return sum;
}


string onesComplement(string s){
    for(char &c:s){  //dont forget this reference &sign
        c=(c=='0')?'1':'0';
    }
    return s;
}


int main() {
    int choice;
    string a, b, checksum;

    while (true) {
        cout << "\n1. Transmitter\n2. Receiver\n3. Exit\nChoice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter 1st 4-bit binary number: "; cin >> a;
            cout << "Enter 2nd 4-bit binary number: "; cin >> b;
            string sum = binarySum(a, b);
            checksum = onesComplement(sum);
            cout << "Checksum: " << checksum << "\n";
            cout << "Data sent: " << a << " " << b << " " << checksum << "\n";
        }
        else if (choice == 2) {
            cout << "Enter 1st 4-bit binary number: "; cin >> a;
            cout << "Enter 2nd 4-bit binary number: "; cin >> b;
            cout << "Enter checksum: "; cin >> checksum;
            string sum = binarySum(binarySum(a, b), checksum);
            if (sum == "1111") cout << " No Error\n";
            else cout << " Error Detected\n";
        }
        else if (choice == 3) break;
        else cout << "Invalid choice!\n";
    }

    return 0;
}