#include <iostream>
#include <string>

int main(){
    std::string input;
    std::getline(std:: cin, input);
    for(int i =0; i <input.size(); i++){
        if(input[i] == input[i+1]){
            continue;
        }
        else if( input[i] != input[i + 1]){
            std::cout << input[i];

        }

        }
    return 0;
}
