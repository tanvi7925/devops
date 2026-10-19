Exercise-9 : Jenkins multi stage pipeline

Output:

Started by user tanvi
Obtained python-flask-app/Jenkinsfile from git https://github.com/tanvi7925/devops-sample-code
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/py-multistage-pipeline
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/jenkins_home/workspace/py-multistage-pipeline/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/tanvi7925/devops-sample-code # timeout=10
Fetching upstream changes from https://github.com/tanvi7925/devops-sample-code
 > git --version # timeout=10
 > git --version # 'git version 2.47.3'
 > git fetch --tags --force --progress -- https://github.com/tanvi7925/devops-sample-code +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision 499b633dc10af51eba12031abb11afc16366dfe2 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 499b633dc10af51eba12031abb11afc16366dfe2 # timeout=10
Commit message: "Fix Flask and Werkzeug compatibility"
 > git rev-list --no-walk f7b700c28cd4856ce83b8815ecfcaa8e90ca1105 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] echo
Creating virtual environment and installing dependencies...
[Pipeline] sh
+ python3 -m venv venv
+ venv/bin/pip install -r python-flask-app/requirements.txt
Requirement already satisfied: Flask==2.1.2 in ./venv/lib/python3.13/site-packages (from -r python-flask-app/requirements.txt (line 1)) (2.1.2)
Collecting Werkzeug==2.1.2 (from -r python-flask-app/requirements.txt (line 2))
  Downloading Werkzeug-2.1.2-py3-none-any.whl.metadata (4.4 kB)
Requirement already satisfied: Jinja2>=3.0 in ./venv/lib/python3.13/site-packages (from Flask==2.1.2->-r python-flask-app/requirements.txt (line 1)) (3.1.6)
Requirement already satisfied: itsdangerous>=2.0 in ./venv/lib/python3.13/site-packages (from Flask==2.1.2->-r python-flask-app/requirements.txt (line 1)) (2.2.0)
Requirement already satisfied: click>=8.0 in ./venv/lib/python3.13/site-packages (from Flask==2.1.2->-r python-flask-app/requirements.txt (line 1)) (8.5.0)
Requirement already satisfied: MarkupSafe>=2.0 in ./venv/lib/python3.13/site-packages (from Jinja2>=3.0->Flask==2.1.2->-r python-flask-app/requirements.txt (line 1)) (3.0.4)
Downloading Werkzeug-2.1.2-py3-none-any.whl (224 kB)
Installing collected packages: Werkzeug
  Attempting uninstall: Werkzeug
    Found existing installation: Werkzeug 3.1.9
    Uninstalling Werkzeug-3.1.9:
      Successfully uninstalled Werkzeug-3.1.9
Successfully installed Werkzeug-2.1.2
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test)
[Pipeline] echo
Running unit tests...
[Pipeline] sh
+ venv/bin/python -m unittest discover -s python-flask-app -p test*.py -v
test_home (test_app.TestApp.test_home) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.011s

OK
Hello, Jenkins Multi-Stage Pipeline!
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Deploy)
[Pipeline] echo
Preparing application deployment...
[Pipeline] sh
+ mkdir -p /var/jenkins_home/workspace/py-multistage-pipeline/python-app-deploy
+ cp python-flask-app/app.py /var/jenkins_home/workspace/py-multistage-pipeline/python-app-deploy/
+ cp python-flask-app/requirements.txt /var/jenkins_home/workspace/py-multistage-pipeline/python-app-deploy/
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Application)
[Pipeline] echo
Starting Flask application...
[Pipeline] sh
+ [ -f /var/jenkins_home/workspace/py-multistage-pipeline/python-app-deploy/app.pid ]
+ echo 2667
+ sleep 3
+ nohup /var/jenkins_home/workspace/py-multistage-pipeline/venv/bin/python /var/jenkins_home/workspace/py-multistage-pipeline/python-app-deploy/app.py
+ cat /var/jenkins_home/workspace/py-multistage-pipeline/python-app-deploy/app.pid
+ kill -0 2667
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test Application)
[Pipeline] echo
Running application tests...
[Pipeline] sh
+ venv/bin/python -m unittest discover -s python-flask-app -p test*.py -v
test_home (test_app.TestApp.test_home) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.006s

OK
Hello, Jenkins Multi-Stage Pipeline!
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] echo
Pipeline completed successfully!
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
