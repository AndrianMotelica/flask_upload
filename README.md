## About

[angular-file-upload](https://github.com/nervgh/angular-file-upload) module provides a good UX when it comes to file upload.
I wanted to create a loosely coupled system, having 2  independent containers imitating a [SOA](https://en.wikipedia.org/wiki/Service-oriented_architecture).

## Motivation

A [POW](https://en.wikipedia.org/wiki/Proof-of-work_system) Automated microservice system for uploading files; having **Flask** as a backend and **Angular** File Upload module for UI/UX.

## Installation

You need to have [docker](https://docs.docker.com/engine/installation/) & [docker-compose](https://docs.docker.com/compose/install/) installed.
In root folder of the project run 'docker-compose up -d', setup will take a while, go grab a coffee. (:

2 contianers will be spinned with [debian:jessie](https://www.debian.org/releases/jessie/), it provides containers with minimum viability for ~80% of developer's needed cases.
Both containers are bundled with Apache and expose port:80 mapped to 5001 and 5002 on host's machine.

Access http://localhost:5002, enjoy!

## Tests

Test flask's uploader application with a vanila HTML uploader @ **localhost:5002/test.html**. 
On success a serialized json response message will be returned.

If UI's container has console errors, please report.