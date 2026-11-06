# ELDORA RenderChunk build pipeline

## Target lock

- Game: Minecraft Bedrock Android 1.26.60.6 (Build 52886189)
- Material platform: ESSL_310
- Lazurite: pin v0.10.0. Its changelog supports material format 26 (26.50.25+) and records that v0.11.0 is incompatible with materials 26.50.25 through 26.60.21.
- Vanilla merge source: the user's own `RenderChunk.material.bin`, extracted from their installed 1.26.60.6 build.

## What the supplied binary can and cannot do

The supplied Android binary is accepted as the exact target-version merge source. It is not a readable GLSL source archive. Lazurite's guide documents that Android materials from 1.21.31.05 onward no longer ship readable shader source, so `lazurite restore` cannot reconstruct the original source from this file.

Lazurite's guide points to the mcbe-shader-codebase project as a source of previously restored vanilla shader code. That repository describes its contents as auto-generated vanilla Minecraft shader code, but the currently inspected branch is not proven to match this exact 1.26.60.6 material. ELDORA will not copy or adapt third-party shader implementations. Any such vanilla reference may only be used to understand the engine interface and variant requirements; ELDORA's implementation remains independently authored.

## Required Lazurite project shape

```
eldora-build/
├── project.json
├── RenderChunk/
│   └── shaders/
│       ├── bgfx_shader.sh
│       ├── fragment.sc
│       ├── vertex.sc
│       └── varying.def.sc
└── vanilla/
    └── RenderChunk.material.bin
```

The source files must be a complete BGFX shader implementation for the selected RenderChunk passes and flags. The vanilla material is the merge base for unmodified material data and variants.

## Compiler

- Lazurite candidate: v0.10.0
- BGFX `shaderc`: required
- Android targets: ESSL_300 and ESSL_310 are supported by the documented Android profile; ESSL_310 is required for this target.
- Build command: `lazurite build ./eldora-build -p android`

The matching shaderc executable must be available to Lazurite. A successful compile proves only that the material was built, not that Minecraft loads it correctly.

## Release gates

1. Verify the exact target material metadata and pass/flag domain using Lazurite v0.10.0.
2. Author an independent BGFX source pair and varying definitions for the passes being overridden.
3. Preserve all other passes and variants through the exact vanilla merge source.
4. Compile Android ESSL_310.
5. Inspect the output material and confirm required passes/variants remain present.
6. Package the compiled binary under `renderer/materials/RenderChunk.material.bin` with a valid resource-pack manifest.
7. Import and test in a disposable world on the target Android build.
8. Profile frame pacing and thermal behavior on the SM-A266M.

## Current blocker

The exact vanilla merge binary is available. The original Android shader source is not recoverable from that binary with Lazurite because the game version obfuscates it. ELDORA still needs a complete independently authored BGFX shader source implementation and a working shaderc build environment. The current opaque GLSL sketch is not a valid drop-in RenderChunk replacement and must not be packaged as one.
