<script setup>
import { Info, Calculator, Lightbulb, Home as HomeIcon, Database } from 'lucide-vue-next'

const podatki = [
  { leto: 1990, sp500: 367, stanovanje: 900 },
  { leto: 1991, sp500: 479, stanovanje: 950 },
  { leto: 1992, sp500: 516, stanovanje: 1000 },
  { leto: 1993, sp500: 568, stanovanje: 1050 },
  { leto: 1994, sp500: 575, stanovanje: 1100 },
  { leto: 1995, sp500: 792, stanovanje: 1200 },
  { leto: 1996, sp500: 1034, stanovanje: 1250 },
  { leto: 1997, sp500: 1298, stanovanje: 1300 },
  { leto: 1998, sp500: 1670, stanovanje: 1350 },
  { leto: 1999, sp500: 2021, stanovanje: 1400 },
  { leto: 2000, sp500: 1837, stanovanje: 1450 },
  { leto: 2001, sp500: 1618, stanovanje: 1500 },
  { leto: 2002, sp500: 1261, stanovanje: 1600 },
  { leto: 2003, sp500: 1622, stanovanje: 1700 },
  { leto: 2004, sp500: 1799, stanovanje: 1850 },
  { leto: 2005, sp500: 1887, stanovanje: 2000 },
  { leto: 2006, sp500: 2186, stanovanje: 2300 },
  { leto: 2007, sp500: 2306, stanovanje: 2700 },
  { leto: 2008, sp500: 1452, stanovanje: 2660 },
  { leto: 2009, sp500: 1837, stanovanje: 2390 },
  { leto: 2010, sp500: 2117, stanovanje: 2420 },
  { leto: 2011, sp500: 2158, stanovanje: 2440 },
  { leto: 2012, sp500: 2504, stanovanje: 2320 },
  { leto: 2013, sp500: 3315, stanovanje: 2080 },
  { leto: 2014, sp500: 3769, stanovanje: 2020 },
  { leto: 2015, sp500: 3821, stanovanje: 2040 },
  { leto: 2016, sp500: 4278, stanovanje: 2180 },
  { leto: 2017, sp500: 5212, stanovanje: 2410 },
  { leto: 2018, sp500: 5478, stanovanje: 2770 },
  { leto: 2019, sp500: 6553, stanovanje: 2800 },
  { leto: 2020, sp500: 7759, stanovanje: 2960 },
  { leto: 2021, sp500: 9986, stanovanje: 3591 },
  { leto: 2022, sp500: 8178, stanovanje: 3935 },
  { leto: 2023, sp500: 10327, stanovanje: 4268 },
  { leto: 2024, sp500: 12991, stanovanje: 4237 },
  { leto: 2025, sp500: 15220, stanovanje: 4783 },
  { leto: 2026, sp500: 16935, stanovanje: 5000 },
]
</script>

