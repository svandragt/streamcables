# Releasing

This guide explains how to cut a new release of StreamCables.

## Before you start

Make sure `main` is green: check that the `lint` and `test` checks pass on the latest commit.

## Steps

1. Choose a version number using [Semantic Versioning](https://semver.org/): bump the major version for breaking changes, the minor version for new features, and the patch version for fixes only.
2. Update the version number in two places:
   - `version` in `pyproject.toml`
   - `__version__` in `streamcables/__init__.py`
   - the `print("StreamCables ...")` line in `streamcables/streamcables.py`
3. Commit the version bump and push it to `main`.
4. Tag the commit and push the tag:

   ```
   git tag -a vX.Y.Z -m "vX.Y.Z"
   git push origin vX.Y.Z
   ```

5. Create the GitHub release from that tag, with your own release notes (see below):

   ```
   gh release create vX.Y.Z --title "vX.Y.Z" --notes-file <path-to-notes>
   ```

## Writing release notes

Release notes are for people who run StreamCables, not for contributors. Write what changed for them, not how you implemented it.

- Group changes under `## Added`, `## Changed`, `## Fixed`, and `## Removed` headings, and skip any heading with nothing under it.
- Leave out internal changes with no user-visible effect, such as CI setup, linting, refactors, and test coverage.
- Mention dependency or security updates only as a single summary line, not a package-by-package list.
- Follow the [Google Developer Documentation Style Guide](https://developers.google.com/style): second person, present tense, active voice, plain language.
