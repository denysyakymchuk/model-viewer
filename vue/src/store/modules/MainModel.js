const state = {
    mainModel: [],
};
const getters = {
    MAIN_MODEL: (state) => {
        return state.mainModel;
    },
};
const mutations = {
    SET_MAIN_MODEL: (state, payload) => {
        state.mainModel = payload;
    },
};
const actions = {
    GET_MAIN_MODEL: async (context, path) => {
        await context.commit("SET_MAIN_MODEL", path);
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};
