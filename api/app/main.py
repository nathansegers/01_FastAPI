from fastapi import FastAPI

app = FastAPI()

birds = [
    {
      "id": "vink",
      "name": "Vink",
      "image": "https://www.natuurpunt.be/sites/default/files/vink.png",
      "short": "De vink is een bekende tuinvogel. De zang eindigt (bij ons) vaak op suskewiet.",
      "recon": [
        "14 - 16 cm, de grootte van een mus",
        "Mannetjes hebben een blauwgrijs petje, roestrode borst en witte vleugelstrepen (zie foto)",
        "Vrouwtjes zijn fletser gekleurd (lijkt op vrouwtje huismus)"
      ],
      "food": {
        "description": "De vink eet insecten. In het najaar en de winter wordt dit aangevuld met zaden en bladknoppen.",
        "what": "Wat voeder je: onkruidzaden, gemengd strooizaad, etensresten, zonnebloempitten",
        "where": "Waar voeder je: op de grond, op de voedertafel, aan de voederbuis"
      },
      "see": "Elke winter zakken ook heel wat vinken naar de tuinen af. Je ziet ze dan meestal op de grond, op zoek naar zaden die door andere vogels op de voedertafel werden gemorst."
    },
    {
      "id": "keep",
      "name": "Keep",
      "image": "https://www.natuurpunt.be/sites/default/files/images/inline/keep-man_r.png",
      "short": "De keep is de noordelijke tegenhanger van onze vink.",
      "recon": [
        "14 - 16 cm",
        "Opvallende oranje borst en witte buik",
        "Vaak in groep en in gezelschap van vinken"
      ],
      "food": {
        "description": "De keep komt bij ons enkel voor tussen oktober en begin april. In die periode worden vooral beukennootjes gegeten, maar ook granen en zaadjes van de berk.",
        "what": "Wat voeder je: onkruidzaden, gemengd strooizaad, etensresten, zonnebloempitten",
        "where": "Waar voeder je: op de grond, op de voedertafel, aan de voederbuis"
      },
      "see": "Elke winter zakken ook heel wat kepen naar de tuinen af. Je ziet ze dan meestal op de grond, op zoek naar zaden. Vooral in vorst- en sneeuwrijke winters kan het aantal tuinkepen hoog oplopen."
    }
]

users = [
    {
        "name": "Nathan Segers",
        "locationOfResidence": "Aalst",
        "age": 23,
        "gender": "M",
        "registrationDate": "15/09/2021"
    }
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/birds")
async def getBirds():
    return birds

@app.get("/users")
async def getUsers():
    return users