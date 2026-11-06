import tailwindcss from '@tailwindcss/vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';
import {defineConfig, loadEnv} from 'vite';

export default defineConfig(({mode, command}) => {
  const env = loadEnv(mode, '.', '');
  if (command === 'build') {
    let apiUrl: URL;
    try {
      apiUrl = new URL(env.VITE_API_URL?.trim());
    } catch {
      throw new Error('Set VITE_API_URL to the deployed backend HTTPS origin before building (for example https://YOUR-BACKEND.vercel.app).');
    }
    const hostname = apiUrl.hostname.replace(/\.$/, '');
    if (
      apiUrl.protocol !== 'https:' ||
      hostname === 'localhost' || hostname.endsWith('.localhost') ||
      hostname.startsWith('127.') || hostname === '[::1]' || hostname === '0.0.0.0' ||
      apiUrl.username || apiUrl.password ||
      apiUrl.pathname !== '/' || apiUrl.search || apiUrl.hash
    ) {
      throw new Error('VITE_API_URL must be the public backend HTTPS origin, without an API path, query, or credentials; localhost is only supported by the dev server.');
    }
  }
  return {
    plugins: [vue(), tailwindcss()],
    define: {
      'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY),
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
      },
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
    },
  };
});
