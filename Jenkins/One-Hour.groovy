pipeline {
    agent any
    
    triggers {
        cron('H 0 * * *') // Runs every day at the beginning of the hour
    }

    stages {
        stage('Your Stage Name') {
            steps {
                // Your pipeline steps go here
                echo "This pipeline runs every hour."
            }
        }
    }
}