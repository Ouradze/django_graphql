import Vue from 'vue';
import 'vuetify';
import App from './App.vue';
import router from './router';
import './registerServiceWorker';
import { createProvider } from './vue-apollo';

Vue.config.productionTip = false;

new Vue({
  router,
  provide: createProvider().provide(),
  render: h => h(App),
}).$mount('#app');
