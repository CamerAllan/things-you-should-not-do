<script>
    import { getContext } from "svelte";
    import Board from "./Board.svelte";
    import Navigation from "./Navigation.svelte";

    export let all_catalogue;
    export let latestPart;

    let pathProps = getContext("pathProps");
    let currentPart = pathProps.part;
    let catalogueEntry = all_catalogue[currentPart];

    async function getThings() {
        const res = await fetch(`/data/parts/${currentPart}.json`);
        const values = await res.json();

        return values;
    }

    let thingsPromise = getThings();
</script>

{#await thingsPromise}
    <!-- Default shit -->
{:then thingsJson}
    <Navigation {currentPart} {latestPart} firstPart={3647} />
    <Board
        part={currentPart}
        startNum={catalogueEntry.startNum}
        newThings={thingsJson.newThings}
        oldThings={thingsJson.oldThings}
    />
    <Navigation {currentPart} {latestPart} firstPart={3647} />
{:catch error}
    {"This part is missing!"}
{/await}
