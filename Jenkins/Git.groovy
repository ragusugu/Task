pipeline {
    agent any

    stages {
        stage('Checkout GitHub Repository') {
            steps {
                script {
                    // Specify your GitHub repository URL
                    def repoUrl = 'https://github.com/ragusugu/HI.git'

                    // Specify the branch you want to checkout
                    def branchName = 'main'

                    // Clean workspace before checking out (optional)
                    //cleanWs()

                    // Checkout the specified branch from the GitHub repository
                    checkout([$class: 'GitSCM', branches: [[name: "refs/heads/${branchName}"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: "${repoUrl}"]]])
                }
            }
        }

        // Add more stages as needed
        stage('Build') {
            steps {
                echo 'Your build steps here'
                // Add your build logic
            }
        }

        // Add more stages as needed
    }
}