# Мрежова и информационна сигурност
Kuzmin.petar@gmail.com

## Записки от часа
Client-server модел по http има правила (req, res)

Req от client (get) - за файл (пр: .html), за да се визуализира в browser

- GET - client искат информация от сървъра;
- POST

Burp Suite - виждат се req и res; Видове атаки, в които се променя user_id на заявката и директо може да се влезне в профил на друг човек (за това се използва Burp Suite)


Скенери - събира информация за даден сайт или организация.

Една от първите стъпки при pen test:

- Vulnerability: Автоматизиран scan и оценяване на резултатите

Скенери:
- Nessus - 32 IP безплатно
- Nexpose

За browsers:
- Burp Suite - всички заявки минават през него -> export на log-овете

За контролното и изпитване:
- OS detection (Разбери как работи - проучи nmap)
```console
emi@debian:nmap -O 95.43.233.245
```
```console
emi@debian:nmap -A 95.43.233.245
```
- TCP и UDP Scan, по default какъв е scan-a, портове
- Сканиране на router
## Nmap IP scan 
IP адреси: 95.43.233.245 и 95.43.223.245

С nmap да бъдат сканирани портове / търсене на кои портове са отворени и уязвимости. Трябва да бъдат предоставени screenshot-и и да бъдат описани.

Доклад: https://docs.google.com/document/d/1Xs7_lLW_lZq5tIOjysH1DEg3HodW6HxdOtCWZLeah0o/edit?usp=sharing

Структура:
- Заглавна страница - име, версия...
- Съдържание -table of content
- От дата до дата (Кога са извършени тестовете)+scope IP адреси

Описание на nmap:
- Nmap A4, A3
- Команди, да бъдат разгледени различните опции и функционалности
- Извършеното сканиране с nmap
- Приложени фигури и тяхното детайлно описание
- Какво е намеренo

Относно форматирането:
- Normal Text: 13
- Фигури: шрифт 12
- Главите са с : Heading 2 - шрифт 16
- Подглави: Heading 3 - шрифт 15
- Heading 1 e за заглавия

1. Check for live systems
```console
emi@debian:nslookup 95.43.233.245
```
```console
emi@debian:nmap -sP 95.43.233.245
```
2. Check for open ports
```console
emi@debian:nmap 95.43.233.245
```
3. Perform banner grabbing
```console
emi@debian:nmap -sV 95.43.233.245
```
```console
emi@debian:nmap -O 95.43.233.245
```
```console
emi@debian:nmap -A 95.43.233.245
```
4. Vulnerability Scan
```console
emi@debian:nmap --script vuln 95.43.233.245
```

## Домашнo Nessus сканиране на host машина
tenable

Инструкции за инсталация на Nessus essentials 

New Scan / Advanced scan

Предоставяне на credentials за стартиране - в зависимост от това на каква машина се прави
За Windows - username, passwords регистри, портове, firewalls

Nessus credentialed check on Windows
Troubleshoоting 

Ако scan-а e успешнo минал - results:
- да са показали pass - plugin type

### Изисквания за документацията (допълване към стария report):
- Как е изтеглен nessus
- Какво е authentic scan
- Съпоствавка с authentic и без authentic scan (разлики)
- Изпълнени стъпки за authentic scan: портове (nessus оперира на конкретни портове), firewall
- Доказателство на конкретните plugin-и (включително и за SMP протокола), че функционира правилно и са минали
- Може да се опише и премахната уязвимост
- Пак колко време е отнело (с писането на report-a)

Отново срок: до сряда на имейл, нова версия и pdf


