# AnvilWiki demo fixtures

Frozen input from ce64308f494df793f07c5b0b304737a65c61eba4, retained for the existing template migration tests. These are test inputs, not wiki content. Demo-marker and author-removal assertions continue to run against original inputs after this fork changes its live identity.

2026-10-10: original wrangler header, landing-route sources, redirect mapping and ad HTML are frozen here so behavioural migration assertions remain active after the fork removes their public counterparts. Test fixtures are excluded from application typecheck/lint and are never copied into the build.
