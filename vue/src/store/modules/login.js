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
    localStorage.setItem('token', payload.auth_token)
    state.token = payload.auth_token
  },
};
const actions = {
  GET_LOGIN: async (context, payload) => {
    const data = await api.post(`/auth/token/login/`, payload, {"Content-Type": 'application/x-www-form-urlencoded'});
    await context.commit("SET_LOGIN", data.data);
    return data.status
  },
  LOGOUT: async () => {
    await api.post(`/auth/token/logout/`);
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
