import { createStore } from "vuex";
import models from "@/store/modules/models";
import MainModel from "@/store/modules/MainModel";

export default createStore({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        MainModel,
        models
    },
});
