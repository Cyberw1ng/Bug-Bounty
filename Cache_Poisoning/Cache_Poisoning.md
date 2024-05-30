# What is cache poisoning?

A Technique whereby an Attacker exploits the behavior of web server and cache so that a harmful HTTP response is server to other users.

Involve 2 Phases:
1. Find out how to bring out a response from the server that unintentionally contains some kind of dangerous payload
2. To make sure that their response is cached and subsequently server to the intended victims.

Impacts:
This leads to different attacks such as XSS, Javascript Injection, Open Redirection and so on.
