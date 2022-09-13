<script lang="ts">
  import { numberWithCommas } from "../helpers/formatting";
  import type Thing from "src/types/thing";

  import Things from "./Things.svelte";
  import Link from "./Nav/InternalLink.svelte";

  export let part: string;
  export let newThings: Thing[] = [];
  export let oldThings: Thing[] = [];
</script>

<div class="board">
  <div class="board-h1">THINGS YOU SHOULD NOT DO</div>
  <div class="board-h2">
    (PART <Link path={`/part/${part}`}
      >{numberWithCommas(Number.parseInt(part))}</Link
    > OF ????)
  </div>

  <Things things={oldThings} old={true} />

  <div class="separator fauxtalics">NEW!</div>
  <Things things={newThings} />
</div>

<style>
  .fauxtalics {
    transform: skew(-15deg, 0deg);
  }

  .separator {
    display: flex;
    align-items: center;
    text-align: center;
  }

  .separator::before,
  .separator::after {
    content: "";
    flex: 1;
    border-bottom: 2px solid #000;
  }

  .separator:not(:empty)::before {
    margin-right: 0.25em;
  }

  .separator:not(:empty)::after {
    margin-left: 0.25em;
  }

  .board {
    width: 420px;
    border-color: black;
    border-width: 3px;
    border-style: solid;
    padding: 1.5em;
  }

  .board-h1 {
    font-size: 2em;
    padding-bottom: 0.15em;
  }

  .board-h2 {
    font-size: 1.2em;
    padding-bottom: 0.15em;
  }
</style>
