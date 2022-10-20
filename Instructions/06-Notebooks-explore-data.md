---
lab:
    title: 'Ingest and explore data in notebooks'
---

# Ingest and explore data in notebooks

Determining the right algorithm and preprocessing transformations for model training can involve a lot of guesswork and experimentation.

In this exercise, you'll use automated machine learning to determine the optimal algorithm and preprocessing steps for a model by performing multiple training runs in parallel.

## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free) in which you have administrative-level access.

## Provision an Azure Machine Learning workspace

An Azure Machine Learning *workspace* provides a central place for managing all resources and assets you need to train and manage your models. You can interact with the Azure Machine Learning workspace through the Studio, Python SDK, and Azure CLI. 

You'll use the Azure CLI to provision the workspace and necessary compute, and you'll use the Python SDK to train a classification model with Automated Machine Learning.

### Create the workspace and compute resources

To create the Azure Machine Learning workspace, a compute instance, and a compute cluster, you'll use the Azure CLI. All necessary commands are grouped in a Shell script for you to execute.
1. In a browser, open the Azure portal at [http://portal.azure.com](https://portal.azure.com/?azure-portal=true), signing in with your Microsoft account.
1. Select the [>_] (*Cloud Shell*) button at the top of the page to the right of the search box. This opens a Cloud Shell pane at the bottom of the portal.
1. The first time you open the cloud shell, you will be asked to choose the type of shell you want to use (*Bash* or *PowerShell*). Select **Bash**.
1. If you are asked to create storage for your cloud shell, check that the correct subscription is specified and select **Create storage**. Wait for the storage to be created.
1. In the terminal, enter the following commands to clone this repo:
    ```bash
    rm -r azure-ml-labs -f
    git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git azure-ml-labs
    ```
1. After the repo has been cloned, enter the following commands to change to the folder for this lab and run the `setup.sh` script it contains:
    ```bash
    cd azure-ml-labs/Labs/05
    ./setup.sh
    ```
1. When asked, **enter your initials to name your compute instance**. Any random string of letters will do (not more than 5 letters).
1. Wait for the script to complete - this typically takes around 5-10 minutes. 

## Clone the lab materials

When you've created the workspace and necessary compute resources, you can open the Azure Machine Learning Studio and clone the lab materials into the workspace. 

1. In the Azure portal, navigate to the Azure Machine Learning workspace named `mlw-dp100-labs`.
1. Select the Azure Machine Learning workspace, and in its **Overview** page, select **Launch studio**. Another tab will open in your browser to open the Azure Machine Learning Studio.
1. Within the Azure Machine Learning Studio, navigate to the **Compute** page and verify that the compute instance and cluster you created in the previous section exist. The compute instance should be running, the cluster should be idle and have 0 nodes running.
1. In the **Compute instances** tab, find your compute instance, and select the **Terminal** application.
1. In the terminal, install the Python SDK on the compute instance by running the following commands in the terminal:
    ```
    pip uninstall azure-ai-ml
    pip install azure-ai-ml
    ```
1. Run the following command to clone a Git repository containing a notebook, data, and other files to your workspace:
    ```
    git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git azure-ml-labs
    ``` 
1. When the command has completed, in the **Files** pane, click **&#8635;** to refresh the view and verify that a new **/users/*your-user-name*/azure-ml-labs** folder has been created. 

## Train a classification model with automated machine learning

Now that you have all the necessary resources, you can run the notebook to configure and submit the Automated Machine Learning job.

1. Open the **Labs/05/Classification with Automated Machine Learning.ipynb** notebook.
1. Run all cells in the notebook. 

A new job will be created in the Azure Machine Learning workspace. The job tracks the inputs defined in the job configuration, the data asset used, and the outputs like metrics to evaluate the models.

Note that the Automated Machine Learning jobs contains child jobs, which represent individual models that have been trained and other tasks needed to execute. 

3. When the Automate Machine Learning job has completed, explore the job details in the Studio:
    - The **Data guardrails** tab shows whether your training data had any issues.
    - The **Models** tab will show all models that have been trained.
    - Select **View explanation** for the best model to understand which features influenced the target value the most.

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should delete the resources you've created to avoid unnecessary Azure costs.

1. Close the Azure Machine Learning Studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-labs** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**. 
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.