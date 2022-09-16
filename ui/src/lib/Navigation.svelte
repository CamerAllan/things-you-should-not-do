<script lang="ts">
    export let firstPart;
    export let latestPart;
    export let currentPart;
    $: currentPartInt = Number.parseInt(currentPart);
</script>

<div class="navContainer">
    <a class="navItem" href={`/part/${firstPart}`}>{"|<"}</a>
    {#if currentPart > firstPart && currentPart <= latestPart}
        <a class="navItem" href={`/part/${currentPartInt - 1}`}>{"<"}</a>
    {/if}
    {#if currentPart < latestPart && currentPart >= firstPart}
        <a class="navItem" href={`/part/${currentPartInt + 1}`}>{">"}</a>
    {/if}
    <a class="navItem" href={`/part/${latestPart}`}>{">|"}</a>
</div>

<style>
    .navContainer {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        padding-top: 15px;
        padding-bottom: 15px;
    }

    .navItem {
        width: 20px;
        text-align: center;
    }
</style>
