import { createStore } from "vuex";
import models from "@/store/modules/models";
import MainModel from "@/store/modules/MainModel";
import login from "@/store/modules/login";
import iframeModel from "@/store/modules/iframeModel";
import registration from "@/store/modules/registration";

export default createStore({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        registration,
        iframeModel,
        MainModel,
        models,
        login,
    },
});
