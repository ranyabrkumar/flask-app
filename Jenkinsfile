pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.13'
        FLASK_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                    python3 -m venv venv
                    call . venv//bin//activate && pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call . venv//bin//activate && python -m pytest tests/
                '''
            }
        }

        stage('Code Quality') {
            steps {
                bat '''
                   call . venv//bin//activate && flake8 app/
                //    pylint app/
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    call . venv//bin//activate && gunicorn app:app
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}