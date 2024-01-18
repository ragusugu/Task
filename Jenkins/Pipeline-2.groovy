pipeline {
    agent any

    parameters {
        string(name: 'PARAMETER_VALUE', defaultValue: 'default_value', description: 'Value to pass to Job-B')
    }

    stages {
        stage('Build') {
            steps {
                echo "Building Job A with parameter value: ${params.PARAMETER_VALUE}"
                // Your pipeline logic for Job A
            }
        }
    }