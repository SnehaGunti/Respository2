
pipeline {
    agent any

    options {
        // Removed ansiColor because it's not a valid option in your setup
        timestamps()
    }

    parameters {
        string(name: 'NUMBERS', defaultValue: '10 20', description: 'Space-separated integers to add (e.g., "10 20 -3 5")')
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Add Numbers') {
            steps {
                // Feed numbers non-interactively
                sh '''
                    echo "$NUMBERS" | python3 add.py
                '''
            }
        }

        stage('Check Even/Odd') {
            steps {
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
            echo 'Pipeline marked SUCCESS because the sum is EVEN.'
        }
        failure {
            echo 'Pipeline marked FAILURE because the sum is ODD (check.py exited 1).'
        }
        always {
            echo 'Build complete.'
        }
    }
}
``

