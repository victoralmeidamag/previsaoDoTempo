<template>
  <div id="app" class="app weather-app">
    <div class="main">
      <div class="search-box">
        <h2>Pesquisa por nome da cidade</h2>
        <input class="search-bar" type="text" placeholder="Pesquisar por CIDADE" v-model="data.city" @input="handleInput" @keyup.enter="enviar">
        <h2>Pesquisa por CEP</h2>
        <input class="search-bar" type="text" placeholder="Pesquisar por CEP">
        <div>
          <div class="header">
            <h1>{{ data.city.charAt(0).toLocaleUpperCase() + data.city.slice(1) }}</h1>
            <h3>{{ hora }}</h3>
          </div>
          <div class="temp">
            <h2>{{ temperatura }}&deg;C</h2>
          </div>
          <div class="estado">
            <h3>{{ descricao }}</h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'WeatherComponent',
  props: {},
  data() {
    return {
      data: {
        city: '',
      },
      hora: new Date().toLocaleString(),
      temperatura: '',
      descricao: '',
    };
  },
  mounted() {
    this.timer = setInterval(() => {
      this.hora = new Date().toLocaleString();
    }, 1000);
  },
  beforeUnmount() {
    clearInterval(this.timer);
  },
  methods: {
    handleInput() {
      this.data.city = this.data.city.toLocaleLowerCase();
      this.data.city = this.data.city.charAt(0).toLocaleUpperCase() + this.data.city.slice(1);
    },
    async enviar() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/search', {
          city: this.data.city,
        }, {
          headers: {
            'Content-Type': 'application/json',
          },
        });
        if (response.data.error) {
          console.error("Erro ao pesquisar:", response.data.error)
        } else {
          this.temperatura = response.data.temperatura
          this.descricao = (response.data.descricao).charAt(0).toLocaleUpperCase() + response.data.descricao.slice(1);
        }
      } catch (error) {
        console.error('Erro ao pesquisar:', error);
      }
    }
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  background: url('../assets/rt.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  margin: 0;
  overflow: hidden;
  object-fit: cover;
}

.main {
  min-height: 100vh;
  padding: 25px;
  background-image: linear-gradient(to bottom, rgba(18, 75, 156, 0.35), rgba(2, 15, 22, 0.75));
}

.search-box {
  width: 100%;
  left: 300px;
  margin: 200px;
  position: relative;
}

.search-box h2{
  color: white;
}

.search-box .search-bar {
  display: block;
  width: 20%;
  padding: 15px;
  position: relative;
  color: #313131;
  font-size: 20px;
  appearance: none;
  border: none;
  outline: none;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  transition: 0.4s;
}

.search-box .search-bar:focus {
  box-shadow: 0px 0px 16px;
  background-color: rgb(255, 255, 255, 0.75);
}

.header {
  padding-top: 20px;
  font-size: 20px;
  color: azure;
  box-shadow: rgb(3, 3, 3, 0.3);
}

.temp {
  display: inline-block;
  padding: 10px 25px;
  font-size: 102px;
  color: #FFF;
  font-weight: 988;
  text-shadow: 3px 6px rgba(0, 0, 0, 0.25);

  background-color: rgba(255, 255, 255, 0.25);
  border-radius: 16px;
  margin: 30px 0;
  box-shadow: 3px 6px rgba(0, 0, 0, 0.25);
}

.estado {
  position: absolute;
  color: #FFF;
  font-style: italic;
  text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
  text-align: center;
}
</style>
