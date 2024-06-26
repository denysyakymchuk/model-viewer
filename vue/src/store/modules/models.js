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
        await context.commit("SET_MODELS", data.data);
    },
    DELETE_MODELS: async (context, payload) => {
        const data = await api.delete(`/models/${payload}`);
        await context.commit("SET_MODELS", data.data.models);
    },
    CREATE_MODELS: async (context, payload) => {
        let formData = new FormData();
        formData.append('path', payload?.selectedFileModel[0]);

        if (payload.selectedSkyBoxImage !== null) {
            formData.append('path_skybox_image', payload.selectedSkyBoxImage[0]);
        }

        if (payload.selectedEnvImage !== null) {
            formData.append('path_env_image', payload.selectedEnvImage[0]);
        }
        // default user
        formData.append('owner', 1);

        const data = await api.post(`/models/`, formData, {'Content-Type': 'multipart/form-data'});
        await context.commit("SET_MODELS", data.data.models);
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};
