#include <iostream>
#include <string>
#include <iomanip>

bool is_palindrome(std::string text){
  std::string name = text;
  std::string r_name = text;
  bool result = true;
  
  for(int i = 0; i < text.size(); ++i){
    for(int j = text.size() - 1; j >=0; --j){
        if(name[i] == r_name[j]){
            result = true;
            i += 1;
        } else {
            result = false;
            j = -1;
            break;
        }
    if(result == false){
        break;
    }
    }
  }
  return result;
}

int main() {
  
  std::cout << std::boolalpha << is_palindrome("madam") << "\n";
  std::cout << std::boolalpha << is_palindrome("ada") << "\n";
  std::cout << std::boolalpha << is_palindrome("lovelace") << "\n";

  std::cout << std::fixed << std::setprecision(2) << 12.3456;

  std::cin.ignore(1000, '\n');
  std::cout << "Tecle <Enter> para encerrar";
  std::cin.get();

  return 0;
}
