<script lang="ts">
    import Thing from "./Thing.svelte";

    export let startNum: number;
    export let things = [];
    export let old = false;
</script>

<table cellspacing="0" cellpadding="0">
    <tbody>
        {#each things as thing, i}
            <Thing num={startNum + i} {thing} {old} />
        {/each}
    </tbody>
</table>

<style>
    table {
        border-collapse: collapse;
    }
</style>
