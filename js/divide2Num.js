// Generate two random integers
const num1 = Math.floor(Math.random() * 100) + 1;
const num2 = Math.floor(Math.random() * 100) + 1;

// Perform division
const result = num1 / num2;

// Check if the result is a whole number
if (Number.isInteger(result)) {
    console.log(`The result of ${num1} / ${num2} is: ${result}`);
} else {
    // Display result with 2 decimal points
    console.log(`The result of ${num1} / ${num2} is: ${result.toFixed(2)}`);
}
