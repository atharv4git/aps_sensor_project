# aps-fault-detection
### Using:
* python
* mongodb
* numpy

### The training pipileine
Training pipelines let you perform custom machine learning (ML) training and automatically create a Model resource based on your training output.
![](https://iili.io/HBI89l2.png)

#### Data Ingetion:
Data ingestion is the process of obtaining and importing data for immediate use or storage in a database. To ingest something is to take something in or absorb something. Data can be streamed in real time or ingested in batches. In real-time data ingestion, each data item is imported as the source emits it.

In data ingestion we create three datasets:
1. training dataset
2. testing dataset
3. validation dataset

### Data Validation:
Data validation refers to the process of ensuring the accuracy and quality of data. It is implemented by building several checks into a system or report to ensure the logical consistency of input and stored data. In automated systems, data is entered with minimal or no human supervision.

### Data Transformation:
Data transformation is the process of converting data from one format to another, typically from the format of a source system into the required format of a destination system. Data transformation is a component of most data integration and data management tasks, such as data wrangling and data warehousing.

### Model Trainer:
Model training is the phase in the data science development lifecycle where practitioners try to fit the best combination of weights and bias to a machine learning algorithm to minimize a loss function over the prediction range.

### Model Evaluation:
Model evaluation is the process of using different evaluation metrics to understand a machine learning model's performance, as well as its strengths and weaknesses. Model evaluation is important to assess the efficacy of a model during initial research phases, and it also plays a role in model monitoring.

### Model Pusher:
The Pusher component is used to push a validated model to a deployment target during model training or re-training. Before the deployment, Pusher relies on one or more blessings from other validation components to decide whether to push the model or not.

* Evaluator blesses the model if the new trained model is "good enough" to be pushed to production.
* (Optional but recommended) InfraValidator blesses the model if the model is mechanically servable in a production environment.

A Pusher component consumes a trained model in SavedModel format, and produces the same SavedModel, along with versioning metadata.

> ML pipilenes can be made totally by scratch or some available services/softwares can be used such as:
>* [TFX](https://www.tensorflow.org/tfx)
>* [Apache Spark ML](https://spark.apache.org/docs/1.6.1/ml-guide.html)
>* [Amazon Sagemakes Pipelines](https://aws.amazon.com/sagemaker/pipelines/?tag=mochaglobal20-20)
>* [Azure ML Pipelines](https://learn.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines)

### Run it yourself:
```
python setup.py
```
