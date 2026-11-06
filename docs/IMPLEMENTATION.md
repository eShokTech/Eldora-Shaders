# Implementation Notes

## Original ELDORA shader code

The first authored module is src/shaders/eldora_color_grade.sh, a BGFX include helper. It is not a standalone shader entry point.

The helper defines a low-cost terrain color grade intended to be integrated after vanilla terrain lighting and before fog:

- preserves near-vanilla daylight;
- introduces a restrained cool tint as sky illumination falls;
- warms areas already illuminated by Minecraft block light;
- avoids additional texture reads, loops, derivatives, and screen-space passes.

The module does not create dynamic lights. Torch and lantern influence is limited by the game's own block-light map. Its lightmap channel assumptions must be checked against the exact RenderChunk interface before integration.

## Reference-pack inspection (user supplied)

The supplied Newb-Complementary-REIMAGINED-Multiplatform.mcpack identifies itself as a v26.60 pack and contains renderer/materials/RenderChunk.material.bin (7,936,915 bytes), alongside other compiled material binaries.

Its COPYRIGHT.txt states that the compiled Newb pack is CC BY-ND 4.0 and may only be redistributed unmodified; it also points to a separately MIT-licensed source repository. ELDORA will not copy, patch, bundle, or redistribute this compiled material. The pack is used only to inspect high-level layout and target-era compatibility clues. The compiled binary is not treated as a vanilla base or as source code.

## Compiler compatibility

The target is Minecraft Bedrock 1.26.60.6. Lazurite's 0.11.0 changelog states that its material change is incompatible with versions 26.50.25 through 26.60.21; Lazurite 0.12.0 adds ESSL_320 support for 26.60.28+. Therefore 0.10.0 is the candidate for 1.26.60.6, subject to confirming the actual material version in the target vanilla binary. Do not compile the target using 0.12.0 by default.

## Integration gate

The helper is not a complete RenderDragon material and is not yet a distributable shader pack. Before integration and packaging, the project must pin and validate:

1. the exact Android material version used by Minecraft 1.26.60.6;
2. a legitimate vanilla material base or another independently licensed build route;
3. the matching Lazurite compiler release and Android ESSL toolchain;
4. the RenderChunk shader interface and all required pass variants;
5. successful compilation and a clean import/load test.

The project will not bundle a placeholder material or a resource pack mislabeled as a shader.

## Compatibility note

RenderDragon shader packs are unofficial and require a compatible loader on Android. Minecraft updates can invalidate material binaries or loader patches. ELDORA's first test build is intended for an isolated disposable world, not the main ELDORA world.
