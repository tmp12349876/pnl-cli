# PnL CLI
A tool for deploying crowd configured services.
Sponsered by PnL.

### Overview
Free and Open Source tools are provided by community members from all over the world at no cost and as an alternative to expensive enterprise software.
FOSS software in many ways aims to provide equality to members of the technology community.
Innovation in the open source community is provided free of charge to the end user.

Accessibility of software naturally leads to an increase in its popularity.
Docker and Terraform are good examples of what open collaboration can acheive.

Privacy continues to be a pressing issue as technology as shown itself to be capable of subtly invading ones personal space.
As end users become more aware of the adverse impacts applications they use today can have on their freedom,
they will join the pursuit of FOSS technology.
Technologies where they can control there own data and operate in peace and quiet.
The noise is loud but many can still not hear it today.
Our liberties crumble.

As computing continues to become cheaper more and more people have access to the internet.
Cloud computing has emerged to at very least remove the burden of hardware maintaince.
VDI, RDP, DCs, etc.

There are few alternatives to the apps used in the course of ones daily modern life.
The apps that do exist are difficult to setup.

The PnL CLI allows for the deployment of terraform configured applications into various public and private clouds.
These simple commands can therefore in theory be used to deploy a wide variety of systems.

PnL also strives to deliver the best configurations for FOSS tools so you can focus on getting things done instead of needed to know all the underlying technical details.
As all of PnLs configurations are open source they are all auditable and our community is security and privacy focused.
Our goal is to bring FOSS services, preconfigured with security in mind to the masses.

This initial version is focused on deploying WireGuard VPN servers on DigitalOcean. Much more to come in the future...

### Requirements
* Python 3.x
* Python Requests library
* Digital Ocean API Key

### Install
Configure Python according to your system instructions.
It is to use `pyenv` or another Python versioning tool if multiple python versions are installed on the system.
You can install `pyenv` by following the directions [here](https://github.com/pyenv/pyenv)

pyenv cheatsheet
```
pyenv versions
pyenv global 3.3.3
pyenv local 3.3.3
```

You should also manage your python dependencies using a tool such as virutalenv.
`virtualenv` can be installed with `pip install virtualenv`.
Activate a new virtual environment in this repos root directory using
```
virtualenv venv
source ./venv/bin/activate
```

You can install the Python requests library with 
```
pip install requests
```

Once the environment is setup you can start the PnL CLI by running `python pnl.py`.
Type `help` for instructions on available commands and `help <command>` for specific command details.

You will need to set the DO API key and admin email address to run most commands.
These parameters can be set each time the CLI is run using the `init` command,
or can be stored in the users `.bash_profile` as such
```
export ADMIN_EMAIL="email@address"
export DO_API_KEY="API_KEY"
```

You must run `source ~/.bash_profile` for the updates to take effect.

### Architecture
[TBD]

### Feature Support
The CLI deployment is initially focused on deploying VPN servers as they are the cornerstone of any PnL deployment.
They provide security in accessing the various resources by creating a private network.

##### CLI Integration
```
[x] VPN deployment (WireGuard)
[] Video Conferencing (JitsiMeet)
[] Messaging Server (MatterMost)
[] Personal cloud storage (NextCloud)
[] Project Management Solution (GitLab)
[] Identity Management (KeyCloak)
```

##### Terraform Configuration
**PnL VPN** [WireGuard]
**PnL Meet** [JitsiMeet]
**PnL Chat** [MatterMost]
**PnL Cloud** [NextCloud]
**PnL Labs** [GitLab]
**PnL IDP** [KeyCloak]

###  Future Roadmap
```
[] Addtional cloud provider support
[] Home network deployments
[] Add users to existing VPN deployments
[] Deploy other services into existing VPN
```

### Reference (help)
The `help` command can be useful for understanding what CLI functionality is available.

For example:

```
The PnL Command Line Interface
PNL:> help

Documented commands (type help <topic>):
========================================
delete  deploy  help  init  list  quit

PNL:> help init

    Initialze the PnL CLI session

    You will be prompted to enter a DO API key and email address.

    To maintain these settings, add the following to your .bash_profile

    export ADMIN_EMAIL="email@address"
    export DO_API_KEY="API_KEY"
    
PNL:> help deploy

    Deploy a VPN server into a specified cloud region.

    Example:
      deploy
    
PNL:> help list

    List the currently deployed pnl resources.

    Example:
      list
    
PNL:> help delete

    Delete a resource

    Example:
      delete
    
```

The currently supported VPN deployment regions are

Digital Ocean:

* New York City
* Amsterdam
* San Francisco
* Singapore
* London
* Frankfurt
* Toronto
* Bangalore
