# Maintaining Jason's GitHub profile

GitHub renders the root `README.md` on Jason's profile. Open the README on your branch to preview changes. The profile uses Markdown, HTML links, and native disclosure controls.

## Repository layout

| Path | Contents |
| --- | --- |
| `README.md` | Introduction, interest cartridges, education, and contribution calendars |
| `assets/studio.webp` | Pixel-art studio cover |
| `assets/cartridges/` | Editable SVGs for basketball, sandbox games, and esports |
| `assets/education/` | City illustrations for the education cards |
| `assets/activity/` | Light and dark 3D calendars refreshed by GitHub Actions |
| `scripts/check_profile.py` | Checks local README references, HTML image descriptions, and SVG markup |
| `.github/workflows/` | Profile checks and contribution calendar updates |

## Editing a cartridge

Find the cartridge's table cell in `README.md`. The linked cover opens an external site. The label underneath opens a disclosure panel with a description and links. Edit the SVG to change its colors or animation. The artwork stays still when a visitor requests reduced motion.

Run the check from the repository root with Python 3.

```sh
python3 scripts/check_profile.py
```

Open all three cartridges on a narrow screen to check that their text fits. For calendar changes, expand the 3D view and inspect both the dark image and the linked light version.

## Refreshing the calendars

- **Antikythera** renders the public commit calendar in its own repository. The profile embeds its published SVG directly. Edit the renderer or refresh the graphic upstream. [Antikythera](https://github.com/hyyyyyyz/antikythera)
- **3D contribution calendar** runs daily. The workflow stages the two SVGs used by the profile. When they change, the GitHub Actions bot commits them to the default branch. These files also work in local previews. [3D calendar generator](https://github.com/yoshi389111/github-profile-3d-contrib)
- Run the 3D calendar workflow manually from the Actions tab on the default branch. It uses the repository’s `GITHUB_TOKEN` and needs write access to that branch.
- **Check profile** runs the local check on pushes and pull requests. Workflow dependencies are pinned to commits. Dependabot checks for updates monthly.

## Credits and license

MishManners' gaming room inspired the studio cover. BrunnerLivio's retro navigation inspired the linked cartridges. ImageGen produced the cover for Jason, and the three cartridge drawings are maintained as SVG source. [MishManners](https://github.com/mishmanners/MishManners) · [BrunnerLivio](https://github.com/BrunnerLivio/brunnerlivio)

The repository retains its original copyright notice and license. [MIT license](./LICENSE)
