Had a go at hacking a router together, there's a couple things I didn't think of up front:

- Default/404 route
    - Need a way to detect when no routes match, would probs need to use some kind of lifecycle event on the Route component
    - Then could set matched on load and unmatched on unload
    - Don't know svelte well and more exciting things to work on, just needed a way to get params from URL really