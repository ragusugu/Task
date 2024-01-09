// Your list of numeric values
const numericValues = [5, 2, 8, 1, 7, 3, 10, 4, 6, 9];

// Step 1: Sort the values in ascending order
const sortedValues = numericValues.slice().sort((a, b) => a - b);

// Step 2: Add one to each value using map and reduce
const resultList = sortedValues.map(value => value + 1);

// Display the sorted values
console.log("Sorted Values:", sortedValues);

// Display the list after adding one to each value
console.log("List after adding one:", resultList);
