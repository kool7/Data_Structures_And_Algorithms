#include <iostream>
#include <vector>
#include "ufo_functions.hpp"

int main() {
  char letter;
  std::string codeword = "codecademy";
  std::string answer = "__________";
  int misses = 0;
  std::vector<char> incorrect;
  bool guess = false;

  while (answer != codeword and misses < 7){

    end_game(answer, codeword);
    display_misses(misses);
    display_status(incorrect, answer);

    std::cout << "\nPlease enter your guess: \n";
    std::cin >> letter;

    for (int i =0; i < codeword.length(); i++){
      if(letter == codeword[i]){
        answer[i]==letter;
        guess=true;
      }
    }

    if (guess){
      std::cout << "\nCorrect!\n";
    }
    else{
      std::cout << "Incorrect! The tractor beam pulls the person in further.\n";
      incorrect.push_back(letter);
      misses++;
    }

    guess=false;

  }

}
