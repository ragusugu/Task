// Step 1: Create a list of string values with a length of 5
let myArray = ["Apple", "Banana", "Cherry", "Date", "Elderberry"];

// Step 2: Separate even index values in one array and odd index values in another array
let evenIndexValues = myArray.filter((_, index) => index % 2 === 0);
let oddIndexValues = myArray.filter((_, index) => index % 2 !== 0);
console.log("Even Index Values:", evenIndexValues);
console.log("odd Index Values:", oddIndexValues);

var myArray1
// Step 3: Remove odd index values from the array
myArray1 = myArray.filter((_, index) => index % 2 === 0);
console.log("removed list:", myArray1);
// Step 4: Display only even index values from the array
let even  = myArray1.filter((_, index) => index % 2 === 0);

console.log("latest Even Index Values:", even);
// console.log("odd Index Values:", oddIndexValues);


// Step 5: Add two more string values after the 3rd index of the array
myArray1.splice(3, 0, "Fig", "Blackcurrent");

// Step 6: Display the modified array
console.log("Modified Array:", myArray1);

// Step 7: Sort the string values in ascending order and display
myArray1.sort();
console.log("Sorted Array:", myArray1);
