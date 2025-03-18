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
                bat '"C:\\Projects\\secure-python-app\\venv\\Scripts\\python.exe" -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '"C:\\Projects\\secure-python-app\\venv\\Scripts\\python.exe" -m pytest tests/'
            }
        }
    }
    
    post {
        always {
            bat 'echo Finished pipeline execution'
        }
    }
}