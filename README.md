#  📐 CAD Lab

My learning path for [FreeCAD](https://www.freecad.org/) — and eventually KiCad. This is a place to drop everything I go through while learning: tutorials I follow, quick demos, personal projects, notes and resources.

## 📚 Official docs:
- [FreeCAD Wiki](https://wiki.freecad.org/Main_Page)
  - [Tutorials — Modeling parts](https://wiki.freecad.org/Tutorials#Modeling_parts)

## Structure

- `tutorials/` — guided exercises following official wiki tutorials or videos
- `projects/` — real things I design for myself (will show up when the first one lands)

Convention: each exercise lives in its own folder, and the `.FCStd` file is named after the folder (e.g. `tutorials/01-simple-part-with-part-design/01-simple-part-with-part-design.FCStd`). Each folder also has an `.stl` export of the final part — GitHub doesn't render FCStd files, but it does render STL with an interactive 3D viewer.

### Exporting STL

From the repo root, regenerate all STL exports with:

```bash
freecadcmd scripts/export-stl.py
```

The script walks every `.FCStd` in the exercise folders and writes the matching `.stl` next to it. Run it whenever a model changes.

## Timeline

### 2026-07-16 — Getting started with Part Design

Created this repo and went through the first two Part Design tutorials: sketching, pads, pockets, and building a part from multiple sketches on different faces.

- ✅ [01 — Simple Part with Part Design](./tutorials/01-simple-part-with-part-design/) · [Wiki](https://wiki.freecad.org/Creating_a_simple_part_with_PartDesign) · [Video](https://youtu.be/FVKhejma69U)
- ✅ [02 — Basic Part Design Tutorial](./tutorials/02-basic-part-design-tutorial/) · [Wiki](https://wiki.freecad.org/Basic_Part_Design_Tutorial_019) · [Video](https://www.youtube.com/watch?v=c1K-jBWytSQ) · [Video (alt)](https://www.youtube.com/watch?v=0-Chk84Le9E)

## Resources

Videos, articles and links worth keeping around:

- [FreeCAD 1.1 is Finally HERE — It's a GAME CHANGER! (Major Updates you missed)](https://www.youtube.com/watch?v=bYdobpjTypg) — Deltahedra's overview of what's new in FreeCAD 1.1
- [25 FreeCAD Hacks (You probably don't know)](https://www.youtube.com/watch?v=vwXklzvvxIA) — Deltahedra's tips and tricks collection
- [STOP using FreeCAD WRONG! Do this INSTEAD (Workflow & Tips)](https://youtu.be/JjFh8vtMBC8) — Deltahedra on proper workflow and modeling habits
