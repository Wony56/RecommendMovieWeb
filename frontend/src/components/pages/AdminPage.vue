<template>
  <v-container>

    <v-col cols="12">
      <v-card>
        <v-card-title>
          사용자 목록
          <div class="flex-grow-1"></div>
          <v-text-field
            v-model="searchUser"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          v-model="selectedUser"
          :headers="headers"
          :items="users"
          :search="searchUser"
          show-select
          item-key="id"
        >
          <template v-slot:item.action="{item}">
            <v-icon small class="mr-2" @click="editUser(item)">mdi-pencil</v-icon>
            <v-icon small @click="deleteUser(item)">mdi-delete</v-icon>
          </template>
        </v-data-table>
        <v-card-actions>
          <v-container>
            <v-row justify="center">
              <v-btn v-bind="optionsUser" @click="deleteSelectedUsers">선택항목 삭제</v-btn>
            </v-row>
          </v-container>
        </v-card-actions>
      </v-card>
    </v-col>

    <br />

    <v-col cols="12">
      <v-card>
        <v-card-title>
          영화 목록
          <div class="flex-grow-1"></div>
          <v-text-field
            v-model="searchMovie"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          v-model="selectedMovie"
          :headers="headersMovie"
          :items="movies"
          :search="searchMovie"
          show-select
          item-key="id"
        >
          <template v-slot:item.action="{item}">
            <v-icon small class="mr-2" @click="editMovie(item)">mdi-pencil</v-icon>
            <v-icon small @click="deleteMovie(item)">mdi-delete</v-icon>
          </template>
        </v-data-table>
        <v-card-actions>
          <v-container>
            <v-row justify="center">
              <v-btn v-bind="optionsMovie" @click="deleteSelectedMovies">선택항목 삭제</v-btn>
            </v-row>
          </v-container>
        </v-card-actions>
      </v-card>
    </v-col>

    <v-dialog v-model="userDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">{{editedUser.username}} 정보 수정</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="editedUser.occupation" label="직업" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="editedUser.age" label="나이" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-select v-model="editedUser.gender" :items="genders" label="성별" required></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="userDialog = false">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="saveEditedUser">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="movieDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">영화정보수정</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="editedMovie.title" label="타이틀" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-combobox
                  v-model="editedMovie.genresArr"
                  :items="genres"
                  label="장르"
                  multiple
                  chips
                ></v-combobox>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="movieDialog = false">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="saveEditedMovie">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>


<script>
import api from "../../api";

export default {
  data() {
    return {
      searchUser: "",
      searchMovie: "",
      selectedUser: [],
      selectedMovie: [],
      userDeleteBtnDisabled: true,
      movieDeleteBtnDisabled: true,
      genders: ["M", "F"],
      genres: [
        "Action",
        "Adventure",
        "Animation",
        "Children's",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Film-Noir",
        "Horror",
        "Musical",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western"
      ],
      headers: [
        {
          text: "사용자",
          align: "left",
          sortable: false,
          value: "username"
        },
        { text: "직업", value: "occupation" },
        { text: "성별", value: "gender" },
        { text: "나이", value: "age" },
        { text: "작업", value: "action", align: "right", sortable: false }
      ],
      users: [],
      headersMovie: [
        {
          text: "타이틀",
          align: "left",
          value: "title"
        },
        { text: "장르", value: "genres" },
        { text: "작업", value: "action", align: "right", sortable: false }
      ],
      movies: [],
      editedUser: {},
      editedMovie: {},
      userDialog: false,
      movieDialog: false
    };
  },
  computed: {
    optionsUser() {
      const options = {
        color: "error",
        disabled: this.userDeleteBtnDisabled
      };

      return options;
    },
    optionsMovie() {
      const options = {
        color: "error",
        disabled: this.movieDeleteBtnDisabled
      };

      return options;
    }
  },
  watch: {
    selectedUser() {
      if (this.selectedUser.length > 0) {
        this.userDeleteBtnDisabled = false;
      } else {
        this.userDeleteBtnDisabled = true;
      }
    },
    selectedMovie() {
      if (this.selectedMovie.length > 0) {
        this.movieDeleteBtnDisabled = false;
      } else {
        this.movieDeleteBtnDisabled = true;
      }
    }
  },
  created() {
    this.initialize();
  },
  methods: {
    initialize() {
      this.getAllProfiles();
      this.getAllMovies();
    },
    async getAllProfiles() {
      await api
        .getAllProfiles()
        .then(res => {
          if (res.status === 200) {
            this.users = res.data.map(d => ({
              id: d.id,
              username: d.username,
              occupation: d.occupation,
              gender: d.gender,
              age: d.age
            }));
          }
        })
        .catch(err => alert(err));
    },
    async getAllMovies() {
      await api
        .searchMovies()
        .then(res => {
          if (res.status === 200) {
            this.movies = res.data.map(d => {
              let genres = "";

              d.genres_array.forEach((g, index) => {
                genres += g;

                if (index !== d.genres_array.length - 1) {
                  genres += ", ";
                }
              });

              return {
                id: d.id,
                title: d.title,
                genres: genres,
                genresArr: d.genres_array
              };
            });
          }
        })
        .catch(err => alert(err));
    },
    editUser(item) {
      this.editedIndex = this.users.indexOf(item);
      this.editedUser = Object.assign({}, item);
      this.userDialog = true;
    },
    editMovie(item) {
      this.editedIndex = this.movies.indexOf(item);
      this.editedMovie = Object.assign({}, item);
      this.movieDialog = true;
    },
    deleteUser(item) {
      const index = this.users.indexOf(item);
      if (confirm("정말 삭제하시겠습니까?")) {
        api
          .deleteUser({ username: item.username })
          .then(res => {
            if (res.status === 200) {
              alert("성공적으로 삭제되었습니다.");
              this.users.splice(index, 1);
            }
          })
          .catch(err => {
            alert(err);
          });
      }
    },
    deleteSelectedUsers() {
      if (confirm("정말 삭제하시겠습니까?")) {
        const selected = this.selectedUser.map(user => user.username);

        api
          .deleteUser({ selected })
          .then(res => {
            if (res.status === 200) {
              this.selectedUser.forEach(user => {
                const index = this.users.indexOf(user);
                this.users.splice(index, 1);
              });
              this.selectedUser = [];
              alert("성공적으로 삭제되었습니다.");
            }
          })
          .catch(err => {
            alert(err);
          });
      }
    },
    deleteMovie(item) {
      const index = this.movies.indexOf(item);
      if (confirm("정말 삭제하시겠습니까?")) {
        api
          .deleteMovie({ id: item.id })
          .then(res => {
            if (res.status === 200) {
              alert("성공적으로 삭제되었습니다.");
              this.movies.splice(index, 1);
            }
          })
          .catch(err => {
            alert(err);
          });
      }
    },
    deleteSelectedMovies() {
      if (confirm("정말 삭제하시겠습니까?")) {
        const selected = this.selectedMovie.map(movie => movie.id);

        api
          .deleteMovie({ selected })
          .then(res => {
            if (res.status === 200) {
              this.selectedMovie.forEach(movie => {
                const index = this.movies.indexOf(movie);
                this.movies.splice(index, 1);
              });
              this.selectedMovie = [];
              alert("성공적으로 삭제되었습니다.");
            }
          })
          .catch(err => {
            alert(err);
          });
      }
    },
    saveEditedUser() {
      api
        .saveEditedUser(this.editedUser)
        .then(res => {
          if (res.status === 200) {
            this.users.splice(this.editedIndex, 1, this.editedUser);
            alert("수정완료");
            this.editedUser = {};
            this.userDialog = false;
          }
        })
        .catch(err => {
          alert(err);
        });
    },
    saveEditedMovie() {
      let genres = "";

      this.editedMovie.genresArr.sort();

      this.editedMovie.genresArr.forEach((genre, index) => {
        genres += genre.trim();

        if (index !== this.editedMovie.genresArr.length - 1) {
          genres += "|";
        }
      });

      this.editedMovie.genres = genres;

      api
        .saveEditedMovie(this.editedMovie)
        .then(res => {
          if (res.status === 200) {
            this.editedMovie.genres = "";
            this.editedMovie.genresArr.forEach((gender, index) => {
              this.editedMovie.genres += gender;

              if (index !== this.editedMovie.genresArr.length - 1) {
                this.editedMovie.genres += ", ";
              }
            });

            this.movies.splice(this.editedIndex, 1, this.editedMovie);
            alert("수정완료");
            this.editedMovie = {};
            this.movieDialog = false;
          }
        })
        .catch(err => alert(err));
    }
  }
};
</script>