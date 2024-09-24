import { createApp } from "vue";
import App from "./App.vue";
import { createVuetify } from 'vuetify'
import '@mdi/font/css/materialdesignicons.css'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/styles'

// @ts-ignore
import store from "./store";
// @ts-ignoreg
import router from "./router";
// @ts-ignore
import vue3GoogleLogin from "vue3-google-login" //library located in src/

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

app.use(store).use(router).use(vuetify).use(vue3GoogleLogin, {clientId: process.env.VUE_APP_CLIENT_ID}).mount("#app");