/*
2
ＣＴＵＯＰＥＮＰＲＯＧＲＡＭＭＩＮＧＣＯＮＴＥＳＴ
Ｃ   Ｔ   Ｕ   Ｏ   Ｐ   Ｅ   Ｎ   Ｐ   Ｒ   Ｏ   Ｇ   Ｒ   Ａ
   Ｍ   Ｍ   Ｉ   Ｎ   Ｇ   Ｃ   Ｏ   Ｎ   Ｔ   Ｅ   Ｓ   Ｔ

7
ＴＨＩＳＩＳＡＳＥＣＲＥＴＭＥＳＳＡＧＥＴＨＡＴＮＯＯＮＥＳＨＯＵＬＤＥＶＥＲＳＥＥＬＥＴＳＥＮＣＲＹＰＴＩＴ
Ｔ                  Ｈ                  Ｉ                  Ｓ                  Ｉ                  Ｓ                  Ａ                  Ｓ
   Ｅ                  Ｃ                  Ｒ                  Ｅ                  Ｔ                  Ｍ                  Ｅ                  Ｓ
      Ｓ                  Ａ                  Ｇ                  Ｅ                  Ｔ                  Ｈ                  Ａ                  Ｔ
         Ｎ                  Ｏ                  Ｏ                  Ｎ                  Ｅ                  Ｓ                  Ｈ                  Ｏ
            Ｕ                  Ｌ                  Ｄ                  Ｅ                  Ｖ                  Ｅ                  Ｒ                  Ｓ
               Ｅ                  Ｅ                  Ｌ                  Ｅ                  Ｔ                  Ｓ                  Ｅ                  Ｎ
                  Ｃ                  Ｒ                  Ｙ                  Ｐ                  Ｔ                  Ｉ                  Ｔ
*/

#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int input;
    string message, plainText, cipherText;
    while (cin >> input && input != 0)
    {
        cin.ignore();
        getline(cin, message);
        plainText.clear();
        for (const char ch : message) {
            if (!isspace(ch)) {
                plainText += toupper(ch);
            }
        }
        cipherText.resize(plainText.size());
        unsigned long long loop = 0;
        unsigned long long index = 0;
        for (const auto ch : plainText)
        {
            cipherText[index] = ch;
            index += input;
            if (index >= plainText.length())
            {
                loop++;
                index = loop; 
            }
        }
        cout << cipherText << '\n';
    }
    return 0;
}
