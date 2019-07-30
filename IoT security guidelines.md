# 延伸筆記1 - IoT security guidelines
---
### OWASP
##### Manufacturer IoT Security Guidance
The goal of this section is help manufacturers build more secure products in the Internet of Things space. The guidance below is at a basic level, giving builders of products a basic set of guidelines to consider from their perspective. This is not a comprehensive list of considerations, and should not be treated as such, but ensuring that these fundamentals are covered will greatly improve the security of any IoT product.
* Avoid the potential for persistent vulnerabilities in devices that have no update capability by ensuring that all devices and systems are built with the ability to be updated when vulnerabilities are discovered
* Rebranded devices used as part of a system should be properly configured so that unnecessary or unintended services do not remain active after the rebranding

##### Developer IoT Security Guidance
The goal of this section is help developers build more secure applications in the Internet of Things space. The guidance below is at a basic level, giving developers of applications a basic set of guidelines to consider from their perspective. This is not a comprehensive list of considerations, and should not be treated as such, but ensuring that these fundamentals are covered will greatly improve the security of any IoT product. Strongly consider using a Secure IoT Framework in order to proactively address many of the concerns listed below.
* Ensuring valid user accounts can't be identified by interface error messages
* Ensuring strong passwords are required by users
* Implementing account lockout after 3 - 5 failed login attempts

##### Consumer IoT Security Guidance
The goal of this section is help consumers purchase secure products in the Internet of Things space. The guidance below is at a basic level, giving consumers a basic set of guidelines to consider from their perspective. This is not a comprehensive list of considerations, and should not be treated as such, but ensuring that these fundamentals are covered will greatly aid the consumer in purchasing a secure IoT product.
* Include security in feature considerations when evaluating a product
* Place Internet of Things devices on a separate network if possible using a firewall

---
### GSMA
The GSMA, together with the mobile industry, has delivered a set of IoT Security Guidelines, backed by an IoT Security Assessment scheme, to provide a proven and robust approach to end-to-end security.

The GSMA IoT Security Guidelines provide best practice for the secure design, development and deployment of IoT solutions across industries and services. Addressing typical cybersecurity and data privacy issues associated with IoT services, the guidelines outline a step-by-step process to securely launch IoT solutions to market and keep them secure through their lifecycles – thereby creating a sustainable IoT ecosystem that is designed for end-to-end security.

The GSMA IoT Security Assessment provides a flexible framework that addresses the diversity of the IoT market, enabling companies to build secure IoT devices and solutions as laid out in the GSMA IoT Security Guidelines.

Both the GSMA IoT Security Guidelines and IoT Security Assessment have been updated by the industry to extend the scope to Mobile IoT technologies, specifically NB-IoT and LTE-M, the 3GPP industry standards for low power wide area technologies in licensed spectrum.

The primary audience for the IoT Security Guidelines are:
* IoT Service Providers – enterprises or organisations who are looking to develop new and innovative connected products and services
* IoT Device Manufacturers – who provide IoT devices to IoT service providers, in order to enable IoT services
* IoT Developers – who build IoT services on behalf of IoT service providers
* Network Operators – who provide services to IoT service providers

---
### IoTSF
This release of the Best Practice Guidelines applies particularly to home consumer products,
although the general principles apply in all market areas.
‘Internet of Things’ (IoT) devices fall into three main categories:
* Sensors, which gather data
* Actuators, which effect actions
* Gateways, which act as communication hubs and may also implement some automation logic.

All these device types may stand alone or be embedded in a larger product. They may also be
complemented by a web application or mobile device app and cloud-based service.
IoT devices, services and software, and the communication channels that connect them, are at risk
of attack by a variety of malicious parties, from bedroom hackers to professional criminals or even
state actors. Possible consequences to consumers of such an attack could include:
* Inconvenience and irritation
* Infringement of privacy
* Loss of life, money, time, property, health, relationships, etc.

For vendors, operators and suppliers, potential consequences may include loss of trust, damage to
reputation, compromised intellectual property, financial loss and possible prosecution.

---
### NIST - National Institute of Standards and Technology
IoT devices have become increasingly prevalent, both in the U.S. and worldwide, with one information technology research and advisory company forecasting that the count of IoT devices in use will reach 20.8 billion by 2020. Another company projects that in 2018, IoT devices will surpass mobile phones as the largest category of connected devices, with a growth projection of 23 percent annually between 2015 and 2021. However with this increased adoption comes a greater potential for misuse, as evidenced by their use in a number of recent DDoS attacks.  The attackers have been able to exploit the relative security weaknesses in IoT devices, like internet-connected cameras and DVRs, using malware to create networks of these computers, known as botnets, that report to a central control server that can be used as a staging ground for launching powerful DDoS attacks.  This malware is able to gain control over numerous IoT devices by continuously scanning the Internet for IoT systems protected by factory default or hard-coded usernames and passwords.

The Guidance is designed to help prevent the vulnerabilities that lead to their exploitation and to facilitate “a disciplined, structured, and standards-based set of systems security engineering activities.”  To accomplish this, the Guidance focuses on assessing the trustworthiness of various internet-connected devices and their impacts through a series of processes governed by the life cycle of each device. The Guidance breaks those processes into four categories:

* Agreement processes
* Organization-project enabling processes
* Technical management processes
* Technical processes

---
### My reflections
There are so many security guidelines for IOT on the Interent already. The guidance is not only for manufacturers, developers, but also for consumers as well. The guidance provides a framework for better securing these devices and perhaps it could be used help making the IoT security regulations.

---
reference:

https://www.gsma.com/iot/iot-security/iot-security-guidelines/

https://www.owasp.org/index.php/IoT_Security_Guidance

https://www.iotsecurityfoundation.org/best-practice-guidelines/