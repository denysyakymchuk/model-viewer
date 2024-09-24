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
    localStorage.setItem('token', payload);
    state.token = payload;
  },
  CLEAR_TOKEN: (state) => {
    localStorage.removeItem('token');
    state.token = null;
  },
};

const actions = {
  GET_LOGIN: async (context, payload) => {
    const data = await api.post(`/auth/token/login/`, payload, { "Content-Type": 'application/x-www-form-urlencoded' });
    await context.commit("SET_LOGIN", data.data.auth_token);
    return data.status;
  },
  LOGOUT: async (context) => {
    await api.post(`/auth/token/logout/`);
    context.commit("CLEAR_TOKEN");
  },
  POST_GOOGLE_LOGIN: async (context, payload) => {
    const  data = await api.post(`/dj-rest-auth/google/login/`, payload, {"Content-Type": 'application/x-www-form-urlencoded'});
    await context.commit("SET_LOGIN", data.data.key)
    return data
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
