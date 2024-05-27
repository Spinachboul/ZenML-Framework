<h3>Goal</h3>
This readme aims to provide an overview of how to deploy ML pipelines on cloud using ZenML open-source package

<h3>Project Description</h3>
This is a simple binary classification of whether the patient is suffering from heart attack or not

<h3>Getting Started</h3>

<h4> Pre-requisites</h4>
1. Python version (3.7+) <br>
2. ZenML package <code> pip install zenml </code> <br>
3. (Optional) Additional dependencies specific to the application (eg. Scikit-learn, pandas, numpy , tensorflow)

<h4> Installation</h4>
No installation step typically required required for getting started

<h4> Initializing the server</h4>
We need to first initialie the ZenML server before getting into the coding part using <code> zenml up </code>

<h4> Execute the main ZenML pipeline </h4>
<code> python run_pipeline.py </code> (Optional) Specify the environment variables and command line arguements

<h4>Pipeline Steps </h4>
<ul>
  <li> Data Ingestion</li>
  <li> Data Cleaning</li>
  <li> Model Training</li>
  <li> Model Validation</li>
  <li> (Optional) Model Deployment </li>
</ul>

<h4> Configuration</h4>
Describe (or) specify any configurations which are peculiar to the ML application
This could be:
<ul>
  <li> Environment variables used for pipeline settings</li>
  <li> Command line arguements for fine tuning specific tests </li>
</ul>

<h4> Documentation</h4>
Include links to any specific documentation relevant to the application.




