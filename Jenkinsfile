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
                bat 'pip install -r requirements.txt' 
                bat 'pip install pytest pytest-cov' 
            } 
        } 
         
        stage('Run Tests') { 
            steps { 
                bat 'pytest --cov=. tests/' 
            } 
        } 
         
        stage('OWASP Dependency Check') { 
            steps { 
                bat 'dependency-check.bat --scan . --out dependency-reports --format "ALL"' 
            } 
            post { 
                always { 
                    archiveArtifacts artifacts: 'dependency-reports/*', allowEmptyArchive: true 
                } 
            } 
        } 
         
        stage('SonarQube Analysis') { 
            steps { 
                bat 'sonar-scanner -Dsonar.projectKey=squ_94844d41cfa7d84e19f88b7ac4c06645c1e5c1d2 -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000' 
            } 
        } 
         
        stage('Build Docker Image') { 
            steps { 
                bat 'docker build -t secure-python-app:latest .' 
            } 
        } 
         
        stage('Scan Docker Image with Trivy') { 
            steps { 
                bat 'trivy image --severity HIGH,CRITICAL secure-python-app:latest' 
            } 
        } 
         
        stage('Deploy') { 
            steps { 
                bat 'docker run -d -p 5000:5000 --name secure-python-app secure-python-app:latest' 
            } 
        } 
    } 
     
    post { 
        always { 
            // Clean up docker containers 
            bat 'docker stop secure-python-app || true' 
            bat 'docker rm secure-python-app || true' 
        } 
    } 
} 
