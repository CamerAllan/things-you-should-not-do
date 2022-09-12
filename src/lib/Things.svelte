<script lang="ts">
import Thing from "./Thing.svelte";

export let things = []
export let old = false;

</script>

<table cellspacing="0" cellpadding="0">
    <tbody>
        {#each things as thing}
            <Thing thing={thing} old={old}/>
        {/each}
    </tbody>
</table>

<style>

table {
    border-collapse: collapse;
}

</style>