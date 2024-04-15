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

## Author a training pipeline

To explore the use of the assets and resources in the Azure Machine Learning workspace, let's try and train a model.

A quick way to author a model training pipeline is by using the **Designer**.

> **Note**: Pop-ups may appear throughout to guide you through the studio. You can close and ignore all pop-ups and focus on the instructions of this lab.

1. Select the **Designer** page from the menu on the left side of the studio.
1. Select the **Regression - Automobile Price Prediction (Basic)** sample.

    A new pipeline appears. At the top of the pipeline, a component is shown to load **Automobile price data (raw)**. The pipeline processes the data and trains a linear regression model to predict the price for each automobile.
1. Select **Configure & Submit** at the top of the page to open the **Set up pipeline job** dialogue
1. On the **Basics** page select **Create new** and set the name of the experiment to `train-regression-designer` then select **Next** .
1. On the **Inputs & outputs** page select **Next** without making any changes.
1. On the **Runtime settings** page an error appears as you don´t have a default compute to run the pipeline.

Let's create a compute target.

## Create a compute target

To run any workload within the Azure Machine Learning workspace, you'll need a compute resource. One of the benefits of Azure Machine Learning is the ability to create cloud-based compute on which you can run experiments and training scripts at scale.

1. In the Azure Machine Learning studio, select the **Compute** page from the menu on the left side. There are four kinds of compute resources you can use:
    - **Compute instances**: A virtual machine managed by Azure Machine Learning. Ideal for development when you're exploring data and iteratively experimenting with machine learning models.
    - **Compute clusters**: Scalable clusters of virtual machines for on-demand processing of experiment code. Ideal for running production code or automated jobs.
    - **Kubernetes clusters**: A Kubernetes cluster used for training and scoring. Ideal for real-time model deployment at a large scale.
    - **Attached compute**: Attach your existing Azure compute resources to the workspace, such as Virtual Machines or Azure Databricks clusters.

    To train a machine learning model that you authored with the Designer, you can use either a compute instance or compute cluster.

2. On the **Compute instances** tab, add a new compute instance with the following settings. 
    - **Compute name**: *Enter a unique name*
    - **Location**: *Automatically the same location as your workspace*
    - **Virtual machine type**: `CPU`
    - **Virtual machine size**: `Standard_DS11_v2`
    - **Available quota**: This shows dedicated cores available.
    - **Show advanced settings**: Note the following settings, but do not select them:
        - **Enable SSH access**: `Unselected` *(you can use this to enable direct access to the virtual machine using an SSH client)*
        - **Enable virtual network**: `Unselected` *(you would typically use this in an enterprise environment to enhance network security)*
        - **Assign to another user**: `Unselected` *(you can use this to assign a compute instance to a data scientist)*
        - **Provision with setup script**: `Unselected` *(you can use this to add a script to run on the remote instance when created)*
        - **Assign a managed identity**: `Unselected` *(you can attach system assigned or user assigned managed identities to grant access to resources)*

3. Select **Create** and wait for the compute instance to start and its state to change to **Running**.

> **Note**: Compute instances and clusters are based on standard Azure virtual machine images. For this exercise, the *Standard_DS11_v2* image is recommended to achieve the optimal balance of cost and performance. If your subscription has a quota that does not include this image, choose an alternative image; but bear in mind that a larger image may incur higher cost and a smaller image may not be sufficient to complete the tasks. Alternatively, ask your Azure administrator to extend your quota.

## Run your training pipeline

You've created a compute target and can now run your sample training pipeline in the Designer.

1. Navigate to the **Designer** page.
1. Select the **Regression - Automobile Price Prediction (basic)** pipeline draft.
1. Select **Configure & Submit** at the top of the page to open the **Set up pipeline job** dialogue
1. On the **Basics** page select **Create new** and set the name of the experiment to `train-regression-designer` then select **Next** .
1. On the **Inputs & outputs** page select **Next** without making any changes.
1. On the **Runtime settings** , in the **Select compute type** drop-down select *Compute instance* and in the **Select Azure ML compute instance** drop-down select your newly created compute instance.
1. Select **Review + Submit** to review the pipeline job and then select **Submit** to run the training pipeline.

The training pipeline will now be submitted to the compute instance. It will take approximately 10 minutes for the pipeline to complete. Let's explore some other pages in the meantime.

## Use jobs to view your history

Any time you run a script or pipeline in the Azure Machine Learning workspace, it's recorded as a **job**. Jobs allow you to keep track of the workloads you ran and compare them with each other. Jobs belong to an **experiment**, which allows you to group job runs together.

1. Navigate to the **Jobs** page, using the menu on the left side of the Azure Machine Learning studio.
1. Select the **train-regression-designer** experiment to view its job runs. Here, you'll see an overview of all jobs that are part of this experiment. If you ran multiple training pipelines, this view allows you to compare the pipelines and identify the best one.
1. Select the last job in the **train-regression-designer** experiment.
1. Note that the training pipeline is shown where you can view which components ran successfully or failed. If the job is still running, you can also identify what is currently being run.
1. To view the pipeline job details, select the **Job overview** at the top right to expand the **Pipeline job overview**.
1. Note that in the **Overview** parameters, you can find the job's status, who created the pipeline, when it was created and how long it took to run the complete pipeline (among other things).

    When you run a script or pipeline as a job, you can define any inputs and document any outputs. Azure Machine Learning also automatically keeps track of your job's properties. By using jobs, you can easily view your history to understand what you or your colleagues have already done.

    During experimentation, jobs help keep track of the different models you train to compare and identify the best model. During production, jobs allow you to check whether automated workloads ran as expected.

1. When your job is completed, you can also view the details of each individual component run, including the output. Feel free to explore the pipeline to understand how the model is trained.

## Delete Azure resources

When you finish exploring Azure Machine Learning, you should delete the resources you've created to avoid unnecessary Azure costs.

1. Close the Azure Machine Learning studio tab and return to the Azure portal.
1. In the Azure portal, on the **Home** page, select **Resource groups**.
1. Select the **rg-dp100-labs** resource group.
1. At the top of the **Overview** page for your resource group, select **Delete resource group**.
1. Enter the resource group name to confirm you want to delete it, and select **Delete**.
