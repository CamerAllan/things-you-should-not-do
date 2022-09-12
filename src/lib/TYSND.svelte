<script>
import Board from "./Board.svelte";

async function getAircrafts() {
    const res = await fetch('/data/12-09-22-1.json');
    const values = await res.json();

    return values;
}

// NOTE await not used here! 
let thingsPromise = getAircrafts();
</script>

{#await thingsPromise}
Uhh
<!-- Default shit -->
{:then thingsJson}
<Board newThings={thingsJson.newThings} oldThings={thingsJson.oldThings}/>
{:catch error}
<p style="color: red">{error.message}</p>
{/await}