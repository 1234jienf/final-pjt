import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import VueGoodTablePlugin from 'vue-good-table-next';


// import the styles 
import 'vue-good-table-next/dist/vue-good-table-next.css'


library.add(fas);

const app = createApp(App);
const pinia = createPinia();

app.component('font-awesome-icon', FontAwesomeIcon);
app.use(VueGoodTablePlugin);


app.use(pinia);
app.use(router);
app.mount('#app');
