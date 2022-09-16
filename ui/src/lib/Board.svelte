<script lang="ts">
  import { numberWithCommas } from "../helpers/formatting";

  import Things from "./Things.svelte";

  export let latestPart: string;
  export let currentPart: string;
  export let startNum: number;
  export let things: string[] = [];

  $: isNewPart = currentPart == latestPart;
</script>

<div class="board">
  <div class="board-h1">THINGS YOU SHOULD NOT DO</div>
  <div class="board-h2">
    (PART <a href={`/part/${currentPart}`}
      >{numberWithCommas(Number.parseInt(currentPart))}</a
    >
    OF ????)
  </div>

  {#if isNewPart}
    <div class="separator fauxtalics">NEW!</div>
  {/if}
  <Things old={!isNewPart} {startNum} {things} />
</div>

<style>
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
    margin-right: 0.25rem;
  }

  .separator:not(:empty)::after {
    margin-left: 0.25rem;
  }

  @media (prefers-color-scheme: light) {
    .board {
      border-color: white;
    }
  }
  
  @media (prefers-color-scheme: light) {
    .board {
      border-color: black;
    }
  }

  .board {
    max-width: 420px;
    border-width: 3px;
    border-style: solid;
    padding: 25px;
    margin: auto;
  }

  .board-h1 {
    font-size: 2rem;
    padding-bottom: 5px;
  }

  .board-h2 {
    font-size: 1.2rem;
    padding-bottom: 5px;
  }
</style>
