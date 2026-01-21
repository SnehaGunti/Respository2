
pipeline {
    agent any

    options {
        // keep console clean & fail fast on errors
        ansiColor('xterm')
        timestamps()
    }

    parameters {
        // Let you choose the numbers from the Jenkins UI at build time
        string(name: 'NUMBERS', defaultValue: '10 20', description: 'Space-separated integers to add (e.g., "10 20 -3 5")')
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                // Make sure Python files are present (for fresh workspaces)
                sh 'ls -la'
            }
        }

        stage('Add Numbers') {
            steps {
                // Feed numbers to add.py via stdin (non-interactive)
                sh '''
                    echo "$NUMBERS" | python3 add.py
                '''
            }
        }

        stage('Check Even/Odd') {
            steps {
                // Exit code 0 => success, 1 => fail, 2 => infra error
                sh 'python3 check.py'
            }
        }

        stage('Archive Result') {
            steps {
                // Keep the output file as a build artifact
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
        unstable {
            echo 'Pipeline UNSTABLE.'
        }
        always {
            echo 'Build complete.'
        }
    }
}

