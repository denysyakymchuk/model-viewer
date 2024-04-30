import api from "@/api/api";

const state = {
    mainModelIframe: null,
    mainModelIframeSBI: null,
    mainModelIframeEI: null,
};
const getters = {
    MAIN_MODEL_IFRAME: (state) => {
        return state.mainModelIframe;
    },
    MAIN_MODEL_IFRAME_SBI: (state) => {
        return state.mainModelIframeSBI;
    },
    MAIN_MODEL_IFRAME_EI: (state) => {
        return state.mainModelIframeEI;
    }
};
const mutations = {
    SET_MAIN_MODEL_IFRAME: (state, payload) => {
        state.mainModelIframe = payload;
    },
    SET_MAIN_MODEL_IFRAME_SBI: (state, payload) => {
        state.skyBoxImage = payload;
    },
    SET_MAIN_MODEL_IFRAME_EI: (state, payload) => {
        state.envImage = payload;
    },

};
const actions = {
    GET_MAIN_MODEL_IFRAME: async (context, id) => {
        const data = await api.get(`/model?path_id=${id}`);
        await context.commit("SET_MAIN_MODEL_IFRAME", data?.data?.path);
        await context.commit("SET_MAIN_MODEL_IFRAME_SBI", data?.data?.path_skybox_image)
        await context.commit("SET_MAIN_MODEL_IFRAME_EI", data?.data?.path_env_image);
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};
