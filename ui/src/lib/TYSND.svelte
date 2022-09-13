<script>
    import { getContext } from "svelte";
    import Board from "./Board.svelte";

    export let all_catalogue;

    let pathProps = getContext("pathProps");
    let part = pathProps.part;
    let catalogueEntry = all_catalogue[part];

    async function getThings() {
        const res = await fetch(`/data/parts/${part}.json`);
        const values = await res.json();

        return values;
    }

    let thingsPromise = getThings();
</script>

{#await thingsPromise}
    <!-- Default shit -->
{:then thingsJson}
    <Board
        {part}
        startNum={catalogueEntry.startNum}
        newThings={thingsJson.newThings}
        oldThings={thingsJson.oldThings}
    />
{:catch error}
    {"Not ready yet! ;)"}
{/await}
