# python-flask-sample-cicd

# Docker Build
# docker build -t flask-sample:latest .

# Docker Run
# docker run -ls -p 5000:5000 flask-sample

#Jenkins
# node {
#    stage('Get Source') {
#       // copy source code from local file system and test
#       // for a Dockerfile to build the Docker image
#       git ('https://github.com/sachinbansalnagarro/python-flask-sample-cicd.git')
#       if (!fileExists("Dockerfile")) {
#          error('Dockerfile missing.')
#       }
#    }
#    stage('Build Docker') {
#        // build the docker image from the source code using the BUILD_ID parameter in image name
#          sh "sudo docker build -t flask-sample:latest ."
#    }
#    stage("run docker container"){
#         sh "docker run -ls -p 5000:5000 flask-sample"
#     }
# }
