<script lang="ts">
    import { setContext } from "svelte";
    setContext("path", window.location.pathname);
</script>

<slot />
