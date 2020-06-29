IMAGE="ImageName"
pipeline {
  agent {
    // Using kubernetes cloud to create jenkins agent
    kubernetes {
      // Pod spec for agent. Agent image created using jenkins-agent.Dockerfile
      yaml """
spec:
  containers:
  - image: "krishbharath/jenkins-slave:kustomize"
    imagePullPolicy: Always
    name: "docker"
    command:
      - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-socket
    resources:
      requests:
        cpu: 800m
        memory: 1Gi
      limits:
        cpu: 800m
        memory: 1Gi
  restartPolicy: "Never"
  securityContext: {}
  volumes:
  - name: docker-socket
    hostPath:
      path: /var/run/docker.sock
      """
    }
  }
  parameters {
    choice(name: 'ENVIRONMENT', choices: ['dev', 'prod', 'qa'], description: 'Environment Ex. prod, dev, qa...')
    string(name: 'APP_NAME', defaultValue: 'aiohttp-framework', description: 'Application name')
    string(name: 'BRANCH_NAME', defaultValue: "feature/pipeline_updates", description: 'Deployment branch name')
    booleanParam(name: 'BUILD', defaultValue: false, description: 'Build Image')
    booleanParam(name: 'DEPLOY', defaultValue: false, description: 'Deploy application')
    booleanParam(name: 'PUSH', defaultValue: false, description: 'Push image to repository')
  }
  // environment {
  //   K8S_TOKEN = credentials("k8s-default-token")
  // }
  stages {
    stage ("Checkout") {
      steps {
        container('docker') {
          git branch: env.BRANCH_NAME, credentialsId:'github_creds', url: 'https://github.com/bharath-krishna/aiohttp_framework.git'
          script {
            def gitCommitTag = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
            IMAGE = "docker.io/krishbharath/${params.APP_NAME}:$gitCommitTag"
          }
        }
      }
    }

    stage ("Build") {
      when { expression { env.BUILD == 'true' } }
      steps {
        container('docker') {
          script {
            withCredentials([usernamePassword(credentialsId: 'docker_hub_creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
              sh """
                docker login --username=$DOCKER_USERNAME --password=$DOCKER_PASSWORD
                docker build -t $IMAGE .
              """
              if (env.PUSH == true) {
                sh """
                  docker push $IMAGE
                """
              } else {
                  echo 'Push image skipped due to condition'
              }
            }
          }
        }
      }
    }

    stage ("Deploy") {
      when { expression { env.DEPLOY == 'true' } }
      steps {
        container('docker') {
          script {
            dir("k8s/${params.ENVIRONMENT}") {
              sh """
                kustomize edit set image docker.io/krishbharath/aiohttp-framework=$IMAGE
                kustomize build > resource.yaml
                kubectl apply -f resource.yaml
                kubectl apply -f ingress.yaml
              """
            }
          }
        }
      }
    }


  }
}