# Implementation Notes

## Original shader code

The first authored shader module is `src/shaders/eldora_color_grade.sc`.

It defines a low-cost terrain color grade intended to be called after vanilla terrain lighting and before fog:

- preserves near-vanilla daylight;
- introduces a restrained cool tint as sky illumination falls;
- warms areas already illuminated by Minecraft block light;
- avoids additional texture reads, loops, derivatives, and screen-space passes.

The module does not create dynamic lights. Torch and lantern influence is limited by the game's own block-light map.

## Integration gate

This module is not a complete RenderDragon material and is not yet a distributable shader pack. Before integration and packaging, the project must pin and validate:

1. the exact Android material version used by Minecraft 1.26.60.6;
2. the matching Lazurite compiler release;
3. the Android ESSL shader compiler and vanilla material base;
4. the RenderChunk shader interface and all required pass variants;
5. successful compilation and a clean import/load test.

The project will not bundle a placeholder material or a resource pack mislabeled as a shader.

## Compatibility note

RenderDragon shader packs are unofficial and require a compatible loader on Android. Minecraft updates can invalidate material binaries or loader patches. ELDORA's first test build is intended for an isolated disposable world, not the main ELDORA world.
