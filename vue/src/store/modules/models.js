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
    DELETE_MODELS: async (context, payload) => {
        const data = await api.get(`/delete-model?path_id=${payload}`);
        await context.commit("SET_MODELS", data.data.models);
    },
    CREATE_MODELS: async (context, payload) => {
        let formData = new FormData();
        formData.append('file', payload[0]);
        const data = await api.post(`/upload-model`, formData);
        await context.commit("SET_MODELS", data.data.models);
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};
