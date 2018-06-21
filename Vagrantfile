# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end

  config.ssh.insert_key = false
  config.ssh.forward_agent = true

  config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "800"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
  end

  config.vm.define "cn1" do |cn1|
    cn1.vm.box = "juwai-centos65"
    cn1.vm.box_url = "http://downloads.juwai.io/devops/boxes/juwai-centos65-x86-64.box"
    cn1.vm.network "private_network", ip: "172.16.0.2"
  end

  config.vm.define "sg1" do |sg1|
    sg1.vm.box = "juwai-centos65"
    sg1.vm.box_url = "http://downloads.juwai.io/devops/boxes/juwai-centos65-x86-64.box"
    sg1.vm.network "private_network", ip: "172.16.1.2"
  end

  config.vm.define "sg2" do |sg2|
    sg2.vm.box = "juwai-centos65"
    sg2.vm.box_url = "http://downloads.juwai.io/devops/boxes/juwai-centos65-x86-64.box"
    sg2.vm.network "private_network", ip: "172.16.1.3"
  end

  config.vm.define "db_sg" do |db_sg|
    db_sg.vm.box = "juwai-centos65"
    db_sg.vm.box_url = "http://downloads.juwai.io/devops/boxes/juwai-centos65-x86-64.box"
    db_sg.vm.network "private_network", ip: "172.16.1.9"
  end

  config.vm.define "db_cn" do |db_cn|
    db_cn.vm.box = "juwai-centos65"
    db_cn.vm.box_url = "http://downloads.juwai.io/devops/boxes/juwai-centos65-x86-64.box"
    db_cn.vm.network "private_network", ip: "172.16.0.9"
  end
end
