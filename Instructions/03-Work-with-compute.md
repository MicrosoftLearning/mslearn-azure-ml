---
lab:
    title: 'Work with compute resources in Azure Machine Learning'
---

# Work with compute resources in Azure Machine Learning

One of the key benefits of the cloud is the ability to use scalable, on-demand compute resources for cost-effective processing of large data.

In this exercise, you'll learn how to use cloud compute in Azure Machine Learning to run experiments and production code at scale.

## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free) in which you have administrative-level access.

## Provision an Azure Machine Learning workspace

An Azure Machine Learning *workspace* provides a central place for managing all resources and assets you need to train and manage your models. You can interact with the Azure Machine Learning workspace through the Studio, Python SDK, and Azure CLI. 

You'll use the Azure CLI to provision the workspace and necessary compute, and you'll use the Python SDK to train a classification model with Automated Machine Learning.

### Create the workspace

To create the Azure Machine Learning workspace, you'll use the Azure CLI. All necessary commands are grouped in a Shell script for you to execute.
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
    cd azure-ml-labs/Labs/03
    ./setup.sh
    ```
1. Wait for the script to complete - this typically takes around 5-10 minutes. 

### Create the setup script

To run notebooks within the Azure Machine Learning workspace, you'll need a compute instance. You can use a setup script to configure the compute instance on creation.

1. In the Azure portal, navigate to the Azure Machine Learning workspace named `mlw-dp100-labs`.
1. Select the Azure Machine Learning workspace, and in its **Overview** page, select **Launch studio**. Another tab will open in your browser to open the Azure Machine Learning Studio.
1. Within the Azure Machine Learning Studio, navigate to the **Notebooks** page.
1. In the **Files** pane, select the &#10753; icon to **Add files**. 
1. Select **Create new file**.
1. Verify that the file location is `Users/<your-user-name>`.
1. Change the file type to `Bash (*.sh)`.
1. Change the file name to `compute-setup.sh`.
1. Open the newly created `compute-setup.sh` file and paste the following to its content:

    ```bash
    #!/bin/bash

    # clone repository
    git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git azure-ml-labs-setup
    ```

### Create the compute instance

To create the compute instance, you can use the Studio, Python SDK, or Azure CLI. You'll use the Studio to create the compute instance with the setup script you just created.

1. Navigate to the **Compute** page, using the menu on the left.
1. In the **Compute instances** tab, select **New**.
1. Configure (don't create yet) the compute instance with the following settings: 
    - **Compute name**: *enter a unique name*
    - **Virtual machine type**: CPU
    - **Virtual machine size**: Standard_DS11_v2
1. Select **Next: Advanced settings**.
1. Select **Add schedule** and configure the schedule to **stop** the compute instance every day at `18:00`. 
1. Select **Provision with setup script**, and select the `compute-setup.sh` script you created previously.
    - **Advanced settings**: Note the following settings, but do not select them:
        - **Enable SSH access**: Unselected *(you can use this to enable direct access to the virtual machine using an SSH client)*
        - **Enable virtual network**: Unselected *(you would typically use this in an enterprise environment to enhance network security)*
        - **Assign to another user**: Unselected *(you can use this to assign a compute instance to a data scientist)*
        - **Provision with setup script**: Unselected *(you can use this to add a script to run on the remote instance when created)*
1. **Create** the compute instance and wait for it to start and its state to change to **Running**.

<br>
<details>
<summary><mark>Click to troubleshoot the error: A compute instance with this name already exists.</mark></summary>
If the following message appears in the Azure Cloud Shell:

<code>
Failed to connect to MSI. Please make sure MSI is configured correctly.
Get Token request returned: &lt;Response [400]&gt;
</code>
<br>
Delete the (partially) created compute instance using:
<code>
az ml compute delete "&lt;your-compute-instance-name&gt;"
</code>

And rerun the command to create a compute instance with a different name for your compute. Try adding random numbers after your initials for a more unique name.
</details>

### Create a compute cluster

You'll train multiple models with Automated Machine Learning and compare them to decide which is the *best* (according to your primary metric). To train multiple models at the same time, you'll need a compute cluster with multiple nodes.

1. Use the command to create a compute cluster in your workspace.
    ```azurecli
    az ml compute create --name "aml-cluster" --size STANDARD_DS11_V2 --max-instances 2 --type AmlCompute -w mlw-dp100-labs -g rg-dp100-labs
    ```

## Clone the lab materials

When you've created the workspace and necessary compute resources, you can open the Azure Machine Learning Studio and clone the lab materials. 

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
    git clone https://github.com/MicrosoftLearning/dp100-auto-ml.git dp100-auto-ml
    ``` 
1. When the command has completed, in the **Files** pane, click **&#8635;** to refresh the view and verify that a new **/users/*your-user-name*/dp100-auto-ml** folder has been created. 

## Train a computer vision model with Automated Machine Learning

INSTRUCTIONS HERE

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should **either**:
- Minimize costs by stopping the compute instance if you want to reuse the workspace for other exercises.
- Delete all Azure resources you created.

### Minimize costs and stop the compute instance
1. In Azure Machine Learning studio, on the **Compute** page, select your compute instance.
2. Click **Stop** to stop your compute instance. When it has shut down, its status will change to **Stopped**.

> **Note**: Stopping your compute ensures your subscription won't be charged for compute resources. You will however be charged a small amount for data storage as long as the Azure Machine Learning workspace exists in your subscription.

### Delete all Azure resources you created
1. Close the Azure Machine Learning Studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-labs** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**. 
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
