pipeline {
  agent any

  environment {
    IMAGE_NAME = 'rishabhraj7/python-app'
  }

  stages {
    stage('Docker Compose Build') {
      steps {
        bat 'docker-compose build'
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'docker-hub-creds',
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          bat """
            echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
            docker tag python-app %IMAGE_NAME%
            docker push %IMAGE_NAME%
          """
        }
      }
    }

    stage('Run with Docker Compose') {
      steps {
        bat 'docker-compose down || exit 0'
        bat 'docker-compose up -d'
      }
    }

    stage('Verify Containers') {
      steps {
        bat 'docker ps'
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
