import api from "@/api/api";

const state = {
  token: localStorage.getItem('token'),
};
const getters = {
  TOKEN: (state) => {
    return state.token;
  },
};
const mutations = {
  SET_LOGIN: (state, payload) => {
    localStorage.setItem('token', payload.access_token)
    state.token = payload.access_token
  },
};
const actions = {
  GET_LOGIN: async (context, payload) => {
    const data = await api.post(`/auth/jwt/login`, payload);
    await context.commit("SET_LOGIN", data.data);
    return data.status
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
