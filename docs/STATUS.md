# Development status

## Current milestone: RenderChunk integration

- [x] Dedicated public repository created.
- [x] Target device and game profile recorded (SM-A266M, Android 16, Bedrock 1.26.60.6).
- [x] Visual direction and performance priorities recorded.
- [x] Original ELDORA terrain color-grading helper authored as a BGFX include (src/shaders/eldora_color_grade.sh).
- [x] Integration and release validation gates documented.
- [x] A user-supplied Bedrock 1.26.60-labelled shader pack was inspected for format and compatibility research.
- [x] Confirmed that the sample contains a compiled renderer/materials/RenderChunk.material.bin (7,936,915 bytes).
- [x] Confirmed that the sample's compiled material is part of the Newb pack and is not a vanilla base; it will not be copied, modified, or redistributed in ELDORA.
- [ ] Pin the exact Android RenderDragon material version for Bedrock 1.26.60.6.
- [ ] Obtain a legitimate vanilla material base or another independently licensed build route.
- [ ] Confirm the matching Lazurite compiler and Android shader compiler.
- [ ] Author the complete original RenderChunk fragment entry point and required pass variants.
- [ ] Compile Android shader material binaries.
- [ ] Build the ELDORA .mcpack.
- [ ] Validate import and activation in a separate Minecraft test world.
- [ ] Profile frame rate and thermal behavior on SM-A266M.
- [ ] Publish a verified release.

## Current artifact state

The repository contains original ELDORA shader helper source, but there is **no compiled or playable ELDORA .mcpack yet**. The uploaded reference pack proves that the target-era resource-pack layout includes a compiled RenderChunk material, but its binary is a third-party compiled artifact and is not a clean vanilla build base.

## Release gate

Do not label any artifact as a playable ELDORA shader until it is compiled for the exact Android material version and tested in Minecraft. A reference pack, documentation-only change, or generic resource pack is not an acceptable substitute.
