pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    environment {
    VERCEL_TOKEN = credentials('vercel_token')
  }
    stages {
        stage('Pre-clean') {
            steps {
                cleanWs()
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Bulding App') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python3 -m pip install -U pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python3 -m pytest 
                '''
            }
        }
        stage('Run Test for code coverage') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python3 -m pytest --cov
                '''
            }
        }
        stage('Generate html report for code coverage') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python3 -m pytest --cov --cov-report=html
                '''
            }
        }
        post {
        always {
          archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
          junit allowEmptyResults: true, testResults: '**/junit/*.xml'
        }
      }
    }

    stage('Install Vercel CLI') {
      steps {
        sh '''
          set -e
          # Prefer project-local CLI for reproducibility
          npm install --no-audit --no-fund --save-dev vercel
        '''
      }
    }

    stage('Link Vercel project') {
      steps {
        sh '''
          set -e
          npx vercel link --project code_coverage --token="$VERCEL_TOKEN" --yes
        '''
      }
    }

    stage('Deploy coverage report') {
      steps {
        sh '''
          set -e
          # Deploy the generated HTML coverage folder
          npx vercel --prod --token="$VERCEL_TOKEN" --confirm --cwd "$(pwd)/htmlcov"
        '''
      }
    }
  }