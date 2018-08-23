# Flask application starter deployed on AWS Elastic Beanstalk

This project provide a quick way to initiate a running Elastic Beanstalk environment with a Hello World Flask application.

The Gitlab CI/CD is pre-configured with a test and a deploy stage in the .gitlab-ci.yml. After each commit, you will be able to deploy automatically your modification on AWS !

### Steps to deploy the starter Flask app

First fork or clone the project, and set up a [virtualenv](https://virtualenv.pypa.io/en/stable/) with python 3.6.

#### 1 - Installing the Elastic beanstalk CLI on your local machine

```
pip install awsebcli --upgrade --user
```

#### 2 - Setting your AWS credentials on your local machine

If it's the first time you use an AWS command line tool as EB CLI, you have to provide credentials. As AWS recommend, it's better to use a specific IAM user and not your AWS root account. 
[For more information on IAM service.](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)

After you have created an IAM user, you can configure your AWS credentials with this command. It will ask you the `aws-access-id` and `aws-secret-key` (which you can find on the AWS IAM admin page).

```
eb init
```

#### 3 - Setting your AWS credentials as Gitlab variables (optional)

If you want to use Gitlab CD to automatically deploy your modifications, you need to set the AWS credentials as Gitlab variables.

Go to Gitlab > Settings > CI / CD > Variables and create two variables : 

- AWS_ACCESS_KEY_ID (corresponding to the `aws-access-id` provided earlier)

- AWS_SECRET_ACCESS_KEY (corresponding to the `aws-secret-key`)

#### 4 - Create the Elastic Beanstalk environment on AWS

```
eb create flask-env
```

This command will create an Elastic Beanstalk environment associated to your IAM user account. After few minutes, you can see the created environment online on the AWS console (Services > Elastic Beanstalk).

By accessing the URL of the running envionment, the Hello world starter application should be displayed !
