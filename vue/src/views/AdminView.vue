<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-container fluid fill-height class="pa-0 ma-0 tblp">
    <v-row class="fill-height">
      <v-col cols="12" class="pa-0 ma-0">
        <v-toolbar color="black" dark>
          <v-toolbar-title>Models</v-toolbar-title>
          <v-btn
              @click="this.dialog = !this.dialog"
              style="margin-right: 2%;
                     margin-top: 1%;
                     background-color: black;">
            <v-icon icon="mdi mdi-image-plus"></v-icon>
          </v-btn>
          <v-btn
              @click="logout()"
              style="margin-right: 2%;
                         margin-top: 1%;
                         background-color: black;">
            <v-icon icon="mdi mdi-logout"></v-icon>
          </v-btn>
          <v-dialog
              v-model="this.dialog"
              style="position: fixed;"
              max-width="500px"
          >
            <v-card>
              <v-card-title>
                <span class="text-h5">New model</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                        cols="12"
                        sm="12"
                        md="12"
                    >
                      <v-alert
                          style="margin-bottom: 1%"
                          v-if="this.errorAlertPath"
                          title="Validation error"
                          :text="this.errorAlertPathText"
                          type="error"
                          variant="outlined"
                      ></v-alert>

                      <v-file-input
                          accept=".glb"
                          placeholder="Pick a 3D model file"
                          prepend-inner-icon="mdi-camera"
                          prepend-icon=""
                          @change="(e) => {this.dataObject.selectedFileModel = e.target.files}"
                          label="Model .glb"
                      ></v-file-input>

                      <v-alert
                          style="margin-bottom: 1%"
                          v-if="this.errorAlertSkyBoxImage"
                          title="Validation error"
                          :text="this.errorAlertPathSkyBoxImageText"
                          type="error"
                          variant="outlined"
                      ></v-alert>
                      <v-file-input
                          accept=".hdr,.jpg"
                          prepend-inner-icon="mdi-camera"
                          prepend-icon=""
                          @change="(e) => {this.dataObject.selectedSkyBoxImage = e.target.files}"
                          label="Skybox image .hdr .jpg"
                      ></v-file-input>

                      <v-alert
                          style="margin-bottom: 1%"
                          v-if="this.errorAlertEnvImage"
                          title="Validation error"
                          :text="this.errorAlertEnvImageText"
                          type="error"
                          variant="outlined"
                      ></v-alert>
                      <v-file-input
                          accept=".jpg"
                          prepend-inner-icon="mdi-camera"
                          prepend-icon=""
                          @change="(e) => {this.dataObject.selectedEnvImage = e.target.files}"
                          label="Env image .jpg"
                      ></v-file-input>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="12"
                        md="12"
                    >
                    </v-col>

                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="blue-darken-1"
                    variant="text"
                    @click="this.dialog = false; this.loading = false"
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
        </v-toolbar>
        <v-data-table
            :headers="headers"
            :items="this.MODELS"
            :loading="loading"
            class="elevation-1"
            dense
            fixed-header
            style="height: 100%; padding: 10px"
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
                >
                </model-viewer>
              </td>
              <td>
                <v-btn color="red" @click="deleteModel(item.id)">
                  <v-icon icon="mdi mdi-delete-outline"></v-icon>
                </v-btn>
              </td>
              <td>
                <v-checkbox v-model="item.is_active"
                            label="Visible"
                            @change="() => changeItemVisible(item.id, item.is_active)"
                >
                </v-checkbox>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import '@google/model-viewer'
import {mapActions, mapGetters} from "vuex";

export default {
  name: "AdminView",
  components: {
  },
  data() {
    return {
      headers: [
        { title: 'Id', key: 'id'},
        { title: 'Path', key: 'path'},
        { title: 'Model', key: 'model'},
        { title: 'Actions', key: 'actions'},
        { title: 'Visible', key: 'visible'},
      ],
      errorAlertSkyBoxImage: false,
      errorAlertEnvImage: false,
      errorAlertPath: false,
      loading: false,
      dialog: false,
      errorAlertPathSkyBoxImageText: '',
      errorAlertEnvImageText: '',
      errorAlertPathText: '',
      dataObject: {
        selectedSkyBoxImage: null,
        selectedFileModel: null,
        selectedEnvImage: null,
      }
    }
  },
  computed: {
    ...mapGetters(["MODELS"]),
  },
  methods: {
    async deleteModel(id) {
      this.loading = true
      await this.DELETE_MODELS(id)
      await this.GET_MODELS_ADMIN()
      this.loading = false
    },
    async sendModel() {
      this.loading = true
      try {
        await this.CREATE_MODELS(this.dataObject)
        await this.GET_MODELS_ADMIN()
        this.dialog = false
        this.loading = false
        this.dataObject = {
          selectedSkyBoxImage: null,
          selectedFileModel: null,
          selectedEnvImage: null,
        }
      } catch (error){
        this.loading = false
        if (error.response.data.path && error.response.status === 400) {
          this.errorAlertPath = true;
          this.errorAlertPathText = error.response.data.path[0] || 'Error! Try again later!';
        } else if (error.response.data.path_skybox_image && error.response.status === 400) {
          this.errorAlertSkyBoxImage = true;
          this.errorAlertPathSkyBoxImageText = error.response.data.path_skybox_image[0] || 'Error! Try again later!';
        } else if (error.response.data.path_env_image && error.response.status === 400) {
          this.errorAlertEnvImage = true;
          this.errorAlertEnvImageText = error.response.data.path_env_image[0] || 'Error! Try again later!';
        } else {
          this.errorAlertPath = true;
          this.errorAlertPathText = 'Occurred error while trying to send a file.';
        }
      }
    },
    async logout() {
      await this.LOGOUT();
      await this.$router.push('/logout');
    },
    async changeItemVisible(itemId, itemIsVisible) {
      await this.UPDATE_VISIBLE_MODEL({ id: itemId, isVisible: itemIsVisible })
    },
    ...mapActions(["GET_MODELS_ADMIN", "DELETE_MODELS", "CREATE_MODELS", "LOGOUT", "UPDATE_VISIBLE_MODEL"]),
  },
  async mounted() {
    await this.GET_MODELS_ADMIN()
  }
};
</script>

<style scoped>
.tblp {
  z-index: 1000;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
}
.pa-0 {
  padding: 0 !important;
}
.ma-0 {
  margin: 0 !important;
}
</style>
