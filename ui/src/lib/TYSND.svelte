<script>
    import { getContext } from "svelte";
    import Board from "./Board.svelte";

    let pathProps = getContext("pathProps");
    let part = pathProps["part"];

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
        newThings={thingsJson.newThings}
        oldThings={thingsJson.oldThings}
    />
{:catch error}
    {"Not ready yet! ;)"}
{/await}
