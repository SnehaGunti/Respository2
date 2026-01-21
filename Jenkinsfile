
pipeline {
    agent any

    parameters {
        string(name: 'NUMBERS', defaultValue: '10 20', description: 'Enter two integers separated by space')
    }

    options { timestamps() }

    stages {
        stage('Show Workspace') {
            steps {
                sh 'pwd && ls -la'
                sh 'echo "--- python-pipeline-demo ---"; ls -la python-pipeline-demo || true'
                sh 'echo "--- pythondir ---"; ls -la pythondir || true'
            }
        }

        stage('Add Numbers') {
            steps {
                //  adjust folder name if your scripts are in pythondir/
                sh 'echo "$NUMBERS" | python3 python-pipeline-demo/add.py'
            }
        }

        stage('Check Even/Odd') {
            steps {
                //  adjust folder name if needed
                sh 'python3 python-pipeline-demo/check.py'
            }
        }

        stage('Archive Result') {
            steps {
                //  archive the file from the correct folder
                archiveArtifacts artifacts: 'python-pipeline-demo/sum.txt', onlyIfSuccessful: false
            }
        }
    }

    post {
        success { echo 'Sum is EVEN — pipeline SUCCESS.' }
        failure { echo ' Sum is ODD — pipeline FAILURE.' }
        always  { echo ' Build complete.' }
    }
}

