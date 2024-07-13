import api from "@/api/api";

const state = {
    models: [],
    nextPage: '', //link to next page
};
const getters = {
    MODELS: (state) => {
        return state.models;
    },
    NEXT_PAGE: (state) => {
        console.log(state.nextPage);
        return state.nextPage;
    }
};
const mutations = {
    SET_MODELS: (state, payload) => {
        state.models = payload;
    },
    EXTEND_MODELS: (state, payload) => {
        state.models = state.models.concat(payload);
    },
    SET_NEXT_PAGE: (state, payload) => {
        state.nextPage = payload !== null ? payload.split('v1')[1] : null
    },
};
const actions = {
    GET_MODELS_ADMIN: async (context) => {
        const data = await api.get(`/models/admin-models/`);
        await context.commit("SET_MODELS", data.data);
    },
    GET_ACTIVE_MODELS: async (context) => {
        const data = await api.get(`/models/get-models/`);
        await context.commit("SET_MODELS", data.data.results);

        if (data.data.next) {
            await context.commit("SET_NEXT_PAGE", data.data.next);
        } else {
            await context.commit("SET_NEXT_PAGE", null);
        }
    },
    GET_EXTEND_MODELS: async (context) => {
        const data = await api.get(context.getters.NEXT_PAGE);
        context.commit("EXTEND_MODELS", data.data.results);
        if (data.data.next) {
            await context.commit("SET_NEXT_PAGE", data.data.next);
        } else {
            await context.commit("SET_NEXT_PAGE", null);
        }
    },
    UPDATE_VISIBLE_MODEL: async (context, payload) => {
        const formData = new FormData();
        formData.append('is_active', payload.isVisible);
        await api.patch(`/models/${payload.id}/`, formData);
    },
    // GET_MODELS: async (context) => {
    //     const data = await api.get(`/models/`);
    //     await context.commit("SET_MODELS", data.data);
    // },
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
