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

        stage('Tests') {
            parallel (
            'Unit Tests': {
                steps {
                bat '''
                call venv\\Scripts\\activate && python -m pytest tests/unit
                '''
                }
            },
            'Integration Tests': {
                steps {
                bat '''
                call venv\\Scripts\\activate && python -m pytest tests/integration
                '''
                }
            }
            )
        }

            

        stage('Code Quality') {
            steps {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                bat '''
                   call venv\\Scripts\\activate && flake8 app/
                '''
            }
            }
        }

        stage('Deploy') {
            steps {
                bat 'call venv\\Scripts\\activate && start /B gunicorn run:app'
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