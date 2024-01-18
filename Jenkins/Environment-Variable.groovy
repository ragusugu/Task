pipeline {
    agent any
    
    stages {
        stage('Print Environment Variable') {
            steps {
                script {
                    echo "Value of MY_VARIABLE: ${env.MY_VARIABLE}"
                }
            }
        }
    }
}
