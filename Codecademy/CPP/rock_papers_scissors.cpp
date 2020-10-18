#include <iostream>
#include <cstdlib>

int main() {

  // select random  number every time program runs
  srand(time(NULL));
  int computer = rand() % 3 + 1;
  int user = 0;

  // output options on screen
  std::cout << "====================\n";
  std::cout << "rock paper scissors!\n";
  std::cout << "====================\n";

  std::cout << "1) ✊\n";
  std::cout << "2) ✋\n";
  std::cout << "3) ✌️\n";

  std::cout << "shoot! ";

  // take user input
  std::cin >> user;

  // print user's choice on screen
  if (user == 1){
    std::cout << "You cho0se: ✊\n";
  }
  else if (user == 2){
    std::cout << "You choose: ✋\n";
  }
  else if (user == 3){
    std::cout << "You choose: ✌️\n";
  }

  // print computer's choice on screen
  if (computer == 1){
    std::cout << "CPU cho0se: ✊\n";
  }
  else if (computer == 2){
    std::cout << "CPU choose: ✋\n";
  }
  else if (computer == 3){
    std::cout << "CPU choose: ✌️\n";
  }

  // if CPU == USER
  if (computer == user){
    std::cout << "Tie\n";
  }

  // condition 1
  else if (user == 1){
    if (computer == 2){
      std::cout << "You lose.";
    }
    if (computer == 3){
      std::cout << "You won!";
    }
  }
  
  // condition 2
  else if (user == 2){
    if (computer == 1){
      std::cout << "You Won.";
    }
    if (computer == 3){
      std::cout << "You lost!";
    }
  }

  // condition 3
  else if (user == 3){
    if (computer == 1){
      std::cout << "You lose.";
    }
    if (computer == 2){
      std::cout << "You won!";
      }
  }

  return 0;

}