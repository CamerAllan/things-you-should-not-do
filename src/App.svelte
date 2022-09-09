<script lang="ts">
  import Board from './lib/Board.svelte'
  import Example from './lib/Example.svelte'
</script>

<main>

  <div class="card">
    <Board />
    <Example />
  </div>

</main>

<style>

	@font-face {
		font-family: 'xkcd';
		font-weight: 500;
		src: url('/fonts/xkcd.otf') format('opentype'); 
	}

	@font-face {
		font-family: 'xkcd-regular';
		font-weight: 500;
		src: url('/fonts/xkcd-Regular.otf') format('opentype'); 
	}
</style>