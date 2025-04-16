---
lab:
    title: 'Explore the Azure Machine Learning workspace'
---

# Explore the Azure Machine Learning workspace

Azure Machine Learning provides a data science platform to train and manage machine learning models. In this lab, you'll create an Azure Machine Learning workspace and explore the various ways to work with the workspace. The lab is designed as an introduction of the various core capabilities of Azure Machine Learning and the developer tools. If you want to learn about the capabilities in more depth, there are other labs to explore.

## Before you start

You'll need an [Azure subscription](https://azure.microsoft.com/free?azure-portal=true) in which you have administrative-level access.

## Provision an Azure Machine Learning workspace

An Azure Machine Learning **workspace** provides a central place for managing all resources and assets you need to train and manage your models. You can provision a workspace using the interactive interface in the Azure portal, or you can use the Azure CLI with the Azure Machine Learning extension. In most production scenarios, it's best to automate provisioning with the CLI so that you can incorporate resource deployment into a repeatable development and operations (*DevOps*) process. 

In this exercise, you'll use the Azure portal to provision Azure Machine Learning to explore all options.

1. Sign into the `https://portal.azure.com/`.
2. Create a new **Azure Machine Learning** resource with the following settings:
    - **Subscription**: *Your Azure subscription*
    - **Resource group**: `rg-dp100-labs`
    - **Workspace name**: `mlw-dp100-labs`
    - **Region**: *Select the geographical region closest to you*
    - **Storage account**: *Note the default new storage account that will be created for your workspace*
    - **Key vault**: *Note the default new key vault that will be created for your workspace*
    - **Application insights**: *Note the default new application insights resource that will be created for your workspace*
    - **Container registry**: None (*one will be created automatically the first time you deploy a model to a container*)
3. Wait for the workspace and its associated resources to be created - this typically takes around 5 minutes.

> **Note**: When you create an Azure Machine Learning workspace, you can use some advanced options to restrict access through a *private endpoint* and specify custom keys for data encryption. We won't use these options in this exercise - but you should be aware of them!

## Explore the Azure Machine Learning studio

*Azure Machine Learning studio* is a web-based portal through which you can access the Azure Machine Learning workspace. You can use the Azure Machine Learning studio to manage all assets and resources within your workspace.

1. Go to the resource group named **rg-dp100-labs**.
1. Confirm that the resource group contains your Azure Machine Learning workspace, an Application Insights, a Key Vault, and a Storage Account.
1. Select your Azure Machine Learning workspace.
1. Select **Launch studio** from the **Overview** page. Another tab will open in your browser to open the Azure Machine Learning studio.
1. Close any pop-ups that appear in the studio.
1. Note the different pages shown on the left side of the studio. If only the symbols are visible in the menu, select the &#9776; icon to expand the menu and explore the names of the pages.
1. Note the **Authoring** section, which includes **Notebooks**, **Automated ML**, and  **Designer**. These are the three ways you can create your own machine learning models within the Azure Machine Learning studio.
1. Note the **Assets** section, which includes **Data**, **Jobs**, and **Models** among other things. Assets are either consumed or created when training or scoring a model. Assets are used to train, deploy, and manage your models and can be versioned to keep track of your history.
1. Note the **Manage** section, which includes **Compute** among other things. These are infrastructural resources needed to train or deploy a machine learning model.

## Train a model using AutoML

To explore the use of the assets and resources in the Azure Machine Learning workspace, let's try and train a model.

A quick way to train and find the best model for a task based on your data is by using the **AutoML** option.

> **Note**: Pop-ups may appear throughout to guide you through the studio. You can close and ignore all pop-ups and focus on the instructions of this lab.

1. Download the training data that will be used at `https://github.com/MicrosoftLearning/mslearn-azure-ml/raw/refs/heads/main/Labs/02/diabetes-data.zip` and extract the compressed files.
1. Back in the Azure Machine Learning studio, select the **AutoML** page from the menu on the left side of the studio.
1. Select **+ New Automated ML job**.
1. In the **Basic settings** step, give a unique name to your training job and experiment or use the default values assigned. Select **Next**.
1. In the **Task type & data** step, select **Classification** as the task type, and select **+ Create** to add your training data.
2. On the **Create data asset** page, in the **Data type** step, give a name to your data asset (e.g `training-data`) and select **Next**.
1. In the **Data source** step, select **From local files** to upload the training data you download previously. Select **Next**.
1. In the **Destination storage type** step, verify that **Azure Blob Storage** is selected as the datastore type and that **workspaceblobstore** is the datastore selected. Select **Next**.
1. In the **MLTable selection** step, select **Upload folder** and select the folder you extracted from the compressed file downloaded earlier. Select **Next**.
1. Review the settings for your data asset and select **Create**.
1. Back in the **Task type & data** step, select the data you just uploaded and select **Next**.

> **Tip**: You may need to select the **Classification** task type again before moving to the next step.

1. In the **Task settings** step, select **Diabetic (Boolean)** as your target column, then open the **View additional configuration settings** option.
1. In the **Additional configuration** pane, change the primary metric to **Accuracy**, then select **Save**.
1. Expand the **Limits** option and set the following properties:
    * **Max trials**: 10
    * **Experiment timeout (minutes)**: 60
    * **Iteration timeout (minutes)**: 15
    * **Enable early termination**: Checked

1. For **Test data**, select **Train-test split** and verify that the **Percentage test of data** is 10. Select **Next**.
1. In the **Compute** step, verify that the compute type is **Serveless** and the virtual machine size selected is **Standard_DS3_v2**. Select **Next**.

> **Note**: Compute instances and clusters are based on standard Azure virtual machine images. For this exercise, the *Standard_DS3_v2* image is recommended to achieve the optimal balance of cost and performance. If your subscription has a quota that does not include this image, choose an alternative image; but bear in mind that a larger image may incur higher cost and a smaller image may not be sufficient to complete the tasks. Alternatively, ask your Azure administrator to extend your quota.

1. Review all your settings and select **Submit training job**.

## Use jobs to view your history

After submitting the job, you'll be redirected to the job's page. Jobs allow you to keep track of the workloads you ran and compare them with each other. Jobs belong to an **experiment**, which allows you to group job runs together. 

1. Note that in the **Overview** parameters, you can find the job's status, who created it, when it was created and how long it took to run (among other things).
1. It should take 10-20 minutes for the training job to finish. When it is completed, you can also view the details of each individual component run, including the output. Feel free to explore the job page to understand how the models are trained.

    Azure Machine Learning automatically keeps track of your job's properties. By using jobs, you can easily view your history to understand what you or your colleagues have already done.
    During experimentation, jobs help keep track of the different models you train to compare and identify the best model. During production, jobs allow you to check whether automated workloads ran as expected.

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should delete the resources you've created to avoid unnecessary Azure costs.

1. Close the Azure Machine Learning studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-labs** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**.
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
