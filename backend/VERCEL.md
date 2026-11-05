# Selitev backenda z Renderja na Vercel

Frontend in backend sta dva Vercel projekta, povezana z istim Git repozitorijem.
Render naj ostane aktiven, dokler novi backend in frontend nista preverjena.

## 1. Pošlji spremembe v GitHub

V korenski mapi repozitorija:

```sh
git add backend/main.py backend/requirements.txt backend/.python-version backend/VERCEL.md
git commit -m "Prepare FastAPI backend for Vercel"
git push
```

JSON datoteki morata biti vključeni v repozitorij. Aplikacija ju bere glede na
lokacijo `main.py`, zato ni odvisna od delovne mape procesa. Seznam odvisnosti
vsebuje FastAPI in Uvicorn (za lokalni zagon in obstoječi Render).

## 2. Ustvari projekt za backend

Na Vercelu izberi **Add New / Create New → Project** in ponovno uvozi isti
GitHub repozitorij kot za frontend.

| Nastavitev | Vrednost |
| --- | --- |
| Project Name | Na primer `index-vs-stanovanja-api` |
| Root Directory | `backend` |
| Framework Preset | `FastAPI` |
| Build Command | Privzeto, brez ročnega override |
| Output Directory | Privzeto, brez ročnega override |
| Install Command | Privzeto, odvisnosti iz `requirements.txt` |

Klikni **Deploy**. Vercel naloži `app` iz `main.py`; ukaza `uvicorn` ne vpisuj
kot Build Command. Python različico določa `.python-version`.

## 3. Preveri backend

Uporabi stalno produkcijsko domeno novega projekta, ne URL-ja posamezne
predogledne objave. Odpri:

```text
https://TVOJ-BACKEND.vercel.app/api/izracun?leto=2020&kes=10000
```

Zamenjaj `TVOJ-BACKEND` z dejansko domeno. Pričakovan je JSON z
`rezultati.stanovanje` in `rezultati.sp500`. Na primer vrednost stanovanja
18919 in vrednost indeksa 21440 pri trenutnih lokalnih podatkih.
Lokalni JSON datoteki se razlikujeta od podatkov, ki jih je ob preverjanju vrnil
Render; nova objava bo uporabljala podatke iz objavljenega Git commita.

Preizkusi tudi v zasebnem oknu brez prijave v Vercel. API mora biti javno
dostopen. Če zahteva prijavo, v nastavitvah **Deployment Protection** prilagodi
zaščito produkcije za ta javni API. Zaščite predogledov ni treba spreminjati.

## 4. Preklopi frontend

V obstoječem frontend projektu odpri **Settings → Environment Variables**.
Shrani dosedanjo vrednost `VITE_API_URL` za morebitno vrnitev, nato za okolje
**Production** nastavi:

```text
VITE_API_URL=https://TVOJ-BACKEND.vercel.app
```

Uporabi samo osnovni URL brez končnega `/` in brez `/api/izracun`.
Če želiš novi API tudi v predogledih frontenda, nastavi še **Preview**.

V **Deployments** ponovno objavi frontend (**Redeploy**), da se spremenljivka
vključi v novo gradnjo. Sama sprememba spremenljivke obstoječe objave ne spremeni.

## 5. Preveri preklop in nato ustavi Render

Na javnem frontendu izračunaj leto 2020 in znesek 10000. V orodjih brskalnika
pod **Network** preveri, da `/api/izracun` kliče novo Vercel domeno in vrne 200.
Trenutna CORS nastavitev backenda dovoljuje klice frontenda tudi na novi domeni.

Šele po uspešnem preverjanju ustavi storitev na Renderju. Če preklop ne deluje,
vrni `VITE_API_URL` na `https://index-vs-apartment-slo.onrender.com` in ponovno
objavi frontend, medtem ko je Render še aktiven.

Uradna navodila:

- https://vercel.com/docs/frameworks/backend/fastapi
- https://vercel.com/docs/functions/runtimes/python
- https://vercel.com/docs/monorepos
