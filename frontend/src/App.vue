<!-- index.html -> main.js -> App.vue 
 
main
- uvozi knjiznice 
- primarno definira path -> kaj se prikaze ko je nek path
- zacene in montira aplikacijo

App.vue
- prvi vstop v vizualno podobo aplikacije
- vrhovni file vizualne podobe
- vse ostale komponente se prikazujejo znotraj nje (vgnezdene). To je kot neko ogrodje za celo aplikacijo
- na vsaki strani se prikaze to kar je v App.vue -> torej to je pametna praksa:
- ce imamo navbar in recimo footer ko hocemo da se skozi pojavljala cez aplikacijo - kar je pogosto
- ce imamo recimo po celi aplikaciji isti padding, pisavo, margin, enaka animacija.. je to dobra praksa



-->

<template>
  <div class="min-h-screen bg-[#f5f5f5] text-[#4a4a4a] font-sans selection:bg-gray-200 flex flex-col">
    
    <!-- HEADER-->
    <header class="w-full px-6 sm:py-8 py-6 bg-white/50 backdrop-blur-sm sticky top-0 z-10 border-b border-gray-100">
      <div class="max-w-4xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-4 sm:gap-0">
        <router-link to="/" class="text-xl font-medium tracking-tight hover:opacity-70 transition-opacity">
          Investicijski<span class="font-light">Kalkulator</span>
        </router-link>
        <nav class="flex gap-6 sm:gap-8 text-[10px] sm:text-sm font-medium uppercase tracking-widest">
          <router-link to="/" class="hover:opacity-60 transition-opacity" active-class="text-black">Domov</router-link>
          <router-link to="/about" class="hover:opacity-60 transition-opacity" active-class="text-black">O projektu</router-link>
          <router-link to="/feedback" class="hover:opacity-60 transition-opacity" active-class="text-black">Predlogi</router-link>
        </nav>
      </div>
    </header>



<!-- okvir za vse strani (home, feedback,about -> vse se znotraj tega prikazejo... s to tailwind kodo)-->
    <main class="max-w-4xl mx-auto px-6 py-8 sm:py-12 flex-grow w-full">
      <!-- surovi okvir kamor vue router nalozi trenutno stran-->
      <router-view v-slot="{ Component }">
        <!-- mehki prehodi-->
        <transition name="fade" mode="out-in">
          <!-- tukaj dejansko izrisemo stran-->
          <component :is="Component" />
        </transition>
      </router-view>
    </main>




<!-- FOOTER-->
    <footer class="w-full px-6 py-6 sm:py-8 border-t border-gray-200 bg-white/30">
      <div class="max-w-4xl mx-auto flex justify-center items-center text-[10px] sm:text-xs text-gray-400 uppercase tracking-widest text-center">
        <span>© 2026 Investicijski kalkulator. Vsi izračuni so informativne narave.</span>
      </div>
    </footer>


  </div>



</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