<template>
  <div class="space-y-16">
    <section class="space-y-6">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-black text-white text-[10px] uppercase font-bold tracking-widest">
        <Info class="w-3 h-3" />
        <span>O projektu</span>
      </div>
      <p class="text-3xl font-light tracking-tight leading-tight max-w-2xl text-gray-900">
        Kako delujejo <span class="italic font-normal">izračuni?</span>
      </p>
      <p class="text-lg text-gray-500 max-w-2xl leading-relaxed">
        Namen tega kalkulatorja je ponuditi poenostavljeno primerjavo med dvema najbolj priljubljenima oblikama dolgoročnega investiranja v Sloveniji:
      </p>
    </section>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 pt-8">
      <!-- ETF Card -->
      <div class="bg-white p-8 rounded-[40px] shadow-sm border border-gray-100 space-y-5">
        <div class="flex items-center gap-3">
          <div class="p-2.5 bg-blue-50 text-blue-600 rounded-2xl">
            <Calculator class="w-5 h-5" />
          </div>
          <h3 class="text-xl font-medium text-gray-900">ETF (S&P 500)</h3>
        </div>
        <p class="text-gray-500 text-sm leading-relaxed">
          Kot investicija v delnice se upoštevajo donosi indeksa S&P 500 Total Return Index (^SP500TR). Gre za indeks, ki že vključuje reinvestirane dividende. Ker gre za pasivno investiranje z enkratnim nakupom, v izračunu izpustimo stroške posredniškega računa in morebitne druge stroške, saj predstavljajo le manjši znesek v primerjavi s celotno investicijo, hkrati je pa namen prikazati informativen izračun.
        </p>
        <p class="text-gray-500 text-sm leading-relaxed">
          Kako poteka izračun v ozadju? Če izberemo leto 2010, se potem vzame donos indeksa od decembra 2010 do danes (2026 april). Ta donos se nato pomnoži z zneskom, ki smo ga investirali.
        </p>
      </div>

      <!-- Real Estate Card -->
      <div class="bg-white p-8 rounded-[40px] shadow-sm border border-gray-100 space-y-5">
        <div class="flex items-center gap-3">
          <div class="p-2.5 bg-orange-50 text-orange-600 rounded-2xl">
            <HomeIcon class="w-5 h-5" />
          </div>
          <h3 class="text-xl font-medium text-gray-900">Nepremičnine</h3>
        </div>
        <div class="text-gray-500 text-sm leading-relaxed">
          <p>Investiranje v stanovanje poteka na naslednji način.</p>
            <br>

            <p>Glede na višino začetne investicije se izračuna, koliko kvadratnih metrov povprečnega rabljenega stanovanja v Ljubljani bi lahko kupili za ta znesek ob koncu izbranega leta.</p>

            <br>

            <p>Nato se vrednost investicije izračunava podobno kot pri investiranju v indeks, saj se upošteva rast vrednosti kvadratnega metra skozi posamezna leta. Pri najemninah pa se predpostavi 4 % letni donos glede na vrednost stanovanja v posameznem letu. <i>Primer:</i> Če je bilo stanovanje v določenem letu vredno 200.000 €, se tako predpostavi, da je letna najemnina znašala 8.000 €.</p>

            <br>

            <p>Pomembno je omeniti, da v izračun niso vključeni davki na najemnino, ki znašajo približno 25 %, prav tako pa niso upoštevani morebitni stroški obnove. Pri teh se običajno priporoča upoštevanje letnega stroška v višini 0,5–1,5 % vrednosti stanovanja v posameznem letu.</p>

            <br>

            <p>Zanimiv dodaten izračun bi bil tudi, če bi bilo mogoče prejete najemnine sproti reinvestirati, podobno kot se pri investiranju v indeks samodejno reinvestirajo dividende.</p>
        </div>
      </div>
    </div>

    <section class="bg-white p-10 rounded-[40px] shadow-sm border border-gray-100 space-y-6">
      <div class="flex items-center gap-3">
        <div class="p-2 bg-yellow-50 rounded-xl">
          <Lightbulb class="text-yellow-600 w-6 h-6" />
        </div>
        <h2 class="text-2xl font-light text-gray-900">Pomembno opozorilo</h2>
      </div>
      <p class="text-gray-600 leading-relaxed text-sm">
        Vsi izračuni so informativne narave in temeljijo na zgodovinskih povprečjih. Točne izračune je praktično nemogoče izračunati. </p>
      
      <p class="text-gray-600 leading-relaxed text-sm">
        Pri investiranju v delnice nastane tudi nekaj manjših stroškov, ki se precej razlikujejo glede na to, katerega posrednika izberemo.
      </p>
      
      <p class="text-gray-600 leading-relaxed text-sm">
        Pri investiranju v stanovanja pa je teh spremenljivk še več – od stroškov pogodb in davkov do vzdrževanja stanovanja...
      </p>
    </section>
        
    <section class="bg-white p-10 rounded-[40px] shadow-sm border border-gray-100 space-y-6">
      <div class="flex items-center gap-3">
        <div class="p-2 bg-purple-50 rounded-xl">
          <Database class="text-purple-600 w-6 h-6" />
        </div>
        <h2 class="text-2xl font-light text-gray-900">Uporabljeni podatki</h2>
      </div>
      <p class="text-gray-600 leading-relaxed text-sm">
        Spodaj so prikazani surovi zgodovinski podatki, ki se uporabljajo pri izračunih znotraj kalkulatorja. Podatki za stanovanja so pridobljeni primarno iz 
        <a href="https://www.e-prostor.gov.si/podrocja/trg-in-vrednosti-nepremicnin/trg-nepremicnin/" target="_blank" rel="noopener noreferrer" style="color: blue; text-decoration: underline;">
            E-Prostor
        </a>
        <br>
        Podatki za vrednosti indeksa S&P 500 TR pa so pridobljeni iz portala
        <a href="https://finance.yahoo.com/quote/%5ESP500TR/history/?period1=568305000&period2=1780230324" target="_blank" rel="noopener noreferrer" style="color: blue; text-decoration: underline;">
            Yahoo Finance
        </a>
      </p>
      
      <div class="overflow-x-auto rounded-2xl border border-gray-100 max-h-96">
        <table class="w-full text-sm text-left table-fixed">
          <thead class="text-xs text-gray-500 uppercase bg-gray-50 sticky top-0">
            <tr>
              <th scope="col" class="w-1/3 px-6 py-4 font-medium">Leto</th>
              <th scope="col" class="w-1/3 px-6 py-4 font-medium text-center">S&P 500 TR</th>
              <th scope="col" class="w-1/3 px-6 py-4 font-medium text-right">Stanovanje (m²)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            <tr v-for="vrstica in podatki" :key="vrstica.leto" class="hover:bg-gray-50/50 transition-colors">
              <td class="px-6 py-4 text-gray-900 font-medium">{{ vrstica.leto }}</td>
              <td class="px-6 py-4 text-gray-600 text-center">{{ vrstica.sp500 }}</td>
              <td class="px-6 py-4 text-gray-600 text-right">{{ vrstica.stanovanje }} €</td>
            </tr>
          </tbody>
        </table>
      </div>

    </section>


  </div>
</template>
