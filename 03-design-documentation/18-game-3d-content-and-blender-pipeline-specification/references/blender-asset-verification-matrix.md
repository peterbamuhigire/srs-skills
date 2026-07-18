# Blender Asset Verification Matrix

| Gate | Minimum oracle | Evidence |
|---|---|---|
| Source integrity | Opens with pinned version; required links/add-ons resolve | validation log |
| Transform/hierarchy | Units, scale, axes, origin, parentage and names match contract | structural diff |
| Geometry | Manifold/deformation/normal/material-slot rules pass | validator report |
| UV/bake/material | UV policy, texture set and target-renderer parity pass approved cases | engine captures |
| Rig/deformation | Export skeleton and extreme-pose matrix pass; controls are not leaked | pose report |
| Animation | Clip identity, range, rate, root motion, events and loops match | animation diff |
| Collision/LOD | Collision behaviour, transitions, bounds and shadows pass | stress-scene record |
| Clean re-import | New project/import reproduces expected asset from named source/export preset | reproducibility log |
| Runtime budget | Named build/scene/device/simultaneous count meets project threshold | profiler capture |
| Rights/culture | Provenance and named scoped approval exist | review register |

An unavailable check is `not assessed`, never passed. Retain failed cases with the same lineage as successful evidence.
