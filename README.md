# CLC3-Project

## Group 3: Mayer, Wagner, Schichl

## Project Description:
  - Implement your own CD pipeline 
We will set up Spinnaker and Tekton CD pipelines and compare which tool works best for our deploying an artifact into a two-stage environment. The pipeline should be triggered by a git commit to the main branch. The next step should be the construction of an container which is tested in a development stage. After successfully testing the implementation in the dev stage the container gets released into the development stage. For the conversion from the dev stage to the development stage we will check which release strategies the tools provide and use the same strategy for each tool.

### Architecture

## Used Technologies:
  - Kubernetes
  - Spinnaker 
    - is an open source, multi-cloud continuous delivery platform for releasing software changes with high velocity and confidence
    - used rather with the GUI than with a CLI
    - allows use with Azure, GCP, AWS, ...
    - is no Build-Server - so third-party build tools are used
  - Tekton 
    - provides k8s-style resources for declaring CI/CD-style pipelines
    - uses Tasks, Pipelines, TaskRuns, PipelineRuns and PipelineResources
    - Pipelines consist of Tasks which contain Steps (basically Shell-Commands) 
    - huge amount of possibilities - a lot to figure out by yourself
  - Github

## Milestones:
  1. Compare Spinnaker and Tekton
  2. Setup Continous Intergration
  3. Setup Spinnaker
  4. Setup Tekton
  5. Setup Continous Delivery Pipelines
  6. Create Automated Testing
  7. Create Demo: Successful CD
  8. Create Demo: Failing CD

## Responsibilities:
  1. All
  2. Wagner
  3. Schichl
  4. Schichl
  5. Mayer
  6. All
  7. All
