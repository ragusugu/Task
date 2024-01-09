// Assuming you have a string with length 10
let inputString = "sugan";

// Add $ symbol after each word
let stringWithDollars = inputString.split('').join('$');

// Display the string with $ symbols
console.log(`String with $ symbols: ${stringWithDollars}`);

// Arrange the string into alphabetical order
let sortedString = inputString.split('').sort().join('');

// Display the string in alphabetical order
console.log(`String in alphabetical order: ${sortedString}`);
