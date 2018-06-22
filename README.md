Setup
==========

This documentation describes how to setup Otter Manager/Node/ZooKeepers.

## Install Components and Prepare Configuration

```
$ vagrant up
$ ansible-playbook  -i provisioning/hosts.vagrant  provisioning/playbook.yml
```

## Start ZooKeeper Clusters

```
$ vagrant ssh cn1    #(also sg1/sg2)
$ cd /opt/zookeeper
$ sudo bin/zkServer.sh start
```

## Start Otter Manager

```
$ vagrant ssh sg1    #(only in sg1 server)
$ cd /opt/manager
$ sudo bin/startup.sh
```

## Start Otter Node

First, you should add node in Otter Manager Web UI

And there, you will got a id for your node(nid).

```
$ vagrant ssh cn1
$ cd /opt/node1
$ sudo su
# echo {{ nid }} > conf/nid
# bin/startup.sh
```
