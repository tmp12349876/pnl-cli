#!/bin/bash

yum install -y yum-utils
yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
yum -y install terraform

# create ENV variable with DO token
export TF_VAR_DO="DOAPIKEYTOREPLACE"
export ADMIN_EMAIL="ADMINEMAILTOREPLACE"
export TF_VAR_PRIVATE_VPN="/root/.ssh/id_rsa_vpn_main"
export TF_VAR_PUBLIC_VPN="/root/.ssh/id_rsa_vpn_main.pub"
export DO_REGION="DOREGIONSLUGTOREPLACE"

#Generate ssh keys
ssh-keygen -t rsa -f /root/.ssh/id_rsa_vpn_main -q -N ""
chmod 400 /root/.ssh/id_rsa_vpn_main 

#Install git
yum install git -y

cd ~
# Email ssh key to new vpn server
BODY=$(cat /root/.ssh/id_rsa_vpn_main | base64)
NAME=$(date +%s)

echo "From: Sender <noreply@pnl.nyc>
To: ${ADMIN_EMAIL}
Subject: PnL VPN Activation
Mime-Version: 1.0
Content-Type: multipart/mixed; boundary="19032019ABCDE"
--19032019ABCDE
Content-Type: text/plain; charset="US-ASCII"
Content-Transfer-Encoding: 7bit
Content-Disposition: inline
Attached is the key to your Private VPN server. Keep it secret, keep it safe.
    May you do good and not evil.
    May you find forgiveness for yourself and forgive others.
    May you share freely, never taking more than you give.
--19032019ABCDE
Content-Type: application;
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="${NAME}.key"
${BODY}
--19032019ABCDE--
" > email.eml

sendmail -t < email.eml
# pull down pnl-vpn repo
#TODO remove token and make publically available pnl vpn repo
git clone https://github.com/AnubisBeaker/pnl-vpn.git

# cd into repo
cd pnl-vpn
sed -i -e 's/${ADMIN_EMAIL}/'"$ADMIN_EMAIL"'/g' bin/vpn-install.sh
sed -i -e 's/nyc1/'"$DO_REGION"'/g' digitalocean.tf
chmod +x bin/*
# run terraform builder
terraform init -input=false 
terraform plan -input=false -auto-approve
terraform apply -input=false -auto-approve

