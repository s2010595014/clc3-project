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
