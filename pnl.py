import os
import sys
import subprocess
import random

import requests

from cmd import Cmd

# Disable insecure warning for now
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#DO_API_KEY = "18212f9ec0f3cf34494732df824391e65a12c74b55c4b9ff66a5df3f6b3fef0a"


DO_BASE_URL = "https://api.digitalocean.com/v2"
    

class pnlShell(Cmd):
  def __init__(self, **kwargs):
    Cmd.__init__(self, **kwargs)
    self.prompt = "PNL:> "

    self.DO_API_KEY = os.environ.get('DO_API_KEY')
    self.ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')

    self.HEADERS = {
      "Authorization": f"Bearer {self.DO_API_KEY}",
      "Content-Type": "application/json"
    }


  def do_deploy(self, args):
    """
    Deploy a VPN server into a specified cloud region.

    Example:
      deploy
    """
    with open("cloud-init.sh", "r") as f:
      user_data = f.read()
    regions = [
      { "display": "New York City", "slug": "nyc1" },
      { "display": "Amsterdam", "slug": "ams3" },
      { "display": "San Francisco", "slug": "sfo3" },
      { "display": "Singapore", "slug": "sgp1" },
      { "display": "London", "slug": "lon1" },
      { "display": "Frankfurt", "slug": "fra1" },
      { "display": "Toronto", "slug": "tor1" },
      { "display": "Bangalore", "slug": "blr1" }
    ]

    region_list = "Regions available for VPN deployment\n"
    
    for index, region in enumerate(regions):
      region_list += f"\t{index}. {region['display']}\n"
    print(self.ADMIN_EMAIL)
    print(region_list)
    selected_region = int(input("Enter the number of the region: "))
    
    user_data = user_data.replace("DOREGIONSLUGTOREPLACE", regions[selected_region]["slug"])
    user_data = user_data.replace("DOAPIKEYTOREPLACE", self.DO_API_KEY)
    user_data = user_data.replace("ADMINEMAILTOREPLACE", self.ADMIN_EMAIL)
    print(user_data)
    body = {
      "name":"Terraform-Initial-Builder",
      "region": regions[selected_region]["slug"],
      "size":"s-1vcpu-1gb",
      "image":"centos-7-x64",
      "ssh_keys": 28787275,
      "tags": ["pnl"],
      "user_data": user_data
    }
    endpoint = "/droplets"
    url = DO_BASE_URL + endpoint
    res = requests.post(url, headers=self.HEADERS, json=body, verify=False)
    data = res.json()
    md = f"""
    Successfully deployed builder droplet, ssh key emailed!
    Name: {data['droplet']['name']}
    Region: {data['droplet']['region']['name']}
    ID: {data['droplet']['id']}

    VPN is now being created. Takes approx 15min to complete.
    The VPN conf file will be emailed seperately when ready.
    """
    print(md)
    
  def do_list(self, args):
    """
    List the currently deployed pnl resources.

    Example:
      list
    """
    endpoint = "/droplets" 
    url = DO_BASE_URL + endpoint
    params = {
      "tag_name": "pnl"
    }
    res = requests.get(url, headers=self.HEADERS, params=params, verify=False)
    data = res.json()
    md = "Resources\n"
    for droplet in data["droplets"]:
      md += f"""
      Name: {droplet['name']}
      Region: {droplet['region']['name']}
      ID: {droplet['id']}
      """
    print(md)
  def do_delete(self, args):
    """
    Delete a resource

    Example:
      delete
    """
    print("Which droplet do you wish to delete?")
    print("Enter 'q' to abort")
    droplet_id_to_delete = input("Enter ID:")

    if droplet_id_to_delete == 'q':
      return
    
    endpoint = f"/droplets/{droplet_id_to_delete}"
    url = DO_BASE_URL + endpoint
    
    res = requests.delete(url, headers=self.HEADERS, verify=False)
    if res.status_code == 204:
      print(f"Droplet {droplet_id_to_delete} deleted successfully")
    else:
      print(f"Issue deleting droplet. {res.status_code}")
  def do_init(self, args):
    """
    Initialze the PnL CLI session

    You will be prompted to enter a DO API key and email address.

    To maintain these settings, add the following to your .bash_profile

    export ADMIN_EMAIL="email@address"
    export DO_API_KEY="API_KEY"
    """
    # Prompt to enter DO api key
    print("init")
    if self.DO_API_KEY and self.ADMIN_EMAIL:
      print("The ADMIN_EMAIL and DO_API_KEY are already set")

    if not self.DO_API_KEY:
      self.DO_API_KEY = input("Enter DO API key: ")
    if not self.ADMIN_EMAIL:
      self.ADMIN_EMAIL = input("Enter admin email: ")

  def do_quit(self, args):
    """
    Quit
    """
    thoughts = [
      "May you do good and not evil",
      "May you find forgiveness for yourself and forgive others",
      "May you share freely, never taking more than you give."
    ]
    print(random.choice(thoughts))
    raise SystemExit
if __name__ == '__main__':
  shell = pnlShell()
  description = "The PnL Command Line Interface"
  shell.cmdloop(intro=description)
