<script lang="ts">
    import { numberWithCommas } from "../../src/helpers/formatting";

    export let thing: string;
    export let old = false;
    export let num = 1;

    let c = old ? "old" : "new";
</script>

<tr class={c}>
    <td class="numbering">#{numberWithCommas(num)}</td>
    <td>{thing.toUpperCase()}</td>
</tr>

<style>

    td {
        vertical-align: top;
        font-size: 1.1rem;
        padding-top: 0.4em;
        line-height: 1rem;
    }

    .numbering {
        width: 70px;
    }
</style>
