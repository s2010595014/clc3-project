# CLC3-Project

## Group 3: Mayer, Wagner, Schichl

## Project Description:
  - Implement a CD pipeline
  
We will set up Spinnaker and Tekton CD pipelines and compare which tool works best for deploying an artifact into a three-stage environment. The pipeline should be triggered by a git commit to the main branch. The next step should be the construction of an container which is tested in a development stage. After successfully testing the implementation in the dev stage the container gets released into the producution stage. For the conversion from the dev stage to the development stage we will check which release strategies the tools provide and use the same strategy for each tool.

![image](https://user-images.githubusercontent.com/81319477/146958129-4aecda4a-e860-414d-a431-1a2034881d7e.png)

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
  - Jenkins

## Architecture
  ### Spinnaker
  ![image](https://user-images.githubusercontent.com/81319477/146951000-22a390e6-b741-408d-baae-e5f035e35f52.png)
  
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
  
  ### Tekton
  
  Tekton’s pipeline is designed to run on Kubernetes. It leverages
  Kubernetes Custom Resource Definition (CRD), which is used to define
  its components like pipelines, tasks, and so on.. CRD is a Kubernetes API
  extension to create custom objects and use them like other Kubernetes
  objects (such as pods, services, etc.). Once they are installed, Tekton
  pipelines are accessible via the Kubernetes CLI (kubectl) and via API calls,
  just like pods and other resources called in Kubernetes. These features
  make Tekton well integrated with the overall Kubernetes system
  
  Tektons pipeline architercture:
  ![image](https://user-images.githubusercontent.com/81319477/146953959-2adb5a0c-2869-4c0e-b2af-1cac8c625b56.png)
  
  Tekton pipline flow diagram:
  ![image](https://user-images.githubusercontent.com/81319477/146955366-12c96acb-1bea-45fc-a02b-8dee15328add.png)
  
  #### Steps
  
  A step is the smallest operation of the Tekton pipeline. It performs a
  specific function in CI/CD, such as managing workflow, compiling
  code, running the unit testing, building and pushing the Docker image,
  and so on
  
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
  Tekton supports many types of resources (a few of them are mentioned
  in Figure 4-5):
  
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
  2. Setup Continous Intergration (Jenkins/Git Actions & Dockerhub)
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
