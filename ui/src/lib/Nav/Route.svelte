<script lang="ts">
    import { getContext, setContext } from "svelte";

    export let path: string;
    let pathElements = path.split("/");

    let currentPath = getContext("path") as string;
    let currentPathElements = currentPath.split("/");

    // Identify positions of params in path
    let paramIndices: number[] = [];
    for (let [i, pe] of pathElements.entries()) {
        const elementIsParam = pe.match(/\{([^)]+)\}/);
        if (elementIsParam) {
            paramIndices.push(i);
        }
    }

    let matched = true;
    // PathElements must be same length
    if (pathElements.length != currentPathElements.length) {
        matched = false;
    }

    // Every part of path must match
    for (let [i, cpe] of currentPathElements.entries()) {
        // Unless it's a parameter
        if (paramIndices.includes(i)) {
            continue;
        }
        if (cpe != pathElements[i]) {
            matched = false;
        }
    }

    // If it's a match, pass path props in context
    if (matched) {
        const pathProps = {};
        for (const pi of paramIndices) {
            const paramName = pathElements[pi]
                .replace("{", "")
                .replace("}", ""); // Disgusting
            pathProps[paramName] = currentPathElements[pi];
        }
        setContext("pathProps", pathProps);
    }
</script>

{#if matched}
    <slot />
{/if}
