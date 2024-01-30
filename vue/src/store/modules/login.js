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
    localStorage.setItem('token', payload.token)
    state.token = payload.token
  },
};
const actions = {
  GET_LOGIN: async (context, payload) => {
    const data = await api.post(`/auth/jwt/login`, payload);
    console.log(data.data)
    await context.commit("SET_LOGIN", data.data.access_token);
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
