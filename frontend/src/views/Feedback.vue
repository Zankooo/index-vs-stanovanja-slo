<script setup>
import { ref } from 'vue'
import { MessageSquare, Send, CheckCircle, AlertCircle, Lightbulb } from 'lucide-vue-next'

const sporocilo = ref('')
const status = ref('idle') // idle | sending | success | error

async function poslji() {
  if (!sporocilo.value.trim()) return

  status.value = 'sending'

  try {
    const response = await fetch('https://api.emailjs.com/api/v1.0/email/send', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        service_id: 'service_c10t16i',
        template_id: 'template_6xqtrc4',
        user_id: 'l3RlUEoMjzngvsDe3',
        template_params: {
          name: 'Anonimni uporabnik',
          time: new Date().toLocaleString('sl-SI'),
          message: sporocilo.value,
        }
      })
    })

    if (response.ok) {
      status.value = 'success'
      sporocilo.value = ''
    } else {
      status.value = 'error'
    }
  } catch (error) {
    status.value = 'error'
  }
}
</script>

<template>
  <div class="space-y-16">

    <!-- Header -->
    <section class="space-y-6">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-black text-white text-[10px] uppercase font-bold tracking-widest">
        <MessageSquare class="w-3 h-3" />
        <span>Povratne informacije</span>
      </div>
      <p class="text-3xl font-light tracking-tight leading-tight max-w-2xl text-gray-900">
        Imaš <span class="italic font-normal">predlog o izboljšavi?</span>
      </p>
      <p class="text-lg text-gray-500 max-w-2xl leading-relaxed">
        Si opazil kakšno napako ali pa imaš samo idejo o morebitni izboljšavi. Sporoči mi spodaj.
      </p>
    </section>

    <!-- Form card -->
    <div class="bg-white p-8 sm:p-10 rounded-[40px] shadow-sm border border-gray-100">

      <!-- Success -->
      <div v-if="status === 'success'" class="flex flex-col items-center gap-4 py-12 text-center">
        <div class="p-4 bg-green-50 rounded-full">
          <CheckCircle class="w-10 h-10 text-green-500" />
        </div>
        <h3 class="text-xl font-medium text-gray-900">Sporočilo poslano!</h3>
        <p class="text-gray-500 text-sm max-w-sm">Hvala za tvoj predlog!</p>
        <button
          @click="status = 'idle'"
          class="mt-4 px-6 py-2.5 rounded-full border border-gray-200 text-sm font-medium text-gray-600 hover:bg-gray-50 transition-colors"
        >
          Pošlji novo sporočilo
        </button>
      </div>

      <!-- Form -->
      <template v-else>
        <div class="space-y-6">
          <textarea
            v-model="sporocilo"
            rows="6"
            placeholder="Opiši svojo idejo ali napako..."
            class="w-full px-4 py-3 rounded-2xl border border-gray-200 bg-gray-50 text-sm text-gray-800 placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:border-transparent transition resize-none"
          />

          <div v-if="status === 'error'" class="flex items-center gap-2 p-4 rounded-2xl bg-red-50 text-red-600 text-sm">
            <AlertCircle class="w-4 h-4 shrink-0" />
            <span>Pošiljanje ni uspelo. Poskusite znova.</span>
          </div>

          <div class="flex justify-end">
            <button
              @click="poslji"
              :disabled="!sporocilo.trim() || status === 'sending'"
              class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-gray-900 text-white text-sm font-medium hover:bg-gray-700 disabled:opacity-40 disabled:cursor-not-allowed transition-all"
            >
              <span v-if="status === 'sending'">Pošiljam...</span>
              <span v-else>Pošlji</span>
              <Send class="w-4 h-4" />
            </button>
          </div>
        </div>
      </template>

    </div>

    <!-- Kaj nas zanima -->
    <div class="bg-white p-8 sm:p-10 rounded-[40px] shadow-sm border border-gray-100 space-y-5">
      <div class="flex items-center gap-3">
        <div class="p-2 bg-yellow-50 rounded-xl">
          <Lightbulb class="text-yellow-600 w-5 h-5" />
        </div>
        <h2 class="text-lg font-medium text-gray-900">Kaj me zanima?</h2>
      </div>
      <ul class="text-sm text-gray-500 space-y-3 leading-relaxed">
        <li class="flex items-start gap-2"><span class="text-gray-300 mt-0.5">→</span> Napake v izračunih ali logiki</li>
        <li class="flex items-start gap-2"><span class="text-gray-300 mt-0.5">→</span> Napačni ali zastareli podatki</li>
        <li class="flex items-start gap-2"><span class="text-gray-300 mt-0.5">→</span> Predlogi za dodatne scenarije (npr. mesečno vlaganje)</li>
        <li class="flex items-start gap-2"><span class="text-gray-300 mt-0.5">→</span> Ideje za nove funkcionalnosti</li>
        <li class="flex items-start gap-2"><span class="text-gray-300 mt-0.5">→</span> Karkoli, kar bi naredilo kalkulator boljši</li>
      </ul>
    </div>

  </div>
</template>
