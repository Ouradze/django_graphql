import Vue from 'vue';
import './plugins/vuetify';
// import Vuetify from 'vuetify';
import App from './components/App/App.vue';
import router from './router';
import './registerServiceWorker';
import { createProvider } from './vue-apollo';

Vue.config.productionTip = false;

// Vue.use(Vuetify);

new Vue({
  router,
  provide: createProvider().provide(),
  render: h => h(App),
}).$mount('#app');
