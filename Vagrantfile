$script_mysql = <<-SCRIPT
  apt-get update --fix-missing  && \
  apt-get install -y mysql-server-5.7 && \
  mysql -e "create user 'pythonuser'@'%' identified by 'pass';" && \
  mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'pythonuser'@'%' IDENTIFIED BY 'pass';" && \
  mysql -e "create database dbdime CHARACTER SET UTF8 collate utf8_general_ci;" 
  
SCRIPT

$script_dime = <<-SCRIPT
  apt-get update && \
  apt-get install -y python3-pip && \
  pip3 install oauth2client -U && \
  pip3 install reportlab -U && \
  pip3 install anaconda -U
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

    config.vm.define "mysql" do |mysql|

      #mysql.vm.network "forwarded_port", guest: 80, host: 8089
      #mysql.vm.network "public_network", ip: "10.10.5.92"
      mysql.vm.network "public_network", ip: "192.168.0.150"

      mysql.vm.provision "shell", inline: $script_mysql

      mysql.vm.synced_folder "./configs", "/configs"
      mysql.vm.synced_folder ".", "/vagrant", disabled: true
      
      mysql.vm.provision "shell",
         inline: "cat /configs/id_rsa.pub >> .ssh/authorized_key:s"

      mysql.vm.provision "shell",
        inline: "cat /configs/mysqld.cnf > /etc/mysql/mysql.conf.d/mysqld.cnf"
      
      mysql.vm.provision "shell",
        inline: "service mysql restart"

    end

      config.vm.define "app" do |app|
        app.vm.network "public_network", ip: "192.168.0.152"
        #dime.vm.provision "shell", inline: $script_app
        app.vm.synced_folder ".", "/app"
        app.vm.synced_folder ".", "/vagrant", disabled: true
      end


end
