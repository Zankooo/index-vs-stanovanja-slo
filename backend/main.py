
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Za razvoj dovolimo vse, kasneje lahko omejimo na 3001
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    print("Hello World!")
    return {"message": "Živijo, svet! To je moj prvi FastAPI."}


def stanovanja_funkcija(katerega_leta, koliko_kesa):
    katerega_leta = str(katerega_leta)
    with open('cene-stanovanj.json') as datoteka:
        podatki = json.load(datoteka)

    if katerega_leta not in podatki:
        return {"napaka": f"Ni podatkov za leto {katerega_leta}."}
    
    # cena kvadrata takrat
    cena_kvadrat_takrat = podatki[katerega_leta]['value']
    # koliko kvadrature si kupu 
    kupljena_kvadratura = int(koliko_kesa) / cena_kvadrat_takrat
    # torej 2026
    zadnje_leto = list(podatki.keys())[-1]
    # cena 2026
    cena_kvadrat_zdaj = podatki[zadnje_leto]['value']
    # koliko je stan zdej vreden
    cena_stana_zdej = kupljena_kvadratura * cena_kvadrat_zdaj

    # koliko smo zasluzl po kvadratu
    # kolk smo zasluzs = 300 000 - 150 000
    zasluzek = cena_stana_zdej - int(koliko_kesa)
    # procentualno kolk je kvadrat zrastu
    rast = (cena_stana_zdej / int(koliko_kesa) - 1) * 100

    # najemnine: 5% od vrednosti kvadrata vsako leto
    najemnine_skupaj = 0
    for leto, leto_podatki in podatki.items():
        leto_num = int(leto)
        if int(katerega_leta) < leto_num <= int(zadnje_leto):
            # vrednost stanovanja pomnozimo z 5%
            vrednost_stana_tega_leta = kupljena_kvadratura * leto_podatki['value']
            najemnine_skupaj += vrednost_stana_tega_leta * 0.04

    return {
        "tip": "STANOVANJE",
        "leto_nakupa": katerega_leta,
        "cena_kvadrat_takrat": cena_kvadrat_takrat,
        "kupljena_kvadratura": round(kupljena_kvadratura, 2),
        "cena_kvadrat_zdaj": cena_kvadrat_zdaj,
        "zadnje_leto": zadnje_leto,
        "vrednost_stanovanja_danes": round(cena_stana_zdej, 0),
        "koliko_je_stan_dobil_na_ceni": round(zasluzek, 0),
        "procentualna_rast_cene_stanovanja": round(rast, 1),
        "zasluzek_od_vseh_najemnin": round(najemnine_skupaj, 0),
        "skupni_zasluzek": round(zasluzek + najemnine_skupaj, 0)
    }


def indeks_funkcija(katerega_leta, koliko_kesa):
    katerega_leta = str(katerega_leta)
    with open('sp500tr.json') as datoteka:
        podatki = json.load(datoteka)

    if katerega_leta not in podatki:
        return {"napaka": f"Ni podatkov za leto {katerega_leta}."}

    zadnje_leto = list(podatki.keys())[-1]

    katerega_leta_vrednost = podatki[katerega_leta]['value']
    zadnje_leto_vrednost = podatki[zadnje_leto]['value']

    koliksen_delez_kupil = int(koliko_kesa) / katerega_leta_vrednost
    vrednost_danes = koliksen_delez_kupil * zadnje_leto_vrednost


    skupni_donos = ((zadnje_leto_vrednost - katerega_leta_vrednost) / katerega_leta_vrednost) * 100
    zasluzek = vrednost_danes - int(koliko_kesa)
    
    return {
        "tip": "S&P 500",
        "leto_nakupa": katerega_leta,
        "vrednost_indeksa_takrat": katerega_leta_vrednost,
        "kupljenih_enot": round(koliksen_delez_kupil, 2),
        "zadnje_leto": zadnje_leto,
        "vrednost_indeksa_zdaj": zadnje_leto_vrednost,
        "vrednost_nase_investicije_danes": round(vrednost_danes, 0),
        "donos_indeksa_procent": round(skupni_donos, 1),
        "skupni_zasluzek": round(zasluzek, 0),
        
    }




@app.get("/api/izracun")
def izracun(leto: int, kes: int):
    stanovanje = stanovanja_funkcija(leto, kes)
    indeks = indeks_funkcija(leto, kes)
    
    return {
        "vhodni_podatki": {
            "leto": leto,
            "investicija": kes
        },
        "rezultati": {
            "stanovanje": stanovanje,
            "sp500": indeks
        }
    }

