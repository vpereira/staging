osc plugin to play with the new staging endpoint

to build it:

```
docker build -ti $USER/staging .
```

to run it:

```
docker run -ti  --network="open-build-service_default" -v $PWD:/root/.osc-plugins $USER/staging bash
```

note that i attach it to a running docker-compose instance from the
opensuse-buildservice, being able to ping frontend, db, etc

a default oscrc for the development opensuse-buildservice is as well copied
to allow us to call osc directly


How to play around:

Assuming that you have a staging workflow with home:Admin as main project and
(home:Admin:Staging:A and home:Admin:Staging:B) as staging projects you can:


list all staging projects belonging to a staging workflow:


```
osc staging staging_projects -m home:Admin
```


select/stage request 1, in the staging project home:Admin:Staging:A, from the
staging workflow, connected with main proejct home:Admin


```
osc staging stage_request -r 1 -m home:Admin -p home:Admin:Staging:A
```

list all staged requests, for a specific staging project:


```
osc staging staged_requests -m home:Admin -p home:Admin:Staging:A
```

see a specific staging project:

```
osc staging staging_projects -m home:Admin -p home:Admin:Staging:A
```

push a request to the excluded_requests:

```
osc staging excluded_requests_create -m home:Admin -r 2
```

remove a request from the excluded_requests:

```
osc staging excluded_requests_delete -m home:Admin -r 2

```

IMPORTANT:

- please do not open issue. if you want to contribute, do a pull request.
- its not production ready, its just a playground to play with the new API
  endpoints
- use at your own risk


![](staging.png)
