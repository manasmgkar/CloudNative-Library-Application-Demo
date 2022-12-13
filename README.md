# microservices-library-demo

## Technical Components Used
### Budilding(coding part)
1. Python
2. Flask Library  
3. Jinja2 Library  
4. Requests Libarary  
5. Elasticsearch client libary  

#### Kubernetes Components
1. StatefulSets for ElasticSearch Database
2. Persistant volume,Volume claims for Elastic Database
3. Deployments for Frontend and Backend API pods. 
4. Service(nodeport) to expose frontend,backend,elastic search to each other
5. Configmaps and configmaps mounted as volumes to map the host,port etc of each service.
6. secrets to store amazon ecr tokens
7. Amazon Elastic Container registry to store my docker images in private registry.

## Design Diagram
![8b7ccc0f-0454-4493-9810-d915c61e894d](https://user-images.githubusercontent.com/76769697/207285899-7e541152-c372-46f3-a7de-727da9292906.png)

