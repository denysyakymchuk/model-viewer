const state = {
    skyBoxImage: null,
    mainModel: null,
    envImage: null,
    mainModelId: null,
    mainModelIndex: null,
};
const getters = {
    MAIN_MODEL: (state) => {
        return state.mainModel;
    },
    MAIN_MODEL_ID: (state) => {
        return state.mainModelId;
    },
    MAIN_SKY_BOX_IMAGE: (state) => {
        return state.skyBoxImage;
    },
    MAIN_ENV_IMAGE: (state) => {
        return state.envImage;
    },
    MAIN_MODEL_INDEX: (state) => {
        return state.mainModelIndex;
    }
};
const mutations = {
    SET_MAIN_MODEL: (state, payload) => {
        state.mainModel = payload;
    },
    SET_MAIN_SKY_BOX_IMAGE: (state, payload) => {
        state.skyBoxImage = payload;
    },
    SET_MAIN_ENV_IMAGE: (state, payload) => {
        state.envImage = payload;
    },
    SET_MAIN_MODEL_ID: (state, payload) => {
        state.mainModelId = payload;
    },
    SET_MAIN_MODEL_INDEX: (state, payload) => {
        state.mainModelIndex = payload;
    }

};
const actions = {
    GET_MAIN_MODEL: async (context, obj) => {
        await context.commit("SET_MAIN_MODEL", obj?.path);
        await context.commit("SET_MAIN_MODEL_ID", obj?.id);
        await context.commit("SET_MAIN_SKY_BOX_IMAGE", obj?.skyBoxImage)
        await context.commit("SET_MAIN_ENV_IMAGE", obj?.envImage);
        await context.commit("SET_MAIN_MODEL_INDEX", obj?.mainModelIndex);
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};
