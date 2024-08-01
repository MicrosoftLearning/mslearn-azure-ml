---
lab:
    title: 'Train a model with the Azure Machine Learning Designer'
---

# Train a model with the Azure Machine Learning Designer

Azure Machine Learning Designer provides a drag and drop interface with which you can define a workflow. You can create a workflow to train a model, testing and comparing multiple algorithms with ease.

In this exercise, you'll use the Designer to quickly train and compare two classification algorithms.

## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free?azure-portal=true) in which you have administrative-level access.

## Provision an Azure Machine Learning workspace

An Azure Machine Learning *workspace* provides a central place for managing all resources and assets you need to train and manage your models. You can interact with the Azure Machine Learning workspace through the studio, Python SDK, and Azure CLI.

You'll use a Shell script which uses the Azure CLI to provision the workspace and necessary resources. Next, you'll use the Designer in the Azure Machine Learning studio to train and compare models.

### Create the workspace and compute cluster

To create the Azure Machine Learning workspace and a compute cluster, you'll use the Azure CLI. All necessary commands are grouped in a Shell script for you to execute.

1. In a browser, open the Azure portal at `https://portal.azure.com/`, signing in with your Microsoft account.
1. Select the \[>_] (*Cloud Shell*) button at the top of the page to the right of the search box. This opens a Cloud Shell pane at the bottom of the portal.
1. Select **Bash** if asked. The first time you open the cloud shell, you will be asked to choose the type of shell you want to use (*Bash* or *PowerShell*).
1. Check that the correct subscription is specified and that **No storage account required** is selected. Select **Apply**.
1. In the terminal, enter the following commands to clone this repo:

    ```azurecli
    rm -r azure-ml-labs -f
    git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git azure-ml-labs
    ```

    > Use `SHIFT + INSERT` to paste your copied code into the Cloud Shell.

1. After the repo has been cloned, enter the following commands to change to the folder for this lab and run the setup.sh script it contains:

    ```azurecli
    cd azure-ml-labs/Labs/05
    ./setup.sh
    ```

    > Ignore any (error) messages that say that the extensions were not installed.

1. Wait for the script to complete - this typically takes around 5-10 minutes.

## Configure a new pipeline

When you've created the workspace and necessary compute cluster, you can open the Azure Machine Learning studio and create a training pipeline with the Designer.

1. In the Azure portal, navigate to the Azure Machine Learning workspace named **mlw-dp100-...**.
1. Select the Azure Machine Learning workspace, and in its **Overview** page, select **Launch studio**. Another tab will open in your browser to open the Azure Machine Learning studio.
1. Close any pop-ups that appear in the studio.
1. Within the Azure Machine Learning studio, navigate to the **Compute** page and verify that the compute cluster you created in the previous section exist. The cluster should be idle and have 0 nodes running.
1. Navigate to the **Designer** page.
1. Select the **Custom** tab at the top of the page.
1. Create a new empty pipeline using custom components.
1. Change the default pipeline name (**Pipeline-Created-on-*date***) to `Train-Diabetes-Classifier` by selecting the pencil icon on its right.


## Create a new pipeline

To train a model, you'll need data. You can use any data stored in a datastore or use a publicly accessible URL.

1. In the left menu, select the **Data** tab.
1. Drag and drop the **diabetes-folder** component to the canvas.

    Now that you have your data, you can continue by creating a pipeline using custom components that already exist within the workspace (were created for you during setup).

1. In the left menu, select the **Components** tab.
1. Drag and drop the **Remove Empty Rows** component on to the canvas, below the **diabetes-folder**.
1. Connect the output of the data to the input of the new component.
1. Drag and drop the **Normalize Numerical Columns** component on to the canvas, below the **Remove Empty Rows**.
1. Connect the output of the previous component to the input of the new component.
1. Drag and drop the **Train a Decision Tree Classifier Model** component on to the canvas, below the **Normalize Numerical Columns**.
1. Connect the output of the previous component to the input of the new component.
1. Select **Configure & Submit** and in the **Set up pipeline job** page create a new experiment and name it `diabetes-designer-pipeline`, then select **Next**.
1. On the **Inputs & Outputs** make no changes and select **Next**.
1. On the **Runtime settings** select **Compute Cluster**, and under the **Select Azure ML compute cluster** select your *aml-cluster*.
1. Select **Review + Submit** and then select **Submit** to start the pipeline run.
1. You can check the status of the run by going to the **Pipelines** page and selecting the **Train-Diabetes-Classifier** pipeline.
1. Wait until all components have successfully completed.

    Submitting the job will initialize the compute cluster. As the compute cluster was idle up until now, it may take some time for the cluster to resize to more than 0 nodes. Once the cluster has resized, it will automatically start running the pipeline.

You'll be able to track the run of each component. When the pipeline fails, you'll be able to explore which component failed and why it failed. Error messages will show in the **Outputs + logs** tab of the job overview.

## Train a second model to compare

To compare between algorithms and evaluate which performs better, you can train two models within one pipeline and compare.

1. Return to the **Designer** and select the **Train-Diabetes-Classifier** pipeline draft.
1. Add the **Train a Logistic Regression Classifier Model** component to the canvas, next to the other training component.
1. Connect the output of the **Normalize Numerical Columns** component to the input of the new training component.
1. At the top, select **Configure & Submit**.
1. On the **Basics** page, create a new experiment named `designer-compare-classification`, and run it.
1. Select **Review + Submit** and then select **Submit** to start the pipeline run.
1. You can check the status of the run by going to the **Pipelines** page and selecting the **Train-Diabetes-Classifier** pipeline with the **designer-compare-classification** experiment.
1. Wait until all components have successfully completed.  
1. Select **Job overview**, then select the **Metrics** tab to review the results for both training components.
1. Try and determine which model performed better.

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should delete the resources you've created to avoid unnecessary Azure costs.

1. Close the Azure Machine Learning studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-...** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**.
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
