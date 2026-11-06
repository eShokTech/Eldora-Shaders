# ELDORA RenderChunk build pipeline

## Target lock

- Game: Minecraft Bedrock Android 1.26.60.6 (Build 52886189)
- Material platform: ESSL_310
- Lazurite: pin v0.10.0. Lazurite v0.11.0 changes the Buffer schema incompatibly for materials 26.50.25 through 26.60.21; v0.12.0 adds ESSL_320 for 26.60.28+.
- Source base: the user's own `RenderChunk.material.bin`, extracted from their installed 1.26.60.6 build. Use it as the vanilla merge source, not as readable shader source.

## Project layout required by Lazurite

```
eldora-build/
├── project.json
├── RenderChunk/
│   ├── config.json
│   └── shaders/
│       ├── bgfx_shader.sh
│       ├── fragment.sc
│       ├── vertex.sc
│       └── varying.def.sc
└── vanilla/
    └── RenderChunk.material.bin
```

## Build configuration

`project.json` must point `merge_source` to the vanilla folder and target Android. The material config must select the BGFX `shaderc` compiler and ESSL_310. The build command is:

```sh
lazurite build ./eldora-build -p android
```

The matching `shaderc` executable must be installed and passed/configured as required by the Lazurite build command. A successful command only proves compilation, not in-game compatibility.

## Hard release gates

1. Preserve the complete RenderChunk pass/flag domain from the target vanilla material.
2. Supply a complete BGFX vertex/fragment source pair and varying definitions.
3. Compile all required ESSL_310 variants against the exact vanilla merge source.
4. Confirm the output material contains all expected passes and variants.
5. Package it under `renderer/materials/RenderChunk.material.bin` with a valid resource-pack manifest.
6. Import and test in a disposable world on the target Android build.
7. Only then label the output as an installable ELDORA shader.

## Current blocker

The extracted Android material is the correct versioned vanilla merge base, but it does not expose readable original GLSL source. The previously authored ELDORA grading helper and opaque-pass sketch do not yet constitute the complete BGFX source pair or the full set of RenderChunk variants. Do not compile or ship the sketch as a replacement material.
