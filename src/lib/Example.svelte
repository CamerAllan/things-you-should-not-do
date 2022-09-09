<script lang="ts">

    async function getAircrafts() {
      const res = await fetch('/data/things-not-do.json');
      const values = await res.json();
  
      return values;
    }
    
    // NOTE await not used here! 
    let thingsPromise = getAircrafts();
  
  </script>
    
{#await thingsPromise }
    <p>...waiting</p>
{:then thingsJson}
    {#each thingsJson.things as thing}
        <p>#{thing.num} {thing.thing}</p>
    {/each}
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}
  