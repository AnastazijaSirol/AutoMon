# AutoMon

AutoMon je distribuirana aplikacija sastavljena od više mikroservisa koji zajedno simuliraju prometni sustav na sutocesti Pula-RIjeka-Umag. Sustav koristi MQTT za komunikaciju između servisa i SQLite bazu za pohranu događaja.

Aplikacija se sastoji od šest mikroservisa:

# Dijelovi aplikacije

1. storage-service
Centralni servis koji prima MQTT poruke od svih ostalih servisa i sprema ih u SQLite bazu traffic.db.

2. entrance-service
Simulira ulazak vozila na autocestu i šalje podatke preko MQTT-a.

3. camera-service
Simulira prolazak vozila pored kamera i i šalje podatke preko MQTT-a.

4. exit-service
Simulira izlazak vozila s autoceste i šalje podatke preko MQTT-a.

5. restarea-service
Simulira zaustavljanje vozila na odmorištima i šalje podatke preko MQTT-a.

6. analytics-service
CLI aplikacija koji čita SQLite bazu i prikazuje analitičke izvještaje.

# Pokretanje aplikacije

```
docker-compose up --build
docker-compose up
docker-compose run analytics-service
```

Svaki mikroservis može raditi samostalno bez ostatka sustava.