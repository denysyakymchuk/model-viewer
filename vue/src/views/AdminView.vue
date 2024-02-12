<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-container fluid fill-height class="pa-0 ma-0 tblp">
    <v-row class="fill-height">
      <v-col cols="12" class="pa-0 ma-0">
        <v-toolbar color="black" dark>
          <v-toolbar-title>Models</v-toolbar-title>
          <v-btn
              @click="this.dialog = !this.dialog"
              style="   margin-right: 2%;
                         margin-top: 1%;
                         background-color: #2bc0d5;">
            New model
          </v-btn>
          <v-btn
              @click="this.$router.push('/logout')"
              style="margin-right: 2%;
                         margin-top: 1%;
                         background-color: #f6b329;">
            Logout
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
                      <v-file-input
                          accept=".glb"
                          placeholder="Pick a 3D model file"
                          prepend-inner-icon="mdi-camera"
                          prepend-icon=""
                          @change="(e) => {this.selectedFile = e.target.files}"
                          label="Image"
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
                    @click="this.dialog = false"
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
              <td><model-viewer :src="item.path"></model-viewer></td>
              <td>
                <v-btn color="red" @click="deleteModel(item.id)" text>
                  Delete
                </v-btn>
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
        { title: 'Model', key: 'path'},
        { title: 'Action', key: 'path'},
      ],
      loading: false,
      dialog: false,
      selectedFile: '',
    }
  },
  computed: {
    ...mapGetters(["MODELS"]),
  },
  methods: {
    async deleteModel(id) {
      this.loading = true
      await this.DELETE_MODELS(id)
      await this.GET_MODELS()
      this.loading = false
    },
    async sendModel() {
      this.loading = true
      await this.CREATE_MODELS(this.selectedFile)
      await this.GET_MODELS()
      this.dialog = false
      this.loading = false
      this.selectedFile = ''
    },
    ...mapActions(["GET_MODELS", "DELETE_MODELS", "CREATE_MODELS"]),
  },
  async mounted() {
    await this.GET_MODELS()
  }
};
</script>

<style scoped>
.tblp {
  z-index: 1000;
  position: fixed;
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
