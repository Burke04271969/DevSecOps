pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'run-python.bat -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'run-python.bat -m pytest tests/'
            }
        }
    }
    
    post {
        always {
            bat 'echo Finished pipeline execution'
        }
    }
}