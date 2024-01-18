pipeline {
    agent any

    stages {
        stage('Create Directory') {
            steps {
                script {
                    // Create a directory named 'my_directory'
                    dir('my_directory') {
                        echo "Creating directory: my_directory"
                    }
                }
            }
        }

        stage('Create Text File') {
            steps {
                script {
                    // Create a text file named 'my_file.txt' inside 'my_directory'
                    writeFile(file: 'my_directory/my_file.txt', text: '')
                    echo "Creating text file: my_directory/my_file.txt"
                }
            }
        }

        stage('Write Content to File') {
            steps {
                script {
                    // Write content to 'my_directory/my_file.txt'
                    writeFile(file: 'my_directory/my_file.txt', text: 'i love space')
                    echo "Writing content to my_directory/my_file.txt"
                }
            }
        }

        stage('Print File Content') {
            steps {
                script {
                    // Read and print the content of 'my_directory/my_file.txt'
                    def fileContent = readFile(file: 'my_directory/my_file.txt').trim()
                    echo "Content of my_directory/my_file.txt: ${fileContent}"
                }
            }
        }
    }
}