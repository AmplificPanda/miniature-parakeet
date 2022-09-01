# miniature-parakeet
Personal learning as part of the Introduction for Cybersecurity Course by INFOSEC
Please note: All notes are written for personal purposes only and may not be beneficial to others.

The three objectives:
- Develop python scripts to automate cybersecurity tasks
- Apply Python to meet objectives throughout the cybersecurity attack life cycle
- Automate common cyberattack and defense activities within Python.

Learning is mapped to MITRE ATT&CK and Shield frameoworks.

Why Python?
- Popular language and one of the fastest-growing
- Simple, readable syntax, easy to learn and use, perfect for scripting
- Includes a number of libraries providing a massive amount of built-in functionality (through imports)

The ATT&CK Framework
![](thematrix.png)

The Shield Framework:
![](shieldmatrix.png)

MITRE Shield was developed by MITRE to promote active defense.
Taking actions to gain some control over an attacker's actions on defenders networks.

Terms: 
- Tactic: the tactical goal at a particular stage of a cyberattack or a goal in active defense
- Technique: A mechanism by which an attacker can achieve the goal outlined in a particular tactic
    - Sub-technique: a method for carrying out a particular technique
- Procedure: A specific implementation of a particular technique
or sub-technique. 

For e.g. Brute Force is a tactic of credential access. We may have multiple techniques for achieving a technique (sub-techniques): password guessing, cracking, spraying and credential stuffing. 
Procedures = Different tools, particular malware variants etc.



S1: Q&A's
Top Level in MITRE ATT&CK + Tactic
John the Ripper = Example of Procedure (as it is a tool)
PRE ATT&CK Matrix = Reconnaissance & Resource Development
False: A cyberthreat actor will use at least one technique from every tactic during a cyberattack.

**Section 1: MITRE PRE-ATT&CK**

The first stage of PRE involves gathering information from a variety of sources. Some of the techniques used are:
- Active Scanning
- Gather Victim host, identity, network and organization information
- Phishing for information
- Search closed sources
- Open technical databases
- Search open websites/domains
- Search victim-owned websites

The second stage of PRE involves the attacker developing or aquiring the tools needed to perform their attack:
- Acquire infrastructure
- Compromise Infrastructure
- Develop capabilities
- Establish accounts
- Obtain capabilities

Resource Development not covered by Python as it is dependent heavily on attacker's goals and resources. Thus, we will look at two techniques of reconnaissance tactic of PRE-ATT&CK:
- Active Scanning:: Network scanning
- Search open technical databases: DNS Exploration

Network Scanning:
- Knowledge of target network is vital for an attacker
  - Identification of potential target systems
  - Discovery of vulnerable applications
  
Network scanning is one method of learning a target network architecture.
 - Port scanning
 - Banner collection ... e.g. SSH displays info which can help you identify vulnerablities present in a specific version of SSH
 - Vulnerability scanning

 Active scanning is the technique:
  - Scanning IP Blocks
  - Vulnerability Scanning

**Open Technical Databases: (Tactic)**
- Open-source intelligence(OSINT) is a trove of useful data regarding an organization and its systems.
Examples include:
- WHOIS: records include data about owners of websites, system admins, etc
- DNS: maps domain names to IP addresses
- CDNs: store cached content for an organization's websites.

https://attack.mitre.org/ for viewing the full MITRE framework for ATT&CK.













