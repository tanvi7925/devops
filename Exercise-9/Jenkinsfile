pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('9-jenkins-multistage-pipeline') {
                    echo 'Installing dependencies...'
                    sh '''
                        python3 -m venv .venv
                        .venv/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                dir('9-jenkins-multistage-pipeline') {
                    echo 'Running unit tests...'
                    sh '.venv/bin/python -m unittest discover -s .'
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('9-jenkins-multistage-pipeline') {
                    sh '''
                        mkdir -p python-app-deploy
                        cp app.py python-app-deploy/
                    '''
                }
            }
        }

        stage('Run Application') {
            steps {
                dir('9-jenkins-multistage-pipeline') {
                    sh '''
                        nohup .venv/bin/python python-app-deploy/app.py \
                            > python-app-deploy/app.log 2>&1 &
                        echo $! > python-app-deploy/app.pid
                    '''
                }
            }
        }

        stage('Test Application') {
            steps {
                dir('9-jenkins-multistage-pipeline') {
                    sh '.venv/bin/python test_app.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs.'
        }
    }
}