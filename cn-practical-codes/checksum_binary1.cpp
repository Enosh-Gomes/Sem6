#include <iostream>
using namespace std;

string binarySum(string a, string b){
    string sum(4,'0'); // string_var(length,filler)
    int carry=0;

    for(int i=3;i>=0;i--){ // start from lsb
        int bit=a[i]-'0'+b[i]-'0'+carry; //dont forget to use a and b
        sum[i]=(bit%2)+'0';
        carry=bit/2; //bit is used not sum here
    }

    while(carry){
        int bit=sum[3]-'0'+carry;
        sum[3]=(bit%2)+'0';
        carry=bit/2; //bit is used not sum here
    }
    return sum;
}



string onesComplement(string s){
    for(char c: s){
        if(c=='1') c='0';
        else
         c='0';
    }
         return s; //outside loop
    
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