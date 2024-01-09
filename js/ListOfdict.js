// Your list of dictionaries
const listOfDictionaries = [
 { key1: "value1a", key2: "value2a", selected: true },
 { key1: "value1b", key2: "value2b", selected: false },
 { key1: "value1c", key2: "value2c", selected: true }
];

// Iterate through the list and display each dictionary
console.log("List of Dictionaries:");
for (const dictionary of listOfDictionaries) {
 console.log(dictionary);
}

// Find dictionaries with key "selected" and value "True"
const selectedDictionaries = listOfDictionaries.filter(dict => dict.selected === true);

// Print each key-value pair for selected dictionaries
for (const selectedDictionary of selectedDictionaries) {
 console.log("Selected: true ==> ", selectedDictionary);

 // Display each key and value separately for the selected dictionary
 for (const key in selectedDictionary) {
   if (selectedDictionary.hasOwnProperty(key)) {
     console.log(`${key}: ${selectedDictionary[key]}`);
   }
 }
 console.log(); // Add a newline for better readability between dictionaries
}
