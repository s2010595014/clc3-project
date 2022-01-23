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
  
## Spinnaker vs Tekton
### Spinnaker
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
  
 #### Architecture 
  
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

#### Application Deployment
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
  
### Tekton
  
Tekton’s pipeline is designed to run on Kubernetes. It leverages
Kubernetes Custom Resource Definition (CRD), which is used to define
its components like pipelines, tasks, and so on.. CRD is a Kubernetes API
extension to create custom objects and use them like other Kubernetes
objects (such as pods, services, etc.). Once they are installed, Tekton
pipelines are accessible via the Kubernetes CLI (kubectl) and via API calls,
just like pods and other resources called in Kubernetes. These features
 make Tekton well integrated with the overall Kubernetes system
  
#### Architercture:
  
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
  
![image](https://user-images.githubusercontent.com/81319477/146953959-2adb5a0c-2869-4c0e-b2af-1cac8c625b56.png)
  
Tekton pipeline flow diagram:
![image](https://user-images.githubusercontent.com/81319477/146955366-12c96acb-1bea-45fc-a02b-8dee15328add.png)


Tekton has four core components:
- Tekton pipelines: This component defines the basic
building blocks (pipeline and task) of CI/CD workflow.
- Triggers: Triggering events for a CI/CD workflow.
- CLI: A command-line interface for CI/CD workflow
management.
- Dashboard: A web-based UI for pipeline management.

#### Tekton’s Pipeline Architecture

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
