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
                bat 'C:\\Users\\ashis\\AppData\\Local\\Python\\bin\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat 'C:\\Users\\ashis\\AppData\\Local\\Python\\bin\\python.exe -m pytest tests\\utilities\\test_webpages.py --headed --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Playwright Report'
            ])
        }
    }
}