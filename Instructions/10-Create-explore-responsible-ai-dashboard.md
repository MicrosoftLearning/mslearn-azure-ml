---
lab:
    title: 'Create and explore the Responsible AI dashboard'
---

# Create and explore the Responsible AI dashboard

After you train your model, you'll want to evaluate your model to explore whether it's performing as expected. Next to performance metrics, there are other factors you can take into consideration. The Responsible AI dashboard in Azure Machine Learning allows you to analyze the data and the model's predictions to identify any bias or unfairness.

In this exercise, you'll prepare your data and create a Responsible AI dashboard in Azure Machine Learning.

## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free?azure-portal=true) in which you have administrative-level access.

## Provision an Azure Machine Learning workspace

An Azure Machine Learning *workspace* provides a central place for managing all resources and assets you need to train and manage your models. You can interact with the Azure Machine Learning workspace through the studio, Python SDK, and Azure CLI.

You'll use the Azure CLI to provision the workspace and necessary compute, and you'll use the Python SDK to run a command job.

### Create the workspace and compute resources

To create the Azure Machine Learning workspace, a compute instance, and a compute cluster, you'll use the Azure CLI. All necessary commands are grouped in a Shell script for you to execute.

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

1. After the repo has been cloned, enter the following commands to change to the folder for this lab and run the **setup.sh** script it contains:

    ```azurecli
    cd azure-ml-labs/Labs/10
    ./setup.sh
    ```

    > Ignore any (error) messages that say that the extensions were not installed.

1. Wait for the script to complete - this typically takes around 5-10 minutes.

    <details>
    <summary><b>Troubleshooting tip</b>: Workspace creation error</summary><br>
    <p>If you receive an error when running the setup script through the CLI, you need to provision the resources manually:</p>
    <ol>
        <li>In the Azure portal home page, select <b>+ Create a resource</b>.</li>
        <li>Search for <i>machine learning</i> and then select <b>Azure Machine Learning</b>. Select <b>Create</b>.</li>
        <li>Create a new Azure Machine Learning resource with the following settings:
            <ul>
                <li><b>Subscription</b>: <i>Your Azure subscription</i></li>
                <li><b>Resource group</b>: rg-dp100-labs</li>
                <li><b>Workspace name</b>: mlw-dp100-labs</li>
                <li><b>Region</b>: <i>Select the geographical region closest to you</i></li>
                <li><b>Storage account</b>: <i>Note the default new storage account that will be created for your workspace</i></li>
                <li><b>Key vault</b>: <i>Note the default new key vault that will be created for your workspace</i></li>
                <li><b>Application insights</b>: <i>Note the default new application insights resource that will be created for your workspace</i></li>
                <li><b>Container registry</b>: None (<i>one will be created automatically the first time you deploy a model to a container</i>)</li>
            </ul>
        <li>Select <b>Review + create</b> and wait for the workspace and its associated resources to be created - this typically takes around 5 minutes.</li>
        <li>Select <b>Go to resource</b> and in its <b>Overview</b> page, select <b>Launch studio</b>. Another tab will open in your browser to open the Azure Machine Learning studio.</li>
        <li>Close any pop-ups that appear in the studio.</li>
        <li>Within the Azure Machine Learning studio, navigate to the <b>Compute</b> page and select <b>+ New</b> under the <b>Compute instances</b> tab.</li>
        <li>Give the compute instance a unique name and then select <b>Standard_DS11_v2</b> as the virtual machine size.</li>
        <li>Select <b>Review + create</b> and then select <b>Create</b>.</li>
        <li>Next, select the <b>Compute clusters</b> tab and select <b>+ New</b>.</li>
        <li>Choose the same region as the one where you created your workspace and then select <b>Standard_DS11_v2</b> as the virtual machine size. Select <b>Next</b></li>
        <li>Give the cluster a unique name and then select <b>Create</b>.</li>
    </ol>
    </details>

## Clone the lab materials

When you've created the workspace and necessary compute resources, you can open the Azure Machine Learning studio and clone the lab materials into the workspace.

1. In the Azure portal, navigate to the Azure Machine Learning workspace named **mlw-dp100-...**.
1. Select the Azure Machine Learning workspace, and in its **Overview** page, select **Launch studio**. Another tab will open in your browser to open the Azure Machine Learning studio.
1. Close any pop-ups that appear in the studio.
1. Within the Azure Machine Learning studio, navigate to the **Compute** page and verify that the compute instance and cluster you created in the previous section exist. The compute instance should be running, the cluster should be idle and have 0 nodes running.
1. In the **Compute instances** tab, find your compute instance, and select the **Terminal** application.
1. In the terminal, install the Python SDK on the compute instance by running the following commands in the terminal:

    ```
    pip uninstall azure-ai-ml
    pip install azure-ai-ml
    ```

    > Ignore any (error) messages that say that the packages couldn't be found and uninstalled.

1. Run the following command to clone a Git repository containing notebooks, data, and other files to your workspace:

    ```
    git clone https://github.com/MicrosoftLearning/mslearn-azure-ml.git azure-ml-labs
    ```

1. When the command has completed, in the **Files** pane, click **&#8635;** to refresh the view and verify that a new **Users/*your-user-name*/azure-ml-labs** folder has been created.

## Create a pipeline to evaluate models and submit from a notebook

Now that you have all the necessary resources, you can run the notebook to retrieve the built-in responsible AI components, create a pipeline, and submit the pipeline to generate a responsible AI dashboard.

1. Open the **Labs/10/Create Responsible AI dashboard.ipynb** notebook.

    > Select **Authenticate** and follow the necessary steps if a notification appears asking you to authenticate.

1. Verify that the notebook uses the **Python 3.10 - AzureML** kernel.
1. Run all cells in the notebook.

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should delete the resources you've created to avoid unnecessary Azure costs.

1. Close the Azure Machine Learning studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-...** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**.
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
