<template>
  <div id="app">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarText">
              <ul class="navbar-nav mr-auto">
                  <li class="nav-item active">
                      <a class="nav-link" href="#"> Empleados <span class="sr-only">(current)</span></a>
                  </li>
                  <li class="nav-item">
                      <a class="nav-link" href="#"> Puestos </a>
                  </li>
                  <li class="nav-item">
                      <a class="nav-link" href="#"> Ciudades</a>
                  </li>
              </ul>
          </div>
      </nav>
    <!-- <HelloWorld/> -->
    <CompanyData/> <!-- Added New tag -->
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import CompanyData from './components/Comp' //import new component

export default {
  name: 'App',
  components: {
    HelloWorld,
    CompanyData //register new component
  }
}
</script>

<style>
@import "../node_modules/bootstrap/dist/css/bootstrap.min.css"; /*Importing Bootstrap*/
#app {
/*  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;*/
}
</style>
