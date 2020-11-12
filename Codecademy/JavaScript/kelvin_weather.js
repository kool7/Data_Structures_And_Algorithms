// tempreature in kelvin
const kelvin = 0;

// temperature in celsius
const celsius = kelvin - 273;

// Fahrenheit
let fahrenheit = celsius * (9/5) + 32;

//Newton
let newton = celsius * (33/100);

// nearest integer less than equal to number
fahrenheit = Math.floor(fahrenheit);

// nearest integer less than equal to number
newton = Math.floor(newton);

// log results in console
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

// log results in console
console.log(`The temperature is ${newton} degrees Newton.`);
