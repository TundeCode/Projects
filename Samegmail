#include <iostream>
#include <string>
#include <cctype>

std::string removeDot(std::string& email) {
    std::string newEmail;
    bool ignoreDot = true;
    for (char ch : email) {
        if (ch == '@') {
            ignoreDot = false; 
            newEmail += ch;
        } else if (ch == '.') {
            if (!ignoreDot) {
                newEmail += ch;
            }
        } else {
            newEmail += tolower(static_cast<unsigned char>(ch));
        }
    }
    return newEmail;
}

std::string removePlus(std::string& email) {
    std::string newEmail;
    bool ignore = false;
    for (char ch : email) {
        if (ch == '+') {
            ignore = true;
        } else if (ch == '@') {
            ignore = false;
            newEmail += ch;
        }
        if (!ignore && ch != '+' && ch != '@') {
            newEmail += std::tolower(static_cast<unsigned char>(ch));
        }
    }
    return newEmail;
}

int main() {
    std::string email;
    std::cin >> email;

    std::string email2;
    std::cin >> email2;

    std::string newEmail = removeDot(email);
    newEmail = removePlus(newEmail);
    std::string newEmail2 = removeDot(email2);
    newEmail2 = removePlus(newEmail2);

    if (newEmail == newEmail2) {
        std::cout << "True" << std::endl;
    } else {
        std::cout << "False" << std::endl;
    }

    // std::cout << newEmail << std::endl;
    // std::cout << newEmail2 << std::endl;

    return 0;
}
