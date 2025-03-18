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
                bat 'python -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests/'
            }
        }
        
        // Other stages commented out until basics work
        /*
        stage('OWASP Dependency Check') {
            steps {
                bat 'echo Running dependency check'
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                bat 'echo Running SonarQube analysis'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat 'echo Building Docker image'
            }
        }
        */
    }
    
    post {
        always {
            bat 'echo Finished pipeline execution'
        }
    }
}