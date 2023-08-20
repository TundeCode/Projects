#include <iostream>
#include <string>
#include <cctype>

std::string removePrefix(const std::string& url) {
    std::string newUrl;
    std::string::size_type prefixPos = url.find("://");

    if (prefixPos != std::string::npos) {
        prefixPos += 3;  
        std::string::size_type suffixPos = url.find('/', prefixPos);

        if (suffixPos != std::string::npos) {
            newUrl = url.substr(prefixPos, suffixPos - prefixPos);
        } else {
            newUrl = url.substr(prefixPos);
        }
    }

    std::string::size_type portPos = newUrl.find(':');
    if (portPos != std::string::npos) {
        newUrl = newUrl.substr(0, portPos);
    }

    for (char& ch : newUrl) {
        ch = std::tolower(ch);
    }

    return newUrl;
}

int main() {
    std::string url;
    std::getline(std::cin, url);

    std::string newUrl = removePrefix(url);
    std::cout << newUrl << std::endl;

    return 0;
}
