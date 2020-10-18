#include <iostream>
#include <cstdlib>

int main() {

  std::cout << "MAGIC 8-BALL\n";

  // setting seed 
  srand(time(NULL));
  int answer = std::rand() % 10;

  if (answer == 0){
    std::cout << "It is certain.";
  }
  else if (answer == 1){
    std::cout << "Very doubtful.";
  }
  else if (answer == 2){
    std::cout << "It is decidedly so.";
  }
  else if (answer == 3){
    std::cout << "Yes - definitely";
  }
  else{
    std::cout << "Yes.";
  }

  return 0;

}