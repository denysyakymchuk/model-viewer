import { createApp } from "vue";
import App from "./App.vue";
import store from "./store";

const app = createApp(App);

app.config.compilerOptions.isCustomElement = tag =>
    /^(model-viewer|effect-composer|pixelate-effect)$/.test(tag);


app.use(store).mount("#app");
