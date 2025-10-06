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
                sh 'npm install -g vercel'
            }
        }
        stage('Deploy to Vercel') {
            steps {
                dir('htmlcov') {
                    sh 'vercel --prod --token=$VERCEL_TOKEN --confirm --name=code_coverage'
                }
            }
        }
    }
