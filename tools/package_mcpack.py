#!/usr/bin/env python3
"""Package a compiled ELDORA RenderChunk material into a Bedrock .mcpack.

This script deliberately refuses to package source sketches or an absent/empty
material binary. It is a packaging step, not a shader compiler.
"""
from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

PACK_UUID = "a5b3a0d1-6f47-4f75-a0f0-2e9a7c6d1e11"
MODULE_UUID = "c7e2f4a9-1b36-4e80-9d52-7f0a6b3c8e22"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--material", type=Path, required=True,
                        help="Compiled RenderChunk.material.bin from Lazurite")
    parser.add_argument("--output", type=Path, default=Path("ELDORA_Shader.mcpack"))
    parser.add_argument("--version", default="0.1.0")
    args = parser.parse_args()

    material = args.material
    if not material.is_file() or material.stat().st_size < 1024:
        parser.error("Compiled material missing or implausibly small; refusing to create a pack.")

    manifest = {
        "format_version": 2,
        "header": {
            "name": "ELDORA Shaders",
            "description": "Original ELDORA RenderDragon shader for Bedrock Android.",
            "uuid": PACK_UUID,
            "version": [0, 1, 0],
            "min_engine_version": [1, 26, 60]
        },
        "modules": [{
            "type": "resources",
            "uuid": MODULE_UUID,
            "version": [0, 1, 0]
        }]
    }
    # Keep manifest version synchronized with the requested semantic version.
    parts = args.version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        parser.error("--version must be MAJOR.MINOR.PATCH")
    manifest["header"]["version"] = [int(p) for p in parts]
    manifest["modules"][0]["version"] = [int(p) for p in parts]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED) as pack:
        pack.writestr("manifest.json", json.dumps(manifest, indent=2) + "\\n")
        pack.write(material, "renderer/materials/RenderChunk.material.bin")

    with zipfile.ZipFile(args.output) as check:
        required = {"manifest.json", "renderer/materials/RenderChunk.material.bin"}
        if not required.issubset(set(check.namelist())):
            raise RuntimeError("Package validation failed: required entries missing.")
    print(f"Packaged {args.output} ({args.output.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
