# Development status

## Current milestone: RenderChunk source integration

- [x] Dedicated public repository created.
- [x] Target device and game profile recorded (SM-A266M, Android 16, Bedrock 1.26.60.6 / Build 52886189).
- [x] Visual direction and performance priorities recorded.
- [x] Original ELDORA terrain color-grading helper authored.
- [x] User supplied the exact vanilla `RenderChunk.material.bin` extracted from their own Minecraft 1.26.60.6 installation.
- [x] Confirmed the supplied vanilla material is the correct versioned merge base; it is not readable source code.
- [x] Pinned Lazurite v0.10.0 as the candidate compiler version for material format 26 / game 26.60.6.
- [x] Added the documented Android RenderChunk build pipeline.
- [ ] Build a complete BGFX RenderChunk vertex/fragment source pair and varying definitions.
- [ ] Preserve all target material passes, flags, and variants.
- [ ] Obtain/run matching shaderc and compile ESSL_310 Android variants.
- [ ] Package compiled material into an ELDORA resource pack.
- [ ] Validate import and activation in a separate Minecraft test world.
- [ ] Profile frame pacing and thermal behavior on SM-A266M.
- [ ] Publish a verified release.

## Current artifact state

The repository contains original ELDORA grading code and an experimental opaque fragment sketch. Neither is a complete replacement for the RenderChunk material. There is no compiled ELDORA `.mcpack` yet.

The user's vanilla `RenderChunk.material.bin` is accepted as the exact target-version merge source. The remaining blocker is reconstructing and authoring the complete BGFX pass/variant source and running the matching compiler.

## Release gate

Do not label an artifact as a playable ELDORA shader until it is compiled for the exact Android material version and tested in Minecraft. A source prototype or generic resource pack is not an acceptable substitute.
