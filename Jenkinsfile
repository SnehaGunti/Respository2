
pipeline {
  agent any
  options { timestamps() }

  environment {
    MAIN_BRANCH    = 'main'            // change if your default branch differs
    CREDENTIALS_ID = 'Jenkins'  // <-- set to your real Jenkins Credentials ID
    GIT_USER_NAME  = 'SnehaGunti'
    GIT_USER_EMAIL = 'guntisneha944@.com'
  }

  stages {
    stage('Stage 1: Run on Branch') {
      steps {
        sh(
          script: '''
            #!/usr/bin/env bash
            set -euo pipefail

            CURRENT_BRANCH="${BRANCH_NAME:-$(git rev-parse --abbrev-ref HEAD)}"
            echo "Branch: ${CURRENT_BRANCH}"
            echo "Running on ${CURRENT_BRANCH}"
            echo "Stage 1 successful"
          ''',
          shell: '/bin/bash'
        )
      }
    }

    stage('Stage 2: Merge to main and Push') {
      when {
        expression {
          def br = (env.BRANCH_NAME ?: "")
          return br && br != env.MAIN_BRANCH
        }
      }
      steps {
        sh(
          script: '''
            #!/usr/bin/env bash
            set -euo pipefail

            CURRENT_BRANCH="${BRANCH_NAME:-$(git rev-parse --abbrev-ref HEAD)}"
            echo "Merging ${CURRENT_BRANCH} -> ${MAIN_BRANCH}"

            git config user.name  "${GIT_USER_NAME}"
            git config user.email "${GIT_USER_EMAIL}"

            git fetch origin
            git checkout -B "${MAIN_BRANCH}" "origin/${MAIN_BRANCH}"

            git merge --no-ff --no-edit "${CURRENT_BRANCH}"
            echo "Stage 2 local merge successful: ${CURRENT_BRANCH} -> ${MAIN_BRANCH}"
          ''',
          shell: '/bin/bash'
        )

        script {
          if (env.CREDENTIALS_ID?.trim()) {
            sshagent(credentials: [env.CREDENTIALS_ID]) {
              sh(
                script: '''
                  #!/usr/bin/env bash
                  set -euo pipefail
                  git push origin "${MAIN_BRANCH}"
                  echo "Stage 2 push successful"
                ''',
                shell: '/bin/bash'
              )
            }
          } else {
            echo 'CREDENTIALS_ID not set — skipping push to origin.'
          }
        }
      }
    }

    stage('Stage 3: Checkout main and Run') {
      steps {
        sh(
          script: '''
            #!/usr/bin/env bash
            set -euo pipefail

            git fetch origin
            git checkout -B "${MAIN_BRANCH}" "origin/${MAIN_BRANCH}" || git checkout "${MAIN_BRANCH}"

            echo "Running on ${MAIN_BRANCH}"
            echo "Stage 3 successful"
          ''',
          shell: '/bin/bash'
        )
      }
    }
  }

  post {
    success { echo 'Pipeline finished successfully.' }
    failure { echo 'Pipeline failed. Check console output.' }
  }
}

