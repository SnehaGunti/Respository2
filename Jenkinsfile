
pipeline {
  agent any
  options { timestamps() }

  environment {
    MAIN_BRANCH    = 'main'             // change if your default branch differs
    CREDENTIALS_ID = 'Jenkins'   // <-- set your Jenkins Credentials ID (SSH)
    GIT_USER_NAME  = 'SnehaGunti'
    GIT_USER_EMAIL = 'guntisneha944@gmail.com'
  }

  stages {

    stage('Stage 1: Checkout & Run on Branch') {
      steps {
        // Use bash to avoid "Illegal option -o pipefail" errors
        sh(
          script: '''
            #!/usr/bin/env bash
            set -euo pipefail

            # Determine the current branch name: prefer BRANCH_NAME (multibranch),
            # else detect from Git (single-branch jobs)
            CURRENT_BRANCH="${BRANCH_NAME:-$(git rev-parse --abbrev-ref HEAD)}"
            echo "Branch (detected): ${CURRENT_BRANCH}"

            # Your branch tasks go here (replace with real build/test commands)
            echo "Running on ${CURRENT_BRANCH}..."
            echo " Stage 1 successful"
          ''',
          shell: '/bin/bash'
        )
      }
    }

    stage('Stage 2: Merge current branch -> main & Push') {
      // Skip Stage 2 if we are already on main
      when {
        expression { 
          // Guard against null/empty BRANCH_NAME (single-branch freestyle)
          def br = (env.BRANCH_NAME ?: '')
          return br && br != env.MAIN_BRANCH
        }
      }
      steps {
        sh(
          script: '''
            #!/usr/bin/env bash
            set -euo pipefail

            CURRENT_BRANCH="${BRANCH_NAME:-$(git rev-parse --abbrev-ref HEAD)}"
            echo "Preparing to merge ${CURRENT_BRANCH} -> ${MAIN_BRANCH}"

            # User config for merge commit metadata
            git config user.name  "${GIT_USER_NAME}"
            git config user.email "${GIT_USER_EMAIL}"

            # Ensure we have up-to-date refs
            git fetch origin

            # Create/update local main from remote
            git checkout -B "${MAIN_BRANCH}" "origin/${MAIN_BRANCH}"

            # Merge the feature/current branch into main
            git merge --no-ff --no-edit "${CURRENT_BRANCH}" || {
              echo " Merge conflict. Resolve locally and re-run the job."; 
              exit 1;
            }

            echo " Stage 2 local merge successful: ${CURRENT_BRANCH} -> ${MAIN_BRANCH}"
          ''',
          shell: '/bin/bash'
        )

        script {
          if (env.CREDENTIALS_ID?.trim()) {
            // Push merged main to origin using SSH credentials
            sshagent(credentials: [env.CREDENTIALS_ID]) {
              sh(
                script: '''
                  #!/usr/bin/env bash
                  set -euo pipefail
                  git push origin "${MAIN_BRANCH}"
                  echo " Stage 2 push successful: pushed ${MAIN_BRANCH} to origin"
                ''',
                shell: '/bin/bash'
              )
            }
          } else {
            echo ' CREDENTIALS_ID not set — skipping push to origin.'
          }
        }
      }
    }

    stage('Stage 3: Checkout main & Run') {
      steps {
        sh(
          script: '''
            #!/usr/bin/env bash
            set -euo pipefail

            # Make sure we are on the latest main
            git fetch origin
            git checkout -B "${MAIN_BRANCH}" "origin/${MAIN_BRANCH}" || git checkout "${MAIN_BRANCH}"

            # Your "run on main" tasks go here (replace with real commands)
            echo "Running on ${MAIN_BRANCH}..."
            echo " Stage 3 successful"
          ''',
          shell: '/bin/bash'
        )
      }
    }
  }

  post {
    success { echo ' Pipeline finished successfully.' }
    failure { echo ' Pipeline failed. Check console output.' }
  }
}
``

