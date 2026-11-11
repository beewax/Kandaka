# Image workflow no-change push repair

Investigated run [43039077414](https://github.com/beewax/Kandaka/actions/runs/43039077414), attempt1, checkoute280c5d7518a16a4a9f138f0fac09ea6eeb6438c. The fetch succeeded and wrote0newimages. The unconditional push then failed at2026-11-11T14:32:31Z because main had advanced. No images were lost or published by that run.

Fresh mainc2d242c856353ee82bf576b2409bb4f2a2fcf6bf still contained the same unconditional push. Recent workflow-run history contained no later image run; the preceding10November run42839667035 succeeded. Success of a previous run did not repair the race.

The commit step now exits successfully before commit/push when its staged image diff is empty. A real image change still commits only `content/images/` and pushes normally. Genuine changed-content push conflicts remain visible; no force push, automatic conflict resolution, permission expansion, workflow cadence, fetcher, secret or image/publication change is included.

Verification: `scripts/test_image_workflow_commit.py` executes the actual workflow shell block against temporary local Git repositories and bare remotes. All3tests pass: unchanged/stale checkout leaves local and advanced remote heads unchanged; new image commits/pushes with unrelated untracked files excluded; changed-content non-fast-forward failure remains nonzero and preserves remote work. `git diff --check` passes. No site build is needed for this workflow-only repair; commit skips Netlify.

Separate source outcomes in the failed run:

- DPLA: HTTP403. The masked request showed an encoded trailing newline (`%0A`) in its key parameter. This is a credential-formatting lead, not proof of the403cause. No key was retrieved, exposed, modified or retried through another route.
- Library of Congress: read timeout using the fetcher's15second timeout. This is not evidence of an access denial or an empty source catalogue.
- National Archives: `NARA_API_KEY` was absent; the fetcher correctly skipped the source. The owner would need valid authorized API access for this source.
- Wikimedia, Europeana and Flickr selections were already catalogued; Smithsonian returned no result. No duplicate candidate was forced into the catalogue.

These source limitations are not fixed or hidden by the Git guard. A future workflow run remains the production verification of this change; local integration tests do not certify external API recovery.
