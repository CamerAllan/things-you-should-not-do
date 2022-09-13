<script lang="ts">
    export let path;
    let handleLinkClick = (event: MouseEvent) => {
        // stop the browser from changing the URL and requesting the new document
        event.preventDefault();
        // push an entry into the browser history stack and change the URL
        window.history.pushState({}, undefined, path);
    };
</script>

<a href={path} on:click={handleLinkClick}>
    <slot />
</a>

<style>
    a {
        color: black;
    }
</style>
