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
                bat '"C:\\Path\\To\\Python\\python.exe" -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '"C:\\Path\\To\\Python\\python.exe" -m pytest tests/'
            }
        }
    }
    
    post {
        always {
            bat 'echo Finished pipeline execution'
        }
    }
}