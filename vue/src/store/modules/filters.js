const state = {
    Pixel: false,
    Brightness: 0,
    Opacity: 1,
    Contrast: 0,
    Grid: 0,
    Sepia: 0,
    ShadowSoftness: 0,
    ShadowIntensity: 0,
    BlendMode: 'SKIP',
};
const getters = {
    MAIN_MODEL_PIXEL: (state) => {
        return state.Pixel;
    },
    MAIN_MODEL_BRIGHTNESS: (state) => {
        return state.Brightness;
    },
    MAIN_MODEL_OPACITY: (state) => {
        return state.Opacity;
    },
    MAIN_MODEL_CONTRAST: (state) => {
        return state.Contrast;
    },
    MAIN_MODEL_GRID: (state) => {
        return state.Grid;
    },
    MAIN_MODEL_SEPIA: (state) => {
        return state.Sepia;
    },
    MAIN_MODEL_SHADOW_SOFTNESS: (state) => {
        return state.ShadowSoftness;
    },
    MAIN_MODEL_SHADOW_INTENSITY: (state) => {
        return state.ShadowIntensity;
    },
    MAIN_MODEL_BLENDMODE: (state) => {
        return state.BlendMode;
    },

};
const mutations = {
    MAIN_MODEL_PIXEL: (state, payload) => {
        state.Pixel = payload;
    },
    MAIN_MODEL_BRIGHTNESS: (state, payload) => {
        state.Brightness = payload;
    },
    MAIN_MODEL_OPACITY: (state, payload) => {
        state.Opacity = payload;
    },
    MAIN_MODEL_CONTRAST: (state, payload) => {
        state.Contrast = payload;
    },
    MAIN_MODEL_GRID: (state, payload) => {
        state.Grid = payload;
    },
    MAIN_MODEL_SEPIA: (state, payload) => {
        state.Sepia = payload;
    },
    MAIN_MODEL_SHADOW_SOFTNESS: (state, payload) => {
        state.ShadowSoftness = payload;
    },
    MAIN_MODEL_SHADOW_INTENSITY: (state, payload) => {
        state.ShadowIntensity = payload;
    },
    MAIN_MODEL_BLENDMODE: (state, payload) => {
        state.BlendMode = payload;
    },
};
const actions = {};

export default {
    state,
    getters,
    mutations,
    actions,
};
