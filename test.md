# CLC3-Project

## Group 3: Mayer, Wagner, Schichl

## Project Description:
  - Implement a CI/CD pipeline
  
In this Project we will comapare Spinnaker and Tekton CD pipelines and determine which tool works best for deploying an artifact into a two-stage environment. 
The pipeline should be triggered by a git commit to the main branch. The next step should be the construction of a container which is tested in a development stage.
After successfully testing the implementation in the dev stage the container gets released into the production stage. For the conversion from the dev stage to the production
stage we will check which release strategies the tools provide and use the same strategy for each tool.

![image](https://user-images.githubusercontent.com/95210174/150667998-73c6426f-c86a-499d-a3d2-09b1a4dc4986.png)

## Used Technologies:
  - Google Cloud Plattform
  - Kubernetes
  - Spinnaker 
  - Tekton
  - Github
  
## Spinnaker vs Tekton
## Spinnaker
Spinnaker is an open source Continuous Deployment tool that natively
supports deploying applications to major cloud providers like GCP, AWS,
and so on. Spinnaker was jointly developed by Google and Netflix to 
72
accelerate their software delivery. Spinnaker is now open sourced and
its growing community is actively working on new features and taking
the product forward. Major contributors are Google, Netflix, Microsoft,
Amazon, and others. The source code for Spinnaker is available on GitHub
at https://github.com/spinnaker. Spinnaker does not support Continuous
Integration; however, it provides integration with market leader CI tools
like Jenkins.

- Multi-cloud support: Spinnaker supports major cloud
providers like Google, Amazon, and so on.
- Continuous Delivery tool: Spinnaker is a Continuous
Delivery tool, as it deploys applications in a safe and
automated manner.
- Open source: Spinnaker is supported by large
community of developers, including Google, Netflix,
Amazon, and so on.
- Supports major deployment strategies: Spinnaker
supports many deployment strategies, including bluegreen, rolling updates, canary, and highlander with
easy rollbacks.
  
### Architecture 
  
- Deck: A browser-based UI and frontend service for
    Spinnaker.
    
- Gate: An API gateway; all microservices of Spinnaker
   communicate with each other via this gateway.
    
- Orca: An orchestration engine responsible for all ad
   hoc operations. This microservice is also responsible
   for persisting information about pipeline execution.
    
- CloudDriver: Responsible for establishing the
   connection to cloud providers and caching all deployed
   resources. It is the main service for integration with
   cloud providers.
  
- Front50: Responsible for persisting metadata in
  applications, pipelines, projects, and notifications.
  
- Rosco: Responsible for baking immutable VM images,
  such as GCE images, AWS AMI, and so on, that will be
  deployed to a specific cloud. It uses the Packer tool to
  create the VM images.
  
- Igor: Used to connect with CI tools like Jenkins or
  Travis CI. It allows Jenkins/Travis CI stages to be used
  in its own pipeline. Without this service, you could not
  integrate with any CI tool.
  
- Echo: Used for sending the notification through
  Slack, email, or SMS and responsible for all incoming
  WebHooks, like GitHub to Spinnaker.
  
- Fiat: Responsible for user authorization in Spinnaker.
  It is used to query user permissions for application and
  service accounts.
  
- Kayenta: Responsible for automated canary analysis
  for spinnaker.
  
- Halyard: A configuration service for Spinnaker
  that maintains the lifecycle of these services during
  Spinnaker startups, updates, and rollbacks.
  
![image](https://user-images.githubusercontent.com/81319477/146951000-22a390e6-b741-408d-baae-e5f035e35f52.png)

### Application Deployment
Spinnaker is used to perform the Continuous Deployment of an
application through pipelines and stages. Pipelines consist of a sequence
of actions, known as stages, that can be composed in any order. Stages in
turn contain the tasks, which are specific actions.
Spinnaker provides a number of stages, such as deploy, disable,
manual judgment, and many more. Pipelines can be triggered manually
or automatically, based on some events. For example, once Jenkins
builds the code and places the deployable unit, it triggers the Spinnaker
pipeline for deployment. Spinnaker supports widely used cloud-native
deployment strategies, including blue-green, rolling red/black, and Canary
deployments.

The pipeline is the key deployment management construct in Spinnaker. It consists of a sequence of actions, known as stages. You can pass parameters from stage to stage along the pipeline.
You can configure the pipeline to emit notifications, by email, Slack, or SMS, to interested parties at various points during pipeline execution (such as on pipeline start/complete/fail).

Stage
A Stage in Spinnaker is a collection of sequential Tasks and composed Stages that describe a higher-level action the Pipeline will perform either linearly or in parallel. You can sequence stages in a Pipeline in any order, though some stage sequences may be more common than others. Spinnaker provides a number of stages such as Deploy, Resize, Disable, Manual Judgment, and many more.

Task
A Task in Spinnaker is an automatic function to perform in Spinnaker.
  
## Tekton
  
Tekton’s pipeline is designed to run on Kubernetes. It leverages
Kubernetes Custom Resource Definition (CRD), which is used to define
its components like pipelines, tasks, and so on.. CRD is a Kubernetes API
extension to create custom objects and use them like other Kubernetes
objects (such as pods, services, etc.). Once they are installed, Tekton
pipelines are accessible via the Kubernetes CLI (kubectl) and via API calls,
just like pods and other resources called in Kubernetes. These features
make Tekton well integrated with the overall Kubernetes system
  
Tekton is
an open source framework especially designed for cloud-native CI/CD
implementation.
It was initially developed by Google for Kubernetes-native based
software build and deployment. In 2018, the Tekton project was donated to
the Continuous Delivery Foundation. Since then, the CDF has taken over
responsibility for new features and enhancement.
Tekton is based on Kubernetes-native principles, which allows
developers to build, test, and deploy cloud-native, containerized
applications across multiple cloud providers. Kubernetes environments
include AWS Elastic Kubernetes Services, Google Kubernetes Service, and
hybrid environments.


Tekton has four core components:
- Tekton pipelines: This component defines the basic
building blocks (pipeline and task) of CI/CD workflow.
- Triggers: Triggering events for a CI/CD workflow.
- CLI: A command-line interface for CI/CD workflow
management.
- Dashboard: A web-based UI for pipeline management.

### Architecture

![image](https://user-images.githubusercontent.com/81319477/146953959-2adb5a0c-2869-4c0e-b2af-1cac8c625b56.png)
  
Tekton pipeline flow diagram:
![image](https://user-images.githubusercontent.com/81319477/146955366-12c96acb-1bea-45fc-a02b-8dee15328add.png)

Tekton’s pipeline is designed to run on Kubernetes. It leverages
Kubernetes Custom Resource Definition (CRD), which is used to define
its components like pipelines, tasks, and so on. CRD is a Kubernetes API
extension to create custom objects and use them like other Kubernetes
objects (such as pods, services, etc.). Once they are installed, Tekton
pipelines are accessible via the Kubernetes CLI (kubectl) and via API calls,
just like pods and other resources called in Kubernetes. These features
make Tekton well integrated with the overall Kubernetes system.
  
#### Steps
  
A step is the smallest operation of the Tekton pipeline. It performs a
specific function in CI/CD, such as managing workflow, compiling
code, running the unit testing, building and pushing the Docker image,
and so on.
  
#### Tasks
  
A task is a collection of steps and these steps execute in a particular
sequence defined by the user. Tasks execute
in the form of Kubernetes pods in the K8 cluster and steps run as a
container within the same pod. In a task, we can also provide the shared
environment information that is accessible to all the steps running in the
same pod. We can mount secrets in a Tekton task, which will be accessible
to every step defined within the same Tekton task.
  
#### Pipelines
  
Pipelines define the set of tasks to be executed in order. Pipelines are
stateless, reusable, and parameterized. In a nutshell, Tekton creates several
pods based on the task and ensures all the pods are running successfully
as desired. Pipelines can execute the tasks on different Kubernetes nodes.
Pipelines are executed in the following order:
  
- Sequential
  
- Concurrently
  
- Direct acyclic graph
  
#### Pipeline Resource (Input/Output Resources)
  
The Pipeline resource component defines objects that could be used
as input or output in the pipeline or tasks. For example, pipeline/task
requires the Git repository location as an input to fetch the latest code and
provide container images as output.
Tekton supports many types of resources.
  
- Git: A Git repository
  
- Pull request: A specific pull request in a Git repository
  
- Image: A container image
  
- Cluster: A Kubernetes cluster
  
#### TaskRuns and PipelineRuns
  
A PipelineRun is responsible for executing a pipeline on specific events
and passing the required execution parameters, input, and output to the
pipeline.
Similarly, TaskRuns are specific triggering points of the task.
TaskRuns and PipelineRuns connect resources with tasks and pipelines.
You can create TaskRuns and PipelineRuns manually or automatically to
trigger the task and pipeline immediately or at a specific time


## Milestones:
  1. Compare Spinnaker and Tekton
  2. Setup Continous Intergration (Jenkins/Git Actions/Google Cloud Build & Dockerhub)
  3. Setup Spinnaker
  4. Setup Kubernetes
  5. Setup Tekton
  6. Setup Continous Delivery Pipelines
  7. Create Automated Testing
  8. Create Demo: Successful CD
  9. Create Demo: Failing CD

## Responsibilities:
  1. All
  2. Wagner
  3. Wagner
  4. Schichl
  5. Schichl
  6. Mayer
  7. Mayer
  8. All
  9. All

# Working on the Project
## Why use Spinnaker instead of Tekton
We choose to work with spinnaker casue it soooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo MUCH BETTER:



## Setup Google Cloud Build for Git
To start things of we started with the CI and implemented Git/Jenkins and Google Cloud Build to have more options. Finally we settled on Google Cloud Build for our final solution.


A build config file in Google Cloud Build contains instructions for Cloud Build to perform tasks based on your specifications. For example, your build config file can contain instructions to build, package, and push Docker images.

### Structure of a build config file
A build config file has the following structure:
```
steps:
- name: string
  args: [string, string, ...]
  env: [string, string, ...]
  dir: string
  id: string
  waitFor: [string, string, ...]
  entrypoint: string
  secretEnv: string
  volumes: object(Volume)
  timeout: string (Duration format)
- name: string
  ...
- name: string
  ...
timeout: string (Duration format)
queueTtl: string (Duration format)
logsBucket: string
options:
 env: [string, string, ...]
 secretEnv: string
 volumes: object(Volume)
 sourceProvenanceHash: enum(HashType)
 machineType: enum(MachineType)
 diskSizeGb: string (int64 format)
 substitutionOption: enum(SubstitutionOption)
 dynamicSubstitutions: boolean
 logStreamingOption: enum(LogStreamingOption)
 logging: enum(LoggingMode)
 pool: object(PoolOption)
substitutions: map (key: string, value: string)
tags: [string, string, ...]
serviceAccount: string
secrets: object(Secret)
availableSecrets: object(Secrets)
artifacts: object (Artifacts)
images:
- [string, string, ...]
```

### Build steps
A build step specifies an action that you want Cloud Build to perform. For each build step, Cloud Build executes a docker container as an instance of docker run. Build steps are analogous to commands in a script and provide you with the flexibility of executing arbitrary instructions in your build. If you can package a build tool into a container, Cloud Build can execute it as part of your build. By default, Cloud Build executes all steps of a build serially on the same machine. If you have steps that can run concurrently, use the waitFor option.

You can include up to 100 build steps in your config file.

Use the steps field in the build config file to specify a build step. Here's a snippet of the kind of configuration you might set in the steps field:
```
steps:
- name: 'gcr.io/cloud-builders/kubectl'
  args: ['set', 'image', 'deployment/mydepl', 'my-image=gcr.io/my-project/myimage']
  env:
  - 'CLOUDSDK_COMPUTE_ZONE=us-east4-b'
  - 'CLOUDSDK_CONTAINER_CLUSTER=my-cluster'
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/my-project-id/myimage', '.']
```

For futher Information pls visit
https://cloud.google.com/build/docs/build-config-file-schema
  
  
## Setup Spinnaker

### Requirements
GCP Account

A ready to use GKE Cluster

## Why Spinnaker?
Spinnaker is the easiest way to release complicated pipelines with little-to-no engineering interaction. Originally built by Netflix, Spinnaker has grown to support multiple clouds and a variety of architectures. Where I feel Spinnaker shines though is it’s integration with Kubernetes.

## Install options -> Halyard
There are a few different ways to install Spinnaker, the recommended way being with Halyard, and other options including Helm and deployment manager.
As Halyard was recommended this option is used. Halyard installs easily and remotely connects to the cluster you are running Spinnaker.
```
#get the lastest Halyard release
curl -O https://raw.githubusercontent.com/spinnaker/halyard/master/install/debian/InstallHalyard.sh
#start the installation
sudo bash InstallHalyard.sh
#Check whether Halyard was installed properly
hal -v
```
After installation, you are able to change settings, and manage your Spinnaker instance from your computer.
The first step after installing Halyard is to connect Halyard to your Kubernetes Cluster so you can install Spinnaker. GCP does require that you provide a Service Account to Halyard with the needed permissions to access your Cluster. To do this access GCP is needed,  and then must be provided to Halyard. 

```
# login into GCP
gcloud auth login
# set project id that your cluster belongs to
gcloud config set project <your-gcp-project-id>
# login to kubectl
gcloud auth application-default login
# download kubeconfig to local computer from a cluster by name
gcloud container clusters get-credentials <your-cluster-name> --zone <your-cluster-zone>
# get kubeconfig context
CONTEXT=$(kubectl config current-context)
kubectl apply --context $CONTEXT -f https://spinnaker.io/downloads/kubernetes/service-account.yml
# get service token
TOKEN=$(kubectl get secret --context $CONTEXT \
   $(kubectl get serviceaccount spinnaker-service-account \
       --context $CONTEXT \
       -n spinnaker \
       -o jsonpath='{.secrets[0].name}') \
   -n spinnaker \
   -o jsonpath='{.data.token}' | base64 --decode)
# set credentials
kubectl config set-credentials ${CONTEXT}-token-user --token $TOKEN
# set context
kubectl config set-context $CONTEXT --user ${CONTEXT}-token-user
# enable kubernetes
hal config provider kubernetes enable
# add in provider account
hal config provider kubernetes account add spinnaker-account --provider-version v2 --context ${CONTEXT}
# finally enable artifacts
hal config features edit --artifacts true
```  
  
Now deploy Spinnaker to the Kubernetes cluster and and customize your installation.
```
# set the account to install spinnaker into
$ACCOUNT=spinnaker-account
# install spinnaker
hal config deploy edit --type distributed --account-name $ACCOUNT
```
  
## Enable Google Cloud Storage  
Spinnaker does not provide persistence storage so it needs to be set up.
Create another Service Account that includes permissions to edit Google Cloud Storage buckets and then enable GCS.

```
SERVICE_ACCOUNT_NAME=spinnaker-gcs-account
SERVICE_ACCOUNT_DEST=~/.gcp/gcs-account.json
# create service account
gcloud iam service-accounts create \
    $SERVICE_ACCOUNT_NAME \
    --display-name $SERVICE_ACCOUNT_NAME
# set service account email
SA_EMAIL=$(gcloud iam service-accounts list \
    --filter="displayName:$SERVICE_ACCOUNT_NAME" \
    --format='value(email)')
# set project
PROJECT=$(gcloud info --format='value(config.project)')
# bind iam policy
gcloud projects add-iam-policy-binding $PROJECT \
    --role roles/storage.admin --member serviceAccount:$SA_EMAIL
mkdir -p $(dirname $SERVICE_ACCOUNT_DEST)
# create service account keys
gcloud iam service-accounts keys create $SERVICE_ACCOUNT_DEST --iam-account $SA_EMAIL
# see https://cloud.google.com/storage/docs/bucket-locations
BUCKET_LOCATION=us
# set configuration
hal config storage gcs edit --project $PROJECT \
    --bucket-location $BUCKET_LOCATION \
    --json-path $SERVICE_ACCOUNT_DEST
# enable gcs
hal config storage edit --type gcs
# deploy all your changes
hal deploy apply
```
 
### Add GCS Artifact Support
For creating pipelines, Spinnaker needs the ability to connect to GCS to pull Helm charts and YAML files.
```
# service account from earlier
SERVICE_ACCOUNT_DEST=~/.gcp/gcs-artifacts-account.json
# artifact account name
ARTIFACT_ACCOUNT_NAME=my-gcs-artifact-account
# enable artifact support if you didn't already
hal config features edit --artifacts true
# enable gcs artifact support
hal config artifact gcs account add $ARTIFACT_ACCOUNT_NAME \
    --json-path $SERVICE_ACCOUNT_DEST
hal config artifact gcs enable
# deploy your changes
hal deploy apply
```
  
### Google Pub/Sub Trigger with Google Cloud Build  
Now Pipleines should trigger builds whenever a Cloud Build was complete.
```
#!/usr/bin/env bash

echo "start editing cloud build"
SERVICE_ACCOUNT_NAME=spinnaker-account
SERVICE_ACCOUNT_DEST=~/.gcp/gcs-account.json
PROJECT=$(gcloud info --format='value(config.project)')
SUBSCRIPTION_NAME=cloud-builds

gcloud pubsub subscriptions create ${SUBSCRIPTION_NAME} \
    --topic projects/${PROJECT}/topics/cloud-builds \
    --project ${PROJECT}

hal config pubsub google subscription add $SUBSCRIPTION_NAME \
    --project ${PROJECT} \
    --subscription-name ${SUBSCRIPTION_NAME} \
    --message-format GCB

hal config pubsub google enable

hal deploy apply

echo "done editing cloud build"
 ``` 
  
Now whenever Cloud Build completes a build the resulting pubsub message will be picked up by Spinnaker and can be used as a trigger pipelines.
  
## Workflow:
- Commit on main branch 
- CI
  - Trigger on Google Cloud Build 
    - Triggered by commit to main branch
  - Building Docker Image
    - cloudbuild.yaml defines several steps
      - unittest
      - build-image
      - docker-login (with credentials from SecretManager)
      - image tagging
      - push image to Dockerhub
- CD
  - Trigger on Docker Registry
  - Expected Artifact: last pushed Docker Image
  - Pipeline Run:
    - Deploy Image to deployment test
    - Manual Judgement - Does new Image run on test deployment?
    - Deploy Image to deployment production
- Replicas Updated with Recreate strategy 
  (instead of Rollout/Ramped because of demo)

## Requirements:
- Github Account
- Dockerhub Account
- GCP Account
- Spinnaker
  - needs Dockerhub Account for Trigger/Expected Artifact
  - Kubernetes Cluster Service Account to deploy Images
- Kubernetes
  - Deployment test
  - Deployment production
    

## Learned Lessons: 
- Getting Data to Spinnaker is difficult
- Need Service Accounts for everything
- Intended Implementations/Usages
  - Intended Usage I: 
    - GCB (Google Cloud Build) creates Image
    - Trigger on finished Image Build (PUB/SUB)
    - Spinnaker gets Image as Expected Artifact
    - Pipeline runs...
  - Difficulties I:
    - Couldn't find out how to create PUB/SUB messages on finished Build
    - Getting the subscriptions into Spinnaker
    - hal deploy apply - Spinnaker deployment did not change
  - Intended Usage II: 
    - GCB creates Image and pushes to GCR (Google Container Registry)
    - Trigger on Image Push to GCR
    - Spinnaker gets Image as Expected Artifact
    - Pipeline runs...
  - Difficulties II:
    - Couldn't find out how to trigger Pipeline on Image push to GCR
    - No Image as Expected Artifact
    - Would not be able to Patch Manifest
- Difference between Deploying and Patching a Manifest
