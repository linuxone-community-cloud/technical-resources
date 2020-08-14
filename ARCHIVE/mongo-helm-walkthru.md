# MongoDB Helm Chart Deployment

## Overview
This document will take you through using the MongoDB Helm Chart preloaded in the LinuxONE Community Cloud IBM Cloud Private container service to deploy your first MondoDB Helm Release.

## Steps

1. Login to IBM Cloud Private
2. Choose the MongoDB helm chart
3. Customize the configuration
4. Deploy/Install the MongoDB Database

## Step 1. Login to IBM Cloud Private

From a browser, go to the [IBM Cloud Private website](https://container.cloud.marist.edu:8443/oidc/login.jsp) and log in with your credentials you previously set up.
    ![alt text](images-mongodb/login.png "login")


## Step 2. Choose the MondoDB helm chart

1.  Click the Catalog in the upper right side of screen

    ![alt text](images-mongodb/catalog.png "catalog")

2.  Select the "ibm-mongodb-dev" helm charts

    ![alt text](images-mongodb/select-mongodb.png "select mongodb")


## Step 3. Customize the configuration

1. Customize the MongoDB deployment, paying attention to the "Release name", "Target namespace", agreeing to the license agreements, "MongoDB username" and "Password for MongoDB admin user".  You can take defaults for everything else.

    ![alt text](images-mongodb/config-mongo-1.png "select config-mongo")
    ![alt text](images-mongodb/config-mongo-2.png "select config-mongo")
    ![alt text](images-mongodb/config-mongo-3.png "select config-mongo")


## Step 4.  Deploy/Install the MongoDB Database

1. Click "Install" in lower right corner of screen

    ![alt text](images-mongodb/mongo-install.png "install")

2. Confirm the installation started with this confirmation...

    ![alt text](images-mongodb/mongo-install-confirm.png "install confirmation")

3. Check the status of your MondoDB deployment/install by clicking "Workloads" and then "Deployments" in the upper left hand corner of screen.


    ![alt text](images-mongodb/deployments.png "deployments")

    ![alt text](images-mongodb/deployments-2.png "deployments")

4.  Click the individual deployments to get more details.

    ![alt text](images-mongodb/deployments-3.png "deployments")

5.  You can also click "Workloads" and "Helm Releases" to get more details about the Helm Release

    ![alt text](images-mongodb/helm-releases.png "helm release")
    ![alt text](images-mongodb/helm-releases-2.png "helm release")
    ![alt text](images-mongodb/helm-releases-3.png "helm release")
