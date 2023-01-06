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
                        sh "docker build --no-cache -t api-tests"
                    }
                }
            }
        
        stage('Test') {
                steps {
                    script {
                        sh "docker run --rm -d --priveleged api-tests"
                    }
                }
            }
        
        }
}