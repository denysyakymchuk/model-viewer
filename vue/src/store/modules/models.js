import api from "@/api/api";

const state = {
    models: [],
};
const getters = {
    MODELS: (state) => {
        return state.models;
    },
};
const mutations = {
    SET_MODELS: (state, payload) => {
        state.models = payload;
    },
};
const actions = {
    GET_MODELS: async (context) => {
        const data = await api.get(`/models`);
        await context.commit("SET_MODELS", data.data.models);
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};
