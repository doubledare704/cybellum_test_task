# How to run project locally with docker-compose?
* Open terminal and locate cwd in root of repo
* ```docker-compose up -d``` to deploy postgresql and flask app in docker

# How to install deps for a project?
* src folder contains requirements.txt
* ```pip install -r requirements.txt```

# How to test endpoints (GET) from browser?
* After deployemnt with docker open ```http://localhost:8000/posts``` to heck list of posts
* If there are no posts you need to create them, but POST endpoints checks Authorization header.

# How to pass authorization?
* For test purpose I've added ```test_endpoints.http``` file, as [http client in pycharm](https://www.jetbrains.com/help/pycharm/http-client-in-product-code-editor.html)
* Create user: need to ```POST http://localhost:8000/users``` with parameters as in file.
* Login: make a ```POST http://localhost:8000/login``` with username and password from previous step. In return you will have access token

# How to pass Authorization header check?
* Obtain access token from prev step and add ```Authorization: Bearer {your_jwt}``` to the request headers.

