pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.10'
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
                    python -m venv venv
                    call venv\\Scripts\\activate && pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate && python -m pytest tests/
                '''
            }
        }

        stage('Code Quality') {
            steps {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                bat '''
                   call venv\\Scripts\\activate && flake8 app/ && pylint app/
                '''
            }
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    call venv\\Scripts\\activate && gunicorn app:app
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