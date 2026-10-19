Exercise-8: Jenkins Hello World Job

Output:

Started by user tanvi
Running as SYSTEM
Building in workspace /var/jenkins_home/workspace/helloworld
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/jenkins_home/workspace/helloworld/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/tanvi7925/devops-sample-code # timeout=10
Fetching upstream changes from https://github.com/tanvi7925/devops-sample-code
 > git --version # timeout=10
 > git --version # 'git version 2.47.3'
 > git fetch --tags --force --progress -- https://github.com/tanvi7925/devops-sample-code +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision 48175e72037c41ed9559d200643fce3278fb72c2 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 48175e72037c41ed9559d200643fce3278fb72c2 # timeout=10
Commit message: "Merge branch 'main' of https://github.com/tanvi7925/devops-sample-code"
First time build. Skipping changelog.
[helloworld] $ /bin/sh -xe /tmp/jenkins8432703784610194987.sh
+ sh hello-world.sh
Hello, Jenkins!
Finished: SUCCESS
