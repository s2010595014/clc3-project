# Workflow:
- Commit on main branch 
- Trigger on Google Cloud Build 
- Building Docker Image
- Push Image to Google Cloud Registry
- (PubSub message to Spinnaker Trigger)
- Deploy Image to Cluster
- Manual Judgement
- Deploy Image to Cluster
