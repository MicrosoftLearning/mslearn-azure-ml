---
lab:
    title: 'Run a training script as a command job in Azure Machine Learning'
---

# Run a training script as a command job in Azure Machine Learning

A notebook is ideal for experimentation and development. Once you've developed a machine learning model and it's ready for production, you'll want to train it with a script. You can run a script as a command job.

In this exercise, you'll test a script and then run it as a command job.

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
    cd azure-ml-labs/Labs/08
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

## Convert a notebook to a script

Using a notebook attached to a compute instance is ideal for experimentation and development as it allows you to immediately run code you've written and review its output. To move from development to production, you'll want to use scripts. As a first step, you can use the Azure Machine Learning studio to convert your notebook to a script.

1. Open the **Labs/08/src/Train classification model.ipynb** notebook.

    > Select **Authenticate** and follow the necessary steps if a notification appears asking you to authenticate.

1. Verify that the notebook uses the **Python 3.10 - AzureML** kernel.
1. Run all cells to explore the code and train a model.
1. Select the &#9776; icon at the top of the notebook to view the **notebook menu**.
1. Expand **Export as**, and select **Python (.py)** to convert the notebook to a Python script.
1. Name the new file `train-classification-model`.
1. Once the new file is created, the script should automatically be opened. Explore the file and note that it contains the same code as the notebook.
1. Select the &#9655;&#9655; icon at the top of the notebook to **save and run the script in the terminal**.
1. The script is initiated by the command **python train-classification-model.py** and the output should be shown below the command.

   > **Note:** If the script returns an ImportError for libstdc++6, run the following commands in the terminal before running the script again:
   > ```bash
   > sudo add-apt-repository ppa:ubuntu-toolchain-r/test
   > sudo apt-get update
   > sudo apt-get upgrade libstdc++6
   > ```

## Test a script with the terminal

After converting a notebook to a script, you may want to further refine it. One best practice when working with scripts, is to use functions. When your script consists of functions, it's easier to unit test your code. When you use functions, your script will consist of blocks of code, each block performing a specific task.

1. Open the **Labs/08/src/train-model-parameters.py** script and explore its contents.
    Note that there is a main function which includes four other functions:

    - Read data
    - Split data
    - Train model
    - Evaluate model

    After the main function, each function is defined. Note how each function defines the expected input and output.

1. Select the &#9655;&#9655; icon at the top of the notebook to **save and run the script in the terminal**. You should get an error after **Reading data...** telling you that it couldn't get the data because the file path was invalid.

    Scripts allow you to parameterize your code to easily change the input data or parameters. In this case, the script expects an input parameter for the data path which we didn't provide. You can find the defined and expected parameters at the end of the script in the **parse_args()** function.

    There are two input parameters defined:
    - **--training_data** which expects a string.
    - **--reg_rate** which expects a number, but has a default value of 0.01.

    To run the script successfully, you'll need to specify the value for the training data parameters. Let's do that by referring to the **diabetes.csv** file which is stored in the same folder as the training script.

1. In the terminal, run the following commands:

    ```
    cd azure-ml-labs/Labs/08/src/
    python train-model-parameters.py --training_data diabetes.csv
    ```

The script should successfully run and as a result, the output should show the accuracy and AUC of the trained model.

Testing the script in the terminal is ideal for verifying whether the script works as expected. If there is any issue with the code, you'll receive an error in the terminal.

**Optionally**, edit the code to force an error and run the command again in the terminal to run the script. For example, remove the line **import pandas as pd**, save and run the script with the input parameter to review the error message.

## Run a script as a command job

If you know your script works, you can run it as a command job. By running your script as a command job, you'll be able to track all the inputs and outputs of the script.

1. Open the **Labs/08/Run script as command job.ipynb** notebook.
1. Run all cells in the notebook.
1. In the Azure Machine Learning studio, navigate to the **Jobs** page.
1. Navigate to the **diabetes-train-script** job to explore the overview of the command job you ran.
1. Navigate to the **Code** tab. All contents of the **src** folder, which was the value of the **code** parameter of the command job, are copied here. You can review the training script which was executed by the command job.
1. Navigate to the **Outputs + logs** tab.
1. Open the **std_log.txt** file and explore its contents. The content of this file is the output of the command. Remember the same output was shown in the terminal when you tested the script there. If the job is unsuccessful because of an issue with the script, the error message will be shown here.

**Optionally**, edit the code to force an error and use the notebook to initiate the command job again. For example, remove the line **import pandas as pd** from the script and save the script. Or, edit the command job configuration to explore the error messages when something is wrong with the job configuration itself instead of the script.

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should delete the resources you've created to avoid unnecessary Azure costs.

1. Close the Azure Machine Learning studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-...** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**.
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
