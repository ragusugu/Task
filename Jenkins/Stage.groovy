pipeline {
    agent any

    stages {
        stage('Stage 1') {
            when {
                expression { params.RUN_STAGE_1 == 'true' }
            }
            steps {
                echo 'Executing Stage 1'
                // Your stage 1 logic here
            }
        }

        stage('Stage 2') {
            when {
                expression { params.RUN_STAGE_2 == 'true' }
            }
            steps {
                echo 'Executing Stage 2'
                // Your stage 2 logic here
            }
        }

        stage('Stage 3') {
            when {
                expression { params.RUN_STAGE_3 == 'true' }
            }
            steps {
                echo 'Executing Stage 3'
                // Your stage 3 logic here
            }
        }
    }

    parameters {
        booleanParam(name: 'RUN_STAGE_1', defaultValue: true, description: 'Run Stage 1')
        booleanParam(name: 'RUN_STAGE_2', defaultValue: false, description: 'Run Stage 2')
        booleanParam(name: 'RUN_STAGE_3', defaultValue: true, description: 'Run Stage 3')
    }
}