pipeline {
    agent any
    stages {
        stage('Print Text') {
            steps {
                echo 'hello!'
            }
        }
    }
}
