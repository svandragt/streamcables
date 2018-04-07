# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.box = "ubuntu/xenial64"
    config.vm.synced_folder "liq/", "/etc/liquidsoap/"
    config.vm.synced_folder ".", "/vagrant/"

    config.vm.provision "shell", path: "vagrant/provision.sh"
    config.vm.provision "shell", path: "vagrant/provision-user.sh", privileged: false
    config.vm.provision "shell", path: "vagrant/provision-always.sh", privileged: false, run: "always"
end
