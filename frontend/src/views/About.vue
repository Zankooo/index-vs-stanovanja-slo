<script setup>
import { Info, Calculator, Lightbulb, Home as HomeIcon } from 'lucide-vue-next'
</script>

<template>
  <div class="space-y-16">
    <section class="space-y-6">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-black text-white text-[10px] uppercase font-bold tracking-widest">
        <Info class="w-3 h-3" />
        <span>O projektu</span>
      </div>
      <p class="text-3xl font-light tracking-tight leading-tight max-w-2xl text-gray-900">
        Kako delujejo naši <span class="italic font-normal">izračuni?</span>
      </p>
      <p class="text-lg text-gray-500 max-w-2xl leading-relaxed">
        Namen tega kalkulatorja je ponuditi poenostavljeno primerjavo med dvema najbolj priljubljenima oblikama dolgoročnega investiranja v Sloveniji.
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
          Kot investicija v delnice se vzamejo donosi S&P 500 Total Return(^SP500TR). To je ETF, ki že ima reinvestirane dividende. Ker gre za pasivno investiranje z enkratnim nakupom, v izračunu izpustimo strošeke posredniškega računa in morebitnih drugih stroškov saj so to le minoren znesek v primerjavi z celotno investicijo.
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
          <p>Investiranje v stanovanje pa je tako. </p>
          <br>
          <p>Glede na to koliko denarja smo investirali se izračuna koliko kvadratov stanovanja smo  lahko kupili za ta denar tistega leta - povprečnega rabljenega stanovanja v Ljubljani.</p>
          <br>
          <p>Potem pa se cena za kvadrat izračunava podobno kot pri investiranju v S&P 500. Kolikor je pač kvadratni meter pridobil v vseh letih. Glede najemnin se pa vzame 5% letno glede na vrednost stanovanje tistega leta. Torej če je stanovanje nekega leta vredno 200.000eur se vzame da je bila letna najemina takrat 10.000eur.</p>
          <br>
          <p>Pomembno je omeniti da smo v izračun spustili davke na najemnino ki znašajo cca 25% in morebitne obnove, za katere se priporoča upoštevati 0,5-1,5% letno glede na vrednost stanovanja tisto leto. </p>
          <br>
          <p>Zanimiv izračun bi pa tudi bil, če bi lahko zaslužene najemnine naprej investirali, tako kot se investira denar naprej samodejno pri investiranju v indeks. </p>
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
      
      <p class="text-gray-600 leading-relaxed text-sm"> Investiranju v delnice je kar nekaj manjhnih stroškov, ki se precej razlikujejo glede na to katerega posredniak imamo.</p>
      
        <p class="text-gray-600 leading-relaxed text-sm">
        Pri investiranju v stanovanja je pa teh spremenljivk še več. Vseh stroškov pogodb, davkov, prenov... 

      </p>
        
    </section>
  </div>
</template>
