<script lang="ts">
import { numberWithCommas } from "../../src/helpers/formatting";
import type Thing from "src/types/thing";

export let thing: Thing;
export let old = false;

let c = old ? "old" : "new"
</script>
    

<tr class={c}>
    <td class="numbering">#{numberWithCommas(thing.num)}</td>
    <td>{thing.thing.toUpperCase()}</td>
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
    width: 85px
}
</style>

