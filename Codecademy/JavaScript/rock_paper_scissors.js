// User Input
const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if(userInput === 'rock' || userInput === 'paper' || userInput === 'scissors') {
    return userInput;
  }
  else{
    console.log('Please Enter Valid Input.')
  }
};

// Computer Choice
const getComputerChoice = () => {
  num = Math.floor(Math.random() * 3);
  switch (num){
    case 1:
      return 'rock';
      break;

    case 2:
      return 'paper';
      break;

    case 3:
      return 'scissors';
      break;
  }
};

// Winner
function determineWinner(userChoice, computerChoice){
  if(userChoice === computerChoice){
    return "Tie";
  }

  if(userChoice === 'rock'){
    if(computerChoice === 'paper'){
      return "Computer Won!";
    }
    else{
      return "User Won!";
    }
  }

  if(userChoice === 'paper'){
    if(computerChoice === 'scissors'){
      return "Computer Won!";
    }
    else{
      return "User Won!";
    }
  }

  if(userChoice === 'scissors'){
    if(computerChoice === 'rock'){
      return "Computer Won!";
    }
    else{
      return "User Won!";
    }
  }
};

function playgame(){
  userChoice = getUserChoice('rock');
  console.log(`User's Choice ${userChoice}`);
  computerChoice = getComputerChoice();
  console.log(`Computer's Choice ${computerChoice}`);
  console.log(determineWinner(userChoice, computerChoice));
};

playgame();