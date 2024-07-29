<template>
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
</template>

<script setup>
let dialog =  false;
let errorAlertPathSkyBoxImageText =  '';
let errorAlertEnvImageText =  '';
let errorAlertPathText =  '';
const dataObject = {
  selectedSkyBoxImage: null,
  selectedFileModel: null,
  selectedEnvImage: null,
}
</script>

<style scoped>
.tblp {
  z-index: 1000;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
}
</style>