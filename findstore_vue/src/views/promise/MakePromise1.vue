<template>
  <v-container>
    <v-row justify="center">
      <v-date-picker color = "deep-purple lighten-4" event-color="deep-purple lighten-4" v-model="picker" :min="today"></v-date-picker>
    </v-row>
    <v-text-field
      class="mx-10"
      v-model="promiseData.title"
      :counter="20"
      label="약속 이름을 입력해주세요."
      required
    ></v-text-field>
    <div class="text-center">
      <v-btn
        v-for="(gu, i) in guList"
        :key="i"
        :color="promiseData.gu == gu ? 'deep-purple lighten-4' : ''"
        class="m-1"
        rounded
        @click="promiseData.gu = gu; gu_cnt = i; promiseData.dong=''"
      >{{gu}}</v-btn>
    </div>
    <div class="text-center">
      <hr />
      <v-btn
        v-for="(dong, di) in dongList[gu_cnt]"
        :key="di"
        :color="promiseData.dong == dong ? 'deep-purple lighten-4' : ''"
        class="m-1"
        rounded
        @click="promiseData.dong = dong"
      >{{dong}}</v-btn>
    </div>
    <hr />
    <div v-if="promiseData.dong && promiseData.title" class="d-flex justify-end">
      <v-btn text color="orange" style="font-size: 15px" class="white--text" small @click="makePromise">다음</v-btn>
    </div>
  </v-container>
</template>

<script>
import axios from "axios";
import constants from "../../lib/constants";

const SERVER_URL = constants.ServerUrl;

export default {
  name: "MakePromise1",
  data() {
    return {
      guList: ["마포구", "성북구", "성동구", "강남구"],
      dongList: [
        [
          "공덕동",
          "노고산동",
          "당인동",
          "대흥동",
          "도화동",
          "동교동",
          "망원동",
          "상수동",
          "상암동",
          "서교동",
          "성산동",
          "신공덕동",
          "신수동",
          "연남동",
          "염리동",
          "용강동",
          "창전동",
          "합정동",
        ],
        [
          "동선동",
          "동소문동",
          "보문동",
          "삼선동",
          "석관동",
          "성북동",
          "안암동",
          "정릉동",
          "하월곡동",
        ],
        [
          "금호동",
          "도선동",
          "마장동",
          "사근동",
          "성수1가",
          "성수2가",
          "옥수동",
          "행당동",
          "혹익동",
          "송정동",
        ],
        [
          "개포동",
          "논현동",
          "대치동",
          "도곡동",
          "삼성동",
          "세곡동",
          "수서동",
          "신사동",
          "압구정동",
          "역삼동",
          "일원동",
          "일원본동",
          "청담동",
        ],
        [],
      ],
      gu_cnt: 4,
      promiseData: {
        title: "",
        date: "",
        gu: "",
        dong: "",
        storelist: "",
      },
      picker: new Date().toISOString().substr(0, 10),
    };
  },
  computed: {
    today () {
      var today = new Date().toISOString().substr(0, 10)
      return today
    }
  },
  created() {
    this.isUser();
  },
  methods: {
    isUser() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .get(SERVER_URL + "/rest-auth/user/", config)
        .then((res) => {
          const userInfo = res.data.username
          axios
            .get(SERVER_URL + "/meeting/detail/" + this.$route.params.m_id)
            .then((res) => {
              if (res.data.user.username != userInfo) {
                this.$router.push({
                  name: "meetinglist"
                })
                alert("잘못된 접근입니다.")
              }
            })
            .catch((err) => console.error(err.response));
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    makePromise() {
      const m_id = this.$route.params.m_id;
      this.promiseData.date = this.picker;
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .post(SERVER_URL + "/promise/" + m_id +"/create/", this.promiseData, config)
        .then((res) => {
          this.$router.push({
            name: "makepromise2",
            params: { p_id: res.data.id },
          });
        })
        .catch((err) => console.log(err.response));
    },
  },
};
</script>

<style>
</style>