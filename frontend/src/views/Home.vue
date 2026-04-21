<script setup>
import { ref } from 'vue'
import { TrendingUp, Home as HomeIcon, ArrowRight, Loader2 } from 'lucide-vue-next'

const yearCount = ref('')
const amount = ref('')
const results = ref(null)
const loading = ref(false)

const handleSubmit = async () => {
  loading.value = true
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/izracun?leto=${yearCount.value}&kes=${amount.value}`);
    const data = await response.json();
    results.value = data.rezultati;
  } 
  catch (err) {
    console.error("Calculation failed", err);
  } finally {
      loading.value = false;
  }
}
</script>

<template>
  <div class="space-y-12">
    <section class="space-y-6">
      <div class="space-y-2">
        <h1 class="text-4xl font-light tracking-tight text-gray-900">
          Primerjajte svoje <span class="italic font-normal">investicije</span>
        </h1>
        <p class="text-gray-500 max-w-lg">
          Vnesite podatke za hitro primerjavo med investiranjem v delniške sklade (ETF) in nepremičnine na podlagi realnih zgodovinskih podatkov.
        </p>
      </div>

      <form @submit.prevent="handleSubmit" class="grid grid-cols-1 md:grid-cols-3 gap-6 items-end bg-white p-8 rounded-3xl shadow-sm border border-gray-100">
        <div class="space-y-2">
          <label class="text-[10px] uppercase tracking-widest font-bold text-gray-400">Leto nakupa (od 1990)</label>
          <input
            v-model="yearCount"
            type="number"
            class="w-full bg-gray-50 border-none rounded-xl px-4 py-3 focus:ring-2 focus:ring-black transition-all outline-none"
            placeholder="npr. 2010"
            min="1990"
            required
          />
        </div>
        <div class="space-y-2">
          <label class="text-[10px] uppercase tracking-widest font-bold text-gray-400">Investirani znesek (€)?</label>
          <input
            v-model="amount"
            type="number"
            class="w-full bg-gray-50 border-none rounded-xl px-4 py-3 focus:ring-2 focus:ring-black transition-all outline-none"
            placeholder="npr. 100000"
            required
          />
        </div>
        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-black text-white rounded-xl py-3 font-medium hover:bg-gray-800 transition-colors flex items-center justify-center gap-2 disabled:opacity-50"
        >
          <Loader2 v-if="loading" class="w-5 h-5 animate-spin" />
          <span v-else>Izračunaj</span>
          <ArrowRight v-if="!loading" class="w-4 h-4" />
        </button>
      </form>
    </section>

    <transition name="fade">
      <div v-if="results" class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Stanovanje Card -->
        <div class="bg-white rounded-[40px] p-8 shadow-sm border border-gray-100 space-y-6 flex flex-col">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-4">
              <div class="p-3 bg-orange-50 text-orange-600 rounded-2xl">
                <HomeIcon class="w-6 h-6" />
              </div>
              <div>
                <h2 class="text-xl font-medium text-gray-900">Stanovanje</h2>
                <p class="text-[10px] text-gray-400 uppercase tracking-widest font-bold">Ljubljana</p>
              </div>
            </div>
          </div>

          <div class="space-y-4 flex-grow">
            <div class="grid grid-cols-1 gap-3">
              <div class="p-4 bg-gray-50 rounded-2xl flex justify-between items-center">
                <p class="text-[10px] uppercase tracking-widest text-gray-400 font-bold">Kvadratura</p>
                <p class="text-sm font-medium text-gray-900">{{ results.stanovanje.kupljena_kvadratura }} m²</p>
              </div>
              <div class="p-4 bg-gray-50 rounded-2xl flex justify-between items-center">
                <p class="text-[10px] uppercase tracking-widest text-gray-400 font-bold">Rast cene</p>
                <p class="text-sm font-medium text-green-600">+{{ results.stanovanje.procentualna_rast_cene_stanovanja }}%</p>
              </div>
            </div>

            <div class="space-y-2 pt-2 border-t border-gray-50">
              <div class="flex justify-between items-center text-xs">
                <span class="text-gray-500 uppercase tracking-wide">Vrednost danes</span>
                <span class="font-medium text-gray-900">{{ results.stanovanje.vrednost_stanovanja_danes.toLocaleString('sl-SI') }} €</span>
              </div>
              <div class="flex justify-between items-center text-xs">
                <span class="text-gray-500 uppercase tracking-wide">Najemnine</span>
                <span class="font-medium text-gray-900 text-green-600">+ {{ results.stanovanje.zasluzek_od_vseh_najemnin.toLocaleString('sl-SI') }} €</span>
              </div>
            </div>
          </div>

          <div class="pt-4 mt-auto">
            <div class="flex justify-between items-center bg-gray-900 text-white p-5 rounded-2xl">
              <p class="text-[10px] uppercase tracking-widest opacity-60 font-bold">Skupni zaslužek</p>
              <p class="text-xl font-light">{{ results.stanovanje.skupni_zasluzek.toLocaleString('sl-SI') }} €</p>
            </div>
            <p class="mt-4 text-[13px] text-gray-400 italic leading-relaxed">
              *Za najemnino se upošteva 5 % vrednosti stanovanja tistega leta. Davki in morebitni stroški obnove še niso vključeni v izračun.
            </p>
          </div>
         
        </div>

        <!-- S&P 500 Card -->
        <div class="bg-white rounded-[40px] p-8 shadow-sm border border-gray-100 flex flex-col">
          <div class="flex items-center gap-4 mb-6">
            <div class="p-3 bg-blue-50 text-blue-600 rounded-2xl">
              <TrendingUp class="w-6 h-6" />
            </div>
            <div>
              <h2 class="text-lg font-medium text-gray-900 leading-tight">S&P 500</h2>
              <p class="text-[10px] text-gray-400 uppercase tracking-widest font-bold">Total Return</p>
            </div>
          </div>

          <div class="space-y-4 flex-grow">
            <div class="grid grid-cols-1 gap-3">
              <div class="p-4 bg-gray-50 rounded-2xl flex justify-between items-center">
                <p class="text-[10px] uppercase tracking-widest text-gray-400 font-bold">Deleži (enot)</p>
                <p class="text-sm font-medium text-gray-900">{{ results.sp500.kupljenih_enot }}</p>
              </div>
              <div class="p-4 bg-gray-50 rounded-2xl flex justify-between items-center">
                <p class="text-[10px] uppercase tracking-widest text-gray-400 font-bold">Donos indeksa</p>
                <p class="text-sm font-medium text-green-600">+{{ results.sp500.donos_indeksa_procent }}%</p>
              </div>
            </div>

            <div class="space-y-2 pt-2 border-t border-gray-50">
              <div class="flex justify-between items-center text-xs">
                <span class="text-gray-500 uppercase tracking-wide">Vrednost danes</span>
                <span class="font-medium text-gray-900">{{ results.sp500.vrednost_nase_investicije_danes.toLocaleString('sl-SI') }} €</span>
              </div>
              <div class="flex justify-between items-center text-xs">
                <span class="text-gray-500 uppercase tracking-wide">Dividende</span>
                <span class="text-[12px] text-gray-400 italic">Že vključene</span>
              </div>
            </div>
          </div>

          <div class="pt-4 mt-auto">
            <div class="flex justify-between items-center bg-gray-900 text-white p-5 rounded-2xl">
              <p class="text-[10px] uppercase tracking-widest opacity-60 font-bold">Skupni zaslužek</p>
              <p class="text-xl font-light">{{ results.sp500.skupni_zasluzek.toLocaleString('sl-SI') }} €</p>
            </div>
          </div>
          <p class="mt-4 text-[13px] text-gray-400 italic leading-relaxed">
              *Glede na to da gre za pasivno investiranje v izračun niso upoštevani stroški posredniškega računa in ostalih morebitnih minornih stroškov.
          </p>
        
        
        </div>
      </div>
    </transition>
  </div>
</template>
