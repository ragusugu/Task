// Empty list
const listOfDictionaries = [];

// Dynamic function to add a dictionary to the list
function addDictionaryToTheList() {
  if (listOfDictionaries.length < 10) {
    // Add a dictionary to the list
    const newDictionary = {
      // key1: "value1",
      // key2: "value2",
    };

    // Example of adding more key-value pairs dynamically
    for (let i = 0; i <= 5; i++) {
     newDictionary[`key${i}`] = `value${i}`;
    }

    listOfDictionaries.push(newDictionary);
    console.log("Dictionary added successfully!");
  } else {
    console.log("List is already at its maximum length (10 dictionaries).");
  }
}

// Test the function to add dictionaries until the list reaches 10
for (let i = 0; i < 11; i++) {
  addDictionaryToTheList();
}

// Display the final list of dictionaries
console.log("Final List of Dictionaries:", listOfDictionaries);
