# Development status

## Current milestone: original shader module

- [x] Dedicated public repository created.
- [x] Target device and game profile recorded (SM-A266M, Android 16, Bedrock 1.26.60.6).
- [x] Visual direction and performance priorities recorded.
- [x] Original ELDORA terrain color-grading module authored.
- [x] Integration and release validation gates documented.
- [ ] Pin exact Android RenderDragon material version for Bedrock 1.26.60.6.
- [ ] Confirm matching Lazurite compiler and native material base.
- [ ] Integrate the original grading module into all required RenderChunk passes.
- [ ] Compile Android shader material binaries.
- [ ] Build the .mcpack.
- [ ] Validate import and activation in a separate Minecraft world.
- [ ] Profile frame rate and thermal behavior on SM-A266M.
- [ ] Publish verified .mcpack release.

## Current artifact state

There is original shader source in the repository, but there is **no compiled .mcpack yet**. The current module is not independently loadable as a shader pack.

## Release gate

Do not label any artifact as a playable ELDORA shader until it is compiled for the exact Android material version and tested in Minecraft. Documentation or a generic resource pack is not an acceptable substitute.
