<template>

  <div>

    <p>Hola mundo </p>
    {{ directory }}

  </div>

</template>

<script>
  import axios from 'axios'
  export default{
  	name: 'CompanyData',
    data(){
      return {
      	directory: []
      }
    },
    async mounted () {
    	try {
    		var result = await axios({
    			method: 'POST',
    			url: 'http://127.0.0.1:8000/graphql/',
    			data: {
    				query: `{
					  allTitles {
					    edges {
					      node {
					        id
					        titleName
					      }
					    }
					  }
					}`
    			}
    		})
    		this.directory = result.data.data.allTitles
    	} catch (error) {
    		console.error(error)
    	}
    }
  }
</script>

<style scoped>
</style>
