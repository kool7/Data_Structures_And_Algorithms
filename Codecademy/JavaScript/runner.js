let raceNumber = Math.floor(Math.random() * 1000);


let raceRegister = false;
let raceAge = 18;

if (raceAge > 18 && raceRegister) {
  raceNumber += 1000;
}

if (raceAge > 18 && raceRegister === true) {
  console.log(`${raceNumber} will race at 9:30.`);
}
else if (raceAge > 18 && raceRegister === false) {
  console.log(`${raceNumber} will race at 11:30.`);
}
else if (raceAge < 18) {
  console.log(`${raceNumber} will race at 12:30.`);
}
else {
  console.log(`See registration desk.`);
}