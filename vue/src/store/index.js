import { createStore } from "vuex";
import models from "@/store/modules/models";
import MainModel from "@/store/modules/MainModel";
import login from "@/store/modules/login";
import iframeModel from "@/store/modules/iframeModel";
import registration from "@/store/modules/registration";
import filters from "@/store/modules/filters";

export default createStore({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        registration,
        iframeModel,
        MainModel,
        filters,
        models,
        login,
    },
});
