<script lang="ts">
	import Router from "./lib/Nav/ClientSideRouter.svelte";
	import Route from "./lib/Nav/Route.svelte";
	import Redirect from "./lib/Redirect.svelte";
	import Tysnd from "./lib/TYSND.svelte";

	async function getCatalogue() {
		const res = await fetch(`/data/catalogue.json`);
		const values = await res.json();

		return values;
	}

	let cataloguePromise = getCatalogue();
</script>

<main>
	<Router>
		{#await cataloguePromise}
			<!-- Default shit -->
		{:then catalogue}
			<Route path={"/"}>
				<Redirect path={`/part/${catalogue.latest}`} />
			</Route>
			<Route path={"/part/{part}"}>
				<Tysnd all_catalogue={catalogue.all} />
			</Route>
		{:catch error}
			{"Not ready yet! ;)"}
		{/await}
	</Router>

	<br />
	Maintained by Cameron Allan. <br />
	Based on <a href={"https://xkcd.com/2669/"}>this comic</a> by XKCD
</main>

<style>
	@font-face {
		font-family: "xkcd";
		src: url("/fonts/xkcd-script.ttf");
	}
</style>
