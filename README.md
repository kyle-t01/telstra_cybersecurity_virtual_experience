# telstra_cybersecurity_virtual_experience

## Experience Summary
Virtual Experience URL:
https://www.theforage.com/simulations/telstra/cybersecurity-cyyo

### Task 1: Responding to a Malware attack
- triage alerts in the Security Operations Center and notify appropiate team for response

**Task 1 response:** 
**From**: Telstra Security Operations
**To**: nbnTeam (nbn@email)
**Subject**:  P1 – Critical ongoing cyberattack
__
Body:
Hello nbn Team, 

At 2022-03-20T03:16:34Z, there is an ongoing attack towards the network hostname of nbn.external.network, under the NBN Connection Infrastructure. The severity of attack necessitates a P1 – Critical Priority response. 

As the attacker attempted to access /tomcatwar.jsp and given that the infrastructure software is Spring Framework 5.3.0, we suspect that the attacker is attempting remote code execution. Our team suggests immediately apply the following mitigation: upgrade Spring Framework 5.3.0 to 5.3.18+.

For any questions or issues, don’t hesitate to reach out to us. 

Kind regards, 
Telstra Security Operations

### Task 2: Analysing the attack
- analyse malware attack patterns to prepare a firewall rule, and communicate it to the networks team

**Task 2 response:**
**From**: Telstra Security Operations
**To**: networks Team (networks@email)
**Subject**: Create Firewall Rule Spring4Shell Vulnerability
—
Body: 
Hello networks team,

We would like to request the creation of a firewall rule and provide you more information about the ongoing attack.

The ongoing remote code execution attack exploits the Spring4Shell vulnerability, where it requires the application to run on Apache Tomcat as a WAR deployment, and the Spring Framework in this case is 5.3.0.

We request that POST requests containing class.module.classLoader… to the /tomcatwar.js , with the headers of: 
suffix=%>//
c1=Runtime
c2=<%
DNT=1
Content-Type=application/x-www-form-urlencoded
be blocked.

For any questions or issues, don’t hesitate to reach out to us.

Kind regards,
Telstra Security Operations

### Task 3: (Technical) Mitigate malware attack
- as the networks team, use Python to write a firewall rule to mitigate the malware from spreading

**Task 3 response:**
Please refer to firewall_server.py
The python script filters out requests that had the malicious headers identified in ealier tasks, if the path requested is towards "/tomcatwar.jsp".

### Task 4: Incident Postmortem
- create a postmortem to reflect on the details of the incident

**Task 4 response:**

**Summary:**
- **Abstract:** Remote code execution attack on Spring4Shell Framework hosted by nbn services team.
- **Impact:** Severity P1 - Critical
- **Keywords:** RCE, Spring4Shell, Zero-day, NBN-services team
- **Incident Duration:** 2022-03-20T03:16:34Z – 2022-03-20T05:16:00Z (~2 hours)
- **Participants:** Telstra security operations, nbn team, networks team
- **Detection Time:** 2022-03-20T03:46:34Z
- **Issue Resolved Time:** 2022-03-20T05:16:00Z

**Impact:**
- Critical P1 impact on nbn service infrastructure, leading to 2-hour downtime.

**Detection:**
- Starting from timestamp 2022-03-20T03:16:34Z, firewall logs detected multiple abnormal POST requests.

**Root Cause:**
- A zero-day vulnerability that allows remote code execution on outdated Spring Framework hosted by nbn services team.
- Starting from timestamp 2022-03-20T03:16:34Z, POST requests to the nbn host address were made with the header:
  - `suffix=%>//`
  - `c1=Runtime`
  - `c2=<%`
  - `DNT=1`
  - `Content-Type=application/x-www-form-urlencoded`
  - to the path `/tomcatwar.jsp`.

**Resolution:**
- At timestamp indicated by the Detection Time (30 minutes after incident start), nbn team was notified of the incident.
- Telstra Security Operations analyzed the malicious request patterns and forwarded them to the networks team.
- A firewall rule was created by the networks team after analysis of malicious request patterns, which was successful in mitigating the malware attack on deployment.
- Infrastructure affected by the attack was restored.

**Action Items:**
- On infrastructure with Spring Framework of 5.3.0+ or before, recommend upgrading to the newest version if feasible.
- Deploy the firewall rule on systems running Spring Framework to prevent such attacks.

