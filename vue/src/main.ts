import { createApp } from "vue";
import App from "./App.vue";
// @ts-ignore
import store from "./store";
// @ts-ignore
import router from "./router";

import { createVuetify } from 'vuetify'
import '@mdi/font/css/materialdesignicons.css'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/styles'

const vuetify = createVuetify({
    components,
    directives,
    theme: {
        themes: {
            light: {
                colors: {
                    primary: '#1867C0',
                    secondary: '#5CBBF6',
                },
            },
        },
    },
})

const app = createApp(App);

app.config.compilerOptions.isCustomElement = tag =>
    /^(model-viewer|effect-composer|pixelate-effect)$/.test(tag);

app.use(store).use(router).use(vuetify).mount("#app"); // Добавьте Vuetify в цепочку плагинов
