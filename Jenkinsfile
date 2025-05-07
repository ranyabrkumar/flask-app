pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.13.2'
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
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        bat '''
                            call venv\\Scripts\\activate
                            python -m pytest tests/unit --junitxml=unit_test_results.xml
                        '''
                    }
                }
                stage('Integration Tests') {
                    steps {
                        bat '''
                            call venv\\Scripts\\activate
                            python -m pytest tests/integration --junitxml=integration_test_results.xml
                        '''
                    }
                }
            }
        }

            

        stage('Code Quality') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat '''
                        call venv\\Scripts\\activate
                        flake8 app/
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
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
        // Executed only on success
        emailext subject: 'Build Successful',
                 body: 'Your build has completed successfully',
                 to: 'ranyabrkumar@gmail.com'
    }
    failure {
        // Executed only on failure
        emailext subject: 'Build Failed',
                 body: 'Your build has failed',
                 to: 'ranyabrkumar@gmail.com'
    }
    }
}
