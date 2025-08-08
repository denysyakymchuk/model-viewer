import {
    GridEffect,
    SepiaEffect,
} from "postprocessing";


const state = {
    Pixel: false,
    Brightness: 0,
    Opacity: 0,
    Contrast: 0,
    Grid: 0,
    Sepia: 0,
    ShadowSoftness: 0,
    ShadowIntensity: 0,
    BlendMode: 'NORMAL',
    SepiaEffect: (() => {
        const sepiaEffect = new SepiaEffect();
        sepiaEffect.intensity = 0;
        return sepiaEffect;
    })(),
    GridEffect: new GridEffect({scale: 0}),
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
    MAIN_MODEL_GRID_EFFECT: (state) => {
        return state.GridEffect;
    },
    MAIN_MODEL_SEPIA_EFFECT: (state) => {
        return state.SepiaEffect;
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
    MAIN_MODEL_GRID_EFFECT: (state, payload) => {
        state.GridEffect.scale = payload;
    },
    MAIN_MODEL_SEPIA_EFFECT: (state, payload) => {
        state.SepiaEffect.intensity = payload;
    },
};

export default {
    state,
    getters,
    mutations,
};
