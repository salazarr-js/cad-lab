# Regenerates the .stl export next to every .FCStd under tutorials/ (and projects/, when it exists).
# Run from the repo root: freecadcmd scripts/export-stl.py
import glob
import os

import FreeCAD
import Mesh

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for fcstd in sorted(glob.glob(os.path.join(root, "*", "*", "*.FCStd"))):
    doc = FreeCAD.openDocument(fcstd)
    bodies = [o for o in doc.Objects if o.TypeId == "PartDesign::Body"]
    if bodies:
        out = os.path.splitext(fcstd)[0] + ".stl"
        Mesh.export(bodies, out)
        print(f"exported: {os.path.relpath(out, root)}")
    else:
        print(f"skipped (no PartDesign body): {os.path.relpath(fcstd, root)}")
    FreeCAD.closeDocument(doc.Name)
