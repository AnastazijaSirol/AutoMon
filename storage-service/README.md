# Storage Service

Storage-service je centralni mikroservis koji prima MQTT poruke sa svih ostalih servisa i sprema ih u SQLite bazu `traffic.db`.

## Pokretanje

```
cd storage-service
docker-compose up --build
docker-compose up
```