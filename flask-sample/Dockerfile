FROM python:3.7-slim-stretch AS base
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "app/app.py" ]


# docker build -t flask-sample:latest .

# docker run -ls -p 5000:5000 flask-sample


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