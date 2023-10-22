# ВОТ - Виртуализация и облачни технологии

lyubomir.stoyanov@oblak.bg
#### Съдържание:

## Какво е виртуализация?
Виртуализацията като технология позволява да бъдат създадени виртуални
репрезентации на сървъри, storage, networks и други физически машини. 

Виртуалният софтуер пресъздава функциите на физическия hw, което позволява няколко (n на брой) виртуални машини
да работят едновременно на една физическа машина.

Виртуализацията се използва с цел хардуерните ресурси да се използват по-ефективно. Затова съществуват cloud computing services, които менажират инфраструктурата по-ефикасно.

## Защо виртуализацията е важна?
Виртуализацията предоставя много повече възможности за взаимодействие с някакъв хардуерен ресурс.

Физическите сървъри консумират:
- Електричество
- Storage space (Пространство)
- Нуждаят се от поддрържа - конфигурации и тн.

Виртуализацията премахва тези ограничения като прави ***абстракция*** на
функционалностите на физическия hw в софтуер.

*Например:* Комапния има нужда от сървъри с три функции:
- Store business email securely 
- Run a customer-facing application 
- Run internal business applications

Всяка една от тези функционалности изисква различни ресурси
- За първата (email application) е нужно: more storage capacity & Windows OS
- За втората (customer-facing application) е нужно: Linux OS & high processing power to handle large volumes of website traffic
- За третата (internal business application) е нужно: iOS & more internal memory (RAM)

***Efficiant hw use***

Вместо да бъдат използвани три различни сървъра с виртуализация могат да бъдат създадени три дигитални сървъра (виртуали машини) само на един физически сървър.

***IaaS***

Компанията може да използва cloud instance или VMs от cloud computing provider (АWS, Azure, Google Cloud). 
AWS manages all the underlying hardware, and the company can request server resources with varying configurations. 
All the applications run on these virtual servers without the users noticing any difference.

 
[KVM -  Kernel-based VM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine)

## Основни концепции за виртуализацията

*Отново понятие за виртуализация:* Процес, който позволява hw ресурси да се споделят, използват едновременно от различни, отделени една от друга среди.
Всяка виртуализирана среда използва разпределените за нея ресурси като:
- Memory - Памет
- Processing power
- Storage
- ...

### VM & HV 