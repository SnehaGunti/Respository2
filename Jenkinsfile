
pipeline {
    agent any

    parameters {
        string(
            name: 'NUMBERS',
            defaultValue: '10 20',
            description: 'Enter two integers separated by a space (e.g., "10 20")'
        )
    }

    options {
        timestamps()
    }

    stages {
        stage('Show Workspace') {
            steps {
                sh 'pwd && ls -la'
            }
        }

        stage('Add Numbers') {
            steps {
                // Send NUMBERS to add.py via stdin so Jenkins doesn’t wait for interactive input
                sh 'echo "$NUMBERS" | python3 add.py'
            }
        }

        stage('Check Even/Odd') {
            steps {
                // Exit code 0 => SUCCESS, 1 => FAILURE
                sh 'python3 check.py'
            }
        }

        stage('Archive Result') {
            steps {
                archiveArtifacts artifacts: 'sum.txt', onlyIfSuccessful: false
            }
        }
    }

    post {
        success {
            echo ' Sum is EVEN — pipeline SUCCESS.'
        }
        failure {
            echo ' Sum is ODD — pipeline FAILURE.'
        }
        always {
            echo ' Build complete.'
        }
    }
}

