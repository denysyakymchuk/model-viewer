<template>
  <div style="width: 100%">
    <v-data-table
        style="position: absolute; top: 0; left: 0"
        :headers="headers"
        :loading="loading"
        :items="this.MODELS"
        density="compact"
        item-key="name"
    >
      <template v-slot:item="{ item }">
        <tr>
          <td>{{ item.id }}</td>
          <td>{{ item.path }}</td>
          <td><model-viewer :src="item.path"></model-viewer></td>
          <td class="delete-button" @click="deleteModel(item.id)">Delete</td>
        </tr>
      </template>
    </v-data-table>
  </div>
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
        { title: 'Id', key: 'id', align: 'left' },
        { title: 'Path', key: 'path', align: 'left' },
        { title: 'Model', key: 'path', align: 'center' },
        { title: 'Action', key: 'path', align: 'center' },
      ],
      itemsPerPage: 5,
      serverItems: [],
      loading: false,
      totalItems: 0,
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
    ...mapActions(["GET_MODELS", "DELETE_MODELS"]),
  },
  async mounted() {
    await this.GET_MODELS()
  }
};
</script>

<style scoped>
html, body, #app {
  height: 100%;
  margin: 0;
}

.table-container {
  height: 100%;
}

::v-deep .v-data-table {
  height: 100%;
}
::v-deep .v-data-table {
  background-color: #f5f5f5; /* Сірий фон таблиці */
  border-radius: 16px; /* Заокруглені кути */
  width: 100%; /* Ширина на всю сторінку */
  box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Тінь для ефекту відділення */
}

::v-deep .v-data-table th {
  background-color: #312f2f; /* Сірий фон для заголовків */
}

::v-deep .v-data-table td {
  background-color: #f9f9f9; /* Світло-сірий для комірок */
}

::v-deep .v-data-table tbody tr:hover {
  background-color: #eeeeee; /* Трохи темніший сірий при наведенні */
}

/* Стилізація кнопки видалення */
::v-deep .delete-button {
  color: #ff5252; /* Червоний колір для тексту */
  cursor: pointer; /* Курсор у вигляді руки для вказівки на можливість кліку */
  font-weight: bold; /* Жирний текст */
}
</style>
