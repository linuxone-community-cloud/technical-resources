![](RackMultipart20200715-4-1mqmsxw_html_fe6804a6ad418043.jpg) Quick Start Guide v1.0

| **Running**  **MongoDB in**  **Docker**  **Containers** | The following instructions can be used to install MongoDB in a Docker container and run database queries in IBM LinuxONE Community Cloud instances. This MongoDB example consists of a database collection of restaurant documents. The example will demonstrate a query and an insertion of a document in the collection. |
| --- | --- |

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

# Prerequisites

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

## Sign up for a LinuxONE Community Cloud trial account

If you have not done so already, register at http://www.ibm.com/linuxone/try for a 120-day trial account. You will receive an email containing credentials to access the LinuxONE Community Cloud self-service portal. This is where you can start exploring all our available services. **Deploy a virtual server instance**

If you have not deployed a virtual server already, please follow these instructions

http://developer.ibm.com/linuxone/wp-content/uploads/sites/57/virtual-servers-quick-start.pdf to create one before proceeding. Make sure you select a flavor (resource definition) with 4 GB of memory (Medium).

This quick-start guide has been tested with the following Linux distributions:

- Red Hat Enterprise Linux (RHEL) 7.2
- SUSE Linux Enterprise Server (SLES) 12
- Ubuntu 16.04

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

# Part A: Install Docker

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

1. Log on to your virtual server with the &#39;linux1&#39; user for RHEL and SLES, or the &#39;ubuntu&#39; user for Ubuntu.

ssh -i \&lt;ssh key\&gt; linux1@\&lt;server IP address\&gt;

or

ssh -i \&lt;ssh key\&gt; ubuntu@\&lt;server IP address\&gt;

or use an SSH client like PuTTY.

1. Switch to root user. sudo su -
2. Download and install Docker files.

RHEL:

  1. wget ftp://ftp.unicamp.br/pub/linuxpatch/s390x/redhat/rhel7.2/docker-1.11.2-rhel7.220160623.tar.gz
  2. tar -xvzf docker-1.11.2-rhel7.2-20160623.tar.gz
  3. mv docker-1.11.2-rhel7.2-20160623/docker\* /bin/

SLES:

Docker already installed. Proceed to Step 4.

Ubuntu:

a.apt-get -y install docker.io=1.10.3-0ubuntu6

1. Start the Docker daemon.

RHEL, SLES:

  1. docker daemon -g /local/docker/lib &amp;
  2. Hit &quot;enter&quot; or &quot;return&quot; Ubuntu:

Daemon already running. Proceed to Part B.

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

# Part B: Download and Install MongoDB

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

1. Create a local directory to store MongoDB data.

mkdir -p /local/docker/mongo-data

1. Download and run the MongoDB image in a Docker container.

docker run -v /local/docker/mongo-data:/mongodb/data -p 27017:27017 -p 28017:28017 -d sinenomine/mongodb-s390x

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

# Part C: Import an Example Database

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

1. Note the Docker Container ID running MongoDB.

docker ps –a

For example,

![](RackMultipart20200715-4-1mqmsxw_html_cd06f3d66d8e61e8.gif)

1. Start a Bash session within the Docker container.

docker exec -it \&lt;CONTAINER ID\&gt; bash

1. Download the example restaurant collection.

curl -O https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/primerdataset.json

1. Import the collection into the test database.

mongoimport --db test --collection restaurants --drop --file ./primer-dataset.json

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

# Part D: Interact with the Example Database in MongoDB

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

1. Start the MongoDB service.

mongo

1. Connect to the test database to access the restaurant collection.

use test

1. Query the database for all &#39;Bakeries&#39;.

db.restaurants.count( { &quot;cuisine&quot;: /Bakery/ } )

The result should show 691.

1. Insert a new &#39;Bakery&#39; document.

db.restaurants.insert({&quot;address&quot; : { &quot;building&quot; : &quot;123&quot;, &quot;coord&quot; : [-73.9434351, 40.6075879], &quot;street&quot;

: &quot;First Street&quot;, &quot;zipcode&quot; : &quot;12345&quot; }, &quot;borough&quot; : &quot;Borough&quot;, &quot;cuisine&quot; : &quot;Bakery&quot;, &quot;grades&quot; : [ {

&quot;date&quot; : ISODate(&quot;2016-01-01T00:00:00Z&quot;), &quot;grade&quot; : &quot;A&quot;, &quot;score&quot; : 10 } ], &quot;name&quot; : &quot;New Bakery&quot;, &quot;restaurant\_id&quot; : &quot;12345678&quot; })

1. Query the database for all &#39;Bakeries&#39;.

db.restaurants.count( { &quot;cuisine&quot;: /Bakery/ } )

The result should show 692.

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

# Extras

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

## Handy Commands

To stop all Docker containers: docker stop $(docker ps -a -q) To remove all Docker instances: docker rm -f $(docker ps -a -q) To remove all Docker images:

docker rmi -f $(docker images -q)

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

# Reference

![](RackMultipart20200715-4-1mqmsxw_html_2d46c59e4f08043f.gif)

## Links

https://docs.docker.com/engine/userguide/intro/ https://docs.docker.com/engine/installation/ https://docs.mongodb.com/getting-started/shell/

![](RackMultipart20200715-4-1mqmsxw_html_fe6804a6ad418043.jpg)

Page | 4© 2 0 1 6 I B M C o r p o r a t i o n
