
pipeline {
  agent any

  options { timestamps() }

  environment {
    MAIN_BRANCH     = 'main'                 // change if your default branch is different
    CREDENTIALS_ID  = 'Jenkins'                     // e.g., 'git-ssh-key' or 'github-pat'; leave blank to skip push
    GIT_USER_NAME   = 'Jenkins CI'
    GIT_USER_EMAIL  = 'jenkins@example.com'
  }

  stages {
    stage('Stage 1: Checkout & Run on Branch') {
      steps {
        sh '''
          set -euxo pipefail
          echo "Branch (Multibranch): ${BRANCH_NAME}"
          #  Run your branch code here (replace with your real commands)
          echo "Running on ${BRANCH_NAME}..."
          echo " Stage 1 successful"
        '''
      }
    }

    stage('Stage 2: Merge current branch -> main & Push') {
      when {
        expression { env.BRANCH_NAME != env.MAIN_BRANCH } // skip if already on main
      }
      steps {
        sh '''
          set -euxo pipefail
          git config user.name  "${GIT_USER_NAME}"
          git config user.email "${GIT_USER_EMAIL}"

          # Make sure main is up to date locally
          git fetch origin
          git checkout -B "${MAIN_BRANCH}" "origin/${MAIN_BRANCH}"

          # Merge the feature branch (current build branch) into main
          git merge --no-ff --no-edit "${BRANCH_NAME}" || {
            echo " Merge conflict. Resolve manually and re-run."; exit 1;
          }

          echo " Stage 2 local merge successful: ${BRANCH_NAME} -> ${MAIN_BRANCH}"
        '''

        script {
          if (env.CREDENTIALS_ID?.trim()) {
            // Push the merged main back to origin using provided creds
            sshagent(credentials: [env.CREDENTIALS_ID]) {
              sh '''
                set -euxo pipefail
                git push origin "${MAIN_BRANCH}"
                echo " Stage 2 push successful: pushed ${MAIN_BRANCH} to origin"
              '''
            }
          } else {
            echo ' CREDENTIALS_ID not set — skipping push to origin.'
          }
        }
      }
    }

    stage('Stage 3: Checkout main & Run') {
      steps {
        sh '''
          set -euxo pipefail
          git checkout "${MAIN_BRANCH}"

          #  Run tasks on main (replace with your real commands)
          echo "Running on ${MAIN_BRANCH}..."
          echo " Stage 3 successful"
        '''
      }
    }
  }

  post {
    success { echo ' Pipeline finished successfully.' }
    failure { echo ' Pipeline failed. Check console output.' }
  }
}

