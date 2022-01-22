# Setup 

## Requirements
A ready to use GKE Cluster

## Why Spinnaker?
Spinnaker is the easiest way to release complicated pipelines with little-to-no engineering interaction. Originally built by Netflix, Spinnaker has grown to support multiple clouds and a variety of architectures. Where I feel Spinnaker shines though is it’s integration with Kubernetes.

## Install options -> Halyard
Install Options: Halyard vs Helm
There are a few different ways to install Spinnaker, the recommended way being with Halyard, and other options including Helm and deployment manager.
Halyard installs easily on your local machine and remotely connects to the cluster you are running Spinnaker. Now you can install, change settings, and manage your Spinnaker instance from your computer.
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
Spinnaker does not provide persistent Storage persistence storage so it needs to be set up
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
 
## Add GCS Artifact Support
For creating pipelines, Spinnaker needs the ability to connect to GCS to pull Helm charts, YAML files.
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
  
## Google Pub/Sub Trigger with Google Cloud Build  
Now Pipleines should be trigger builds whenever a Cloud Build was complete.
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
  
# Workflow:
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

# Requirements:
- Github Account
- Dockerhub Account
- GCP Account
- Spinnaker
  - needs Dockerhub Account for Trigger/Expected Artifact
  - Kubernetes Cluster Service Account to deploy Images
- Kubernetes
  - Deployment test
  - Deployment production
    

# Learned Lessons: 
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
