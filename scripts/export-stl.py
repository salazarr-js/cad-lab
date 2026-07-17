# Regenerates, next to every .FCStd under tutorials/ (and projects/, when it exists):
#   - <name>.stl   -> the mesh, rendered by GitHub's interactive 3D viewer
#   - preview.png  -> a clean isometric render of the mesh, used inline in the README
#
# The preview is rendered from the .stl with OpenSCAD (headless), NOT the thumbnail
# FreeCAD embeds in the .FCStd - so the framing is always centered, isometric, and
# free of origin axes regardless of how the view was left when the file was saved.
#
# Run from the repo root: freecadcmd scripts/export-stl.py
import glob
import os
import shutil
import subprocess
import tempfile

import FreeCAD
import Mesh

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# OpenSCAD renders the previews; it's optional. Without it the STLs are still
# exported and each missing preview is just reported as a warning.
OPENSCAD = shutil.which("openscad") or shutil.which(
    "openscad", path="/opt/homebrew/bin:/usr/local/bin"
)
# camera = translate(x,y,z), rotate(x,y,z), distance - translate/distance are
# overridden by --viewall/--autocenter, so only the isometric rotation matters.
RENDER_ARGS = [
    "--imgsize=600,600",
    "--projection=o",
    "--autocenter",
    "--viewall",
    "--camera=0,0,0,55,0,25,50",
    "--colorscheme=Tomorrow",
]


def render_preview(stl):
    """Render a centered isometric PNG from the mesh via OpenSCAD.

    Returns the output path, or None if OpenSCAD is missing or the render fails
    - the caller warns and moves on, so a missing OpenSCAD never blocks the STLs.
    """
    if not OPENSCAD:
        return None
    out = os.path.join(os.path.dirname(stl), "preview.png")
    scad = tempfile.NamedTemporaryFile(mode="w", suffix=".scad", delete=False)
    try:
        scad.write('import("%s");\n' % stl)
        scad.close()
        subprocess.run(
            [OPENSCAD, "-o", out, *RENDER_ARGS, scad.name],
            check=True,
            capture_output=True,
        )
        return out
    except (OSError, subprocess.CalledProcessError) as err:
        print(f"  ! preview render failed for {os.path.basename(stl)}: {err}")
        return None
    finally:
        os.unlink(scad.name)


for fcstd in sorted(glob.glob(os.path.join(root, "*", "*", "*.FCStd"))):
    doc = FreeCAD.openDocument(fcstd)
    bodies = [o for o in doc.Objects if o.TypeId == "PartDesign::Body"]
    if bodies:
        stl = os.path.splitext(fcstd)[0] + ".stl"
        Mesh.export(bodies, stl)
        print(f"exported: {os.path.relpath(stl, root)}")
        preview = render_preview(stl)
        if preview:
            print(f"preview:  {os.path.relpath(preview, root)}")
        else:
            print(f"preview:  skipped (OpenSCAD not available)")
    else:
        print(f"skipped (no PartDesign body): {os.path.relpath(fcstd, root)}")
    FreeCAD.closeDocument(doc.Name)
