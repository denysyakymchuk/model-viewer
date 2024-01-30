import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
})

const app = createApp(App);

app.config.compilerOptions.isCustomElement = tag =>
    /^(model-viewer|effect-composer|pixelate-effect)$/.test(tag);

app.use(store).use(router).use(vuetify).mount("#app"); // Добавьте Vuetify в цепочку плагинов
