pipeline {
  agent any

  environment {
    IMAGE_NAME = 'rishabhraj7/python-app'
    CONTAINER_NAME = 'python-app-container'
  }

  stages {
    stage('Build Docker Image') {
      steps {
        bat "docker build -t %IMAGE_NAME% ."
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'docker-hub-creds',
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          bat '''
            echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
            docker push %IMAGE_NAME%
          '''
        }
      }
    }

    stage('Run Docker Container') {
      steps {
        bat '''
          docker stop %CONTAINER_NAME% || exit 0
          docker rm %CONTAINER_NAME% || exit 0
          docker run -d --name %CONTAINER_NAME% -p 5000:5000 %IMAGE_NAME%
        '''
      }
    }

    stage('Verify Running Container') {
      steps {
        bat 'docker ps -f name=%CONTAINER_NAME%'
      }
    }
  }

  post {
    success {
      echo '✅ Build, push, and run successful!'
    }
    failure {
      echo '❌ Pipeline failed.'
    }
  }
}
