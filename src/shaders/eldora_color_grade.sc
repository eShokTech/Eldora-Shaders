// ELDORA Shaders - original color grading module
// Target: RenderDragon / BGFX shader source (ESSL Android profile).
// This file contains ELDORA-authored math only. It does not replace the
// game's material interface or claim to be a complete compiled material.
//
// Integration point (once the exact 26.60 RenderChunk material interface is
// pinned): apply eldora_grade_terrain() to the lit terrain RGB before fog.
// Inputs are the sampled vanilla-lit color and the chunk lightmap UV.

#ifndef ELDORA_COLOR_GRADE_SC
#define ELDORA_COLOR_GRADE_SC

// Gentle warm daylight, restrained cool night ambience and practical
// torch warmth. Deliberately avoids crushing shadows or expensive sampling.
vec3 eldora_grade_terrain(vec3 litColor, vec2 lightmapUV) {
    float skyLight = clamp(lightmapUV.x, 0.0, 1.0);
    float blockLight = clamp(lightmapUV.y, 0.0, 1.0);

    // Keep the daylight close to vanilla and introduce a slow cool shift
    // only as sky illumination falls.
    float nightAmount = 1.0 - smoothstep(0.12, 0.62, skyLight);
    vec3 nightTint = vec3(0.78, 0.84, 1.04);
    vec3 graded = mix(litColor, litColor * nightTint, nightAmount * 0.34);

    // Warm local light without inventing light sources or adding screen
    // space passes. The game's own block-light map remains authoritative.
    float torchAmount = smoothstep(0.04, 0.72, blockLight);
    vec3 torchTint = vec3(1.06, 0.91, 0.72);
    graded = mix(graded, graded * torchTint, torchAmount * 0.22);

    // A restrained filmic shoulder protects bright blocks and sky-lit areas.
    // This is intentionally low-cost and does not use derivatives,
    // additional texture fetches, loops, or time-dependent uniforms.
    graded = graded / (vec3(1.0) + max(graded - vec3(0.82), vec3(0.0)) * 0.12);

    return max(graded, vec3(0.0));
}

#endif // ELDORA_COLOR_GRADE_SC
