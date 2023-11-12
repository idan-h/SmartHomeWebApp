import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './routes';

import VueSelect from "vue-select";
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'

const app = createApp(App);
app.use(router);
app.component("v-select", VueSelect)
app.component("v-slider", VueSlider)
app.mount('#app');
