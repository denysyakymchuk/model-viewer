import api from "@/api/api";

const state = {
};

const getters = {

};

const mutations = {
};

const actions = {
    REGISTRATION_NEW_USER: async (context, payload) => {
        await api.post(`/auth/users/`, payload, { "Content-Type": 'application/x-www-form-urlencoded' });
    },
    ACTIVATE_ACCOUNT: async (context, payload) => {
        await api.post(`/auth/users/activation/`, payload, { "Content-Type": 'application/x-www-form-urlencoded' });
    }
};

export default {
    state,
    getters,
    mutations,
    actions,
};
