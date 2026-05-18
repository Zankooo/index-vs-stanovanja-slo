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

            <p>Glede na višino začetne investicije se izračuna, koliko kvadratnih metrov povprečnega rabljenega stanovanja v Ljubljani bi lahko kupili za ta znesek v določenem letu.</p>

            <br>

            <p>Nato se vrednost investicije izračunava podobno kot pri investiranju v indeks, saj se upošteva rast vrednosti kvadratnega metra skozi posamezna leta. Pri najemninah pa se predpostavi 4 % letni donos glede na vrednost stanovanja v posameznem letu. Če je bilo stanovanje v določenem letu vredno 200.000 €, se tako predpostavi, da je letna najemnina znašala 10.000 €.</p>

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
        Pri investiranju v stanovanja pa je teh spremenljivk še več – od stroškov pogodb in davkov do vzdrževanja ter prenov.
      </p>
        
    </section>
  </div>
</template>
