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
    .old {
        opacity: 0.5;
    }

    td {
        vertical-align: top;
        font-size: 1.1em;
        padding-top: 0.4em;
        line-height: 1em;
    }

    .numbering {
        width: 70px;
    }
</style>
