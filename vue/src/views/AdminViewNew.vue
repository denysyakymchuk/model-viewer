<template>
  <v-responsive class="border rounded">
    <v-app :theme="theme">
      <v-app-bar class="px-3">
        <v-spacer><span style="font-size: 20px" class="mdi mdi-cube-outline"></span>Models</v-spacer>
        <v-btn
            :prepend-icon="theme === 'dark' ?  'mdi-weather-night' : 'mdi-weather-sunny'"
            text="Toggle Theme"
            slim
            @click="onClick"
        ></v-btn>
        <v-btn @click="dialog = !dialog">
          <v-icon icon="mdi mdi-image-plus"></v-icon>
        </v-btn>
        <v-btn @click="logout()">
          <v-icon icon="mdi mdi-logout"></v-icon>
        </v-btn>
      </v-app-bar>

      <v-main>
        <v-dialog
            v-model="dialog"
            persistent
            style="position: fixed;"
            max-width="500px"
        >

        <!--    Spinner      -->
          <div class="d-flex justify-center align-center">
            <v-progress-circular v-if="!isLoaded"  indeterminate color="white" :size="53" :width="4"></v-progress-circular>
          </div>
        <!--    Spinner      -->

          <v-card v-if="isLoaded">
            <v-card-title>
              <span class="text-h5">New model</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-alert
                        style="margin-bottom: 1%"
                        v-if="errorAlertPath"
                        title="Validation error"
                        :text="errorAlertPathText"
                        type="error"
                        variant="outlined"
                    ></v-alert>

                    <v-file-input
                        accept=".glb"
                        placeholder="Pick a 3D model file"
                        prepend-inner-icon="mdi-camera"
                        @change="(e) => { dataObject.selectedFileModel = e.target.files }"
                        label="Model .glb"
                    ></v-file-input>

                    <v-alert
                        style="margin-bottom: 1%"
                        v-if="errorAlertSkyBoxImage"
                        title="Validation error"
                        :text="errorAlertPathSkyBoxImageText"
                        type="error"
                        variant="outlined"
                    ></v-alert>

                    <v-file-input
                        accept=".hdr,.jpg"
                        prepend-inner-icon="mdi-camera"
                        @change="(e) => { dataObject.selectedSkyBoxImage = e.target.files }"
                        label="Skybox image .hdr .jpg"
                    ></v-file-input>

                    <v-alert
                        style="margin-bottom: 1%"
                        v-if="errorAlertEnvImage"
                        title="Validation error"
                        :text="errorAlertEnvImageText"
                        type="error"
                        variant="outlined"
                    ></v-alert>

                    <v-file-input
                        accept=".jpg"
                        prepend-inner-icon="mdi-camera"
                        @change="(e) => { dataObject.selectedEnvImage = e.target.files }"
                        label="Env image .jpg"
                    ></v-file-input>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="
                  dialog = false;
                  errorAlertPath = false;
                  errorAlertEnvImage = false;
                  errorAlertSkyBoxImage = false;
                  loading = false;"
              >
                Cancel
              </v-btn>
              <v-btn
                  color="blue-darken-1"
                  variant="text"
                  @click="sendModel()"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-container fluid fill-height>
          <v-data-table
              :headers="headers"
              :items="store.getters['MODELS']"
              :loading="loading"
              class="elevation-1"
              dense
              fixed-header
          >
            <template v-slot:item="{ item }">
              <tr>
                <td>{{ item.id }}</td>
                <td>{{ item.path }}</td>
                <td>
                  <model-viewer
                      :src="item.path"
                      :environment-image="item.path_env_image"
                      :skybox-image="item.path_skybox_image"
                  />
                </td>
                <td>
                  <v-btn color="red" @click="deleteModel(item.id)">
                    <v-icon icon="mdi mdi-delete-outline"></v-icon>
                  </v-btn>
                </td>
                <td>
                  <v-checkbox
                      v-model="item.is_active"
                      label="Visible"
                      @change="() => changeItemVisible(item.id, item.is_active)"
                  />
                </td>
              </tr>
            </template>
          </v-data-table>
        </v-container>
      </v-main>
    </v-app>
  </v-responsive>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore();
const theme = ref('dark');
const router = useRouter();

const headers = [
  { title: 'Id', key: 'id' },
  { title: 'Path', key: 'path' },
  { title: 'Model', key: 'model' },
  { title: 'Actions', key: 'actions' },
  { title: 'Visible', key: 'visible' },
];

const dialog = ref(false);
const isLoaded = ref(true);
const loading = ref(false);
const errorAlertPath = ref(false);
const errorAlertSkyBoxImage = ref(false);
const errorAlertEnvImage = ref(false);
const errorAlertPathSkyBoxImageText = ref('');
const errorAlertEnvImageText = ref('');
const errorAlertPathText = ref('');

//models object
const dataObject = {
  selectedSkyBoxImage: null,
  selectedFileModel: null,
  selectedEnvImage: null,
};

function onClick() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark'; //change admin theme
}

async function deleteModel(id) {
  loading.value = true;
  await store.dispatch('DELETE_MODELS', id);
  await store.dispatch('GET_MODELS_ADMIN');
  loading.value = false;
}

async function sendModel() {
  //close all error messages
  errorAlertPath.value = false;
  errorAlertSkyBoxImage.value = false;
  errorAlertEnvImage.value = false;
  try {
    //check if main model exists
    if (!dataObject.selectedFileModel) {
      errorAlertPath.value = true;
      errorAlertPathText.value = "The model doesn't exists";
      return false
    }
    isLoaded.value = false //mark as start loading
    await store.dispatch('CREATE_MODELS', dataObject);
    await store.dispatch('GET_MODELS_ADMIN');
    dialog.value = false; //close the model
    dataObject.selectedSkyBoxImage = null;
    dataObject.selectedFileModel = null;
    dataObject.selectedEnvImage = null;
    isLoaded.value = true //mark as loaded
  } catch (error){
    if (error.response.data.path && error.response.status === 400) {
      errorAlertPath.value = true;
      errorAlertPathText.value = error.response.data.path[0] || 'Error! Try again later!';
    } else if (error.response.data.path_skybox_image && error.response.status === 400) {
      errorAlertSkyBoxImage.value = true;
      errorAlertPathSkyBoxImageText.value = error.response.data.path_skybox_image[0] || 'Error! Try again later!';
    } else if (error.response.data.path_env_image && error.response.status === 400) {
      errorAlertEnvImage.value = true;
      errorAlertEnvImageText.value = error.response.data.path_env_image[0] || 'Error! Try again later!';
    } else {
      errorAlertPath.value = true;
      errorAlertPathText.value = 'Occurred error while trying to send a file.';
    }
  } finally {
    isLoaded.value = true //mark as loaded
  }
}

async function logout() {
  await store.dispatch('LOGOUT');
  await router.push('/logout');
}

async function changeItemVisible(itemId, itemIsVisible) {
  await store.dispatch('UPDATE_VISIBLE_MODEL', {id: itemId, isVisible: itemIsVisible});
}

onMounted(async () => {
  await store.dispatch('GET_MODELS_ADMIN');
});
</script>

<style scoped>
@font-face {
  font-family: 'Lexend';
  src: url('../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf') format('truetype');
  font-weight: normal; /* or a specific weight */
  font-style: normal; /* or italic */
}
* {
  font-family: Lexend;
}
</style>
