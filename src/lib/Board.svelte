<script lang="ts">
    let count: number = 0
    const increment = () => {
        count += 1
    }
</script>

<div class="board">
    <div class="board-h1">THINGS YOU SHOULD NOT DO</div>
    <div class="board-h2">(PART N OF ????)</div>
</div>

<style>

.board {
    max-width: 900px;
    min-width: 500px;
    border-color: black;
    border-width: 1;
    border-style: solid;
    padding: 1.5em;
}

.board-h1 {
    font-size: 2em;
    padding-bottom: 0.15em;
}

.board-h2 {
    font-size: 1.2em;
}

</style>
