// ELDORA Shaders: original color grading helpers.
// Include this file from the RenderChunk fragment shader after BGFX headers.
// The caller supplies vanilla-lit RGB and the game's lightmap UV.

#ifndef ELDORA_COLOR_GRADE_SH
#define ELDORA_COLOR_GRADE_SH

vec3 eldoraGradeTerrain(vec3 litColor, vec2 lightmapUV) {
    float skyLight = clamp(lightmapUV.x, 0.0, 1.0);
    float blockLight = clamp(lightmapUV.y, 0.0, 1.0);

    float nightAmount = 1.0 - smoothstep(0.12, 0.62, skyLight);
    vec3 nightTint = vec3(0.78, 0.84, 1.04);
    vec3 graded = mix(litColor, litColor * nightTint, nightAmount * 0.34);

    float torchAmount = smoothstep(0.04, 0.72, blockLight);
    vec3 torchTint = vec3(1.06, 0.91, 0.72);
    graded = mix(graded, graded * torchTint, torchAmount * 0.22);

    graded = graded / (vec3(1.0) + max(graded - vec3(0.82), vec3(0.0)) * 0.12);
    return max(graded, vec3(0.0));
}

#endif
