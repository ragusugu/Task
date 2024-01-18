pipeline {
    agent any
    
    parameters {
        string(name: 'MY_PARAMETER', defaultValue: 'Default_Value', description: 'Enter a value for the parameter')
    }
    
    stages {
        stage('Print Parameter Value') {
            steps {
                script {
                    echo "Value of MY_PARAMETER: ${params.MY_PARAMETER}"
                }
            }
        }
    }
}