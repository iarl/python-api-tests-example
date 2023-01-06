pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages{
       
        stage('Checkout') {
            steps {
                script {
                    git url: "https://github.com/iarl/python-api-tests-example.git", branch: "jenkins"
                }
            }
        }

        stage('Build') {
                steps {
                    script {
                        sh "docker build ."
                    }
                }
            }
        
        stage('Test') {
                steps {
                    script {
                        sh "docker run api-tests"
                    }
                }
            }
        
        }
}