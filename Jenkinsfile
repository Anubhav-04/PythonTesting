pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage('Pre-clean') {
            steps {
                // Clean workspace before code checkout
                cleanWs()
            }
        }
        stage('Checkout') {
            steps {
                // Check out your code from SCM
                checkout scm
            }
        }
        stage('Bulding App') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install pytest
                    pip install pytest-cov
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        stage('Run Test for code coverage') {
            steps {
                sh 'pytest --cov'
            }
        }
    }
}