# ELDORA Shaders: specification

## Product target

An original RenderDragon shader/resource-pack project for Minecraft Bedrock Android 1.26.60.x, designed around a performance-first target on the Samsung Galaxy A26 5G (SM-A266M).

## Art direction

### Day
- Preserve natural readability and vanilla-like visibility.
- Avoid global darkening and crushed shadows.
- Keep color treatment restrained and medieval-fantasy in tone.

### Golden hours
- Gradual sunrise and sunset transitions.
- Warm amber light near the horizon without a hard color jump.

### Night
- Deep blue atmosphere.
- Darker and more threatening than day, but navigable.
- No pitch-black exposure; retain useful environmental visibility.

### Artificial light
- Torches, lanterns, and campfires should read as warm light sources and recognizable safe points.
- Avoid expensive effects that require broad-screen blur or costly multi-pass processing unless profiling proves viable.

### Weather and biomes
- Fog should respond to biome atmosphere where supported by the target shader pipeline.
- Rain should increase fog density and soften distant visibility.
- Weather changes should remain gradual.

## Performance constraints

- Performance is the primary quality target.
- Avoid unnecessary screen-space passes, high sample counts, and costly volumetrics.
- Establish a baseline before enabling optional effects.
- Test frame pacing and device temperature on the target phone, not only on desktop.

## Compatibility and validation

- Target Bedrock 1.26.60.x / Android RenderDragon.
- Verify the exact shader packaging and loader requirements for the target game build before release.
- A successful CI build is not proof of in-game compatibility.
- Test only in a disposable world until visual, stability, and performance checks pass.

## Originality and licensing

ELDORA shader source must be written independently. External repositories may be studied for technical interfaces, documented formats, build systems, and compatibility notes only. Do not copy or adapt their shader implementation or precompiled packs.
