from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(msg: str) -> None:
    print(f"❌ {msg}")


def ok(msg: str) -> None:
    print(f"✅ {msg}")


def main() -> int:
    errors: list[str] = []

    student_file = Path("STUDENT.md")
    if not student_file.exists():
        errors.append(
            "Missing `STUDENT.md`.\n"
            "Fix: Create a new file named EXACTLY `STUDENT.md` in the root of the repository, "
            "commit it, and push your branch."
        )
    else:
        ok("Found `STUDENT.md`.")

        text = student_file.read_text(encoding="utf-8", errors="replace")

        # ---- Required headings ----
        if re.search(r"^#\s+Student Information\s*$", text, flags=re.MULTILINE):
            ok("Found heading: `# Student Information`.")
        else:
            errors.append(
                "Missing heading `# Student Information`.\n"
                "Fix: Add `# Student Information` at the top of `STUDENT.md`."
            )

        if re.search(r"^##\s+Reflection\s*$", text, flags=re.MULTILINE):
            ok("Found heading: `## Reflection`.")
        else:
            errors.append(
                "Missing heading `## Reflection`.\n"
                "Fix: Add `## Reflection` below your student information in `STUDENT.md`."
            )

        # ---- Required fields ----
        # We expect list items like:
        # - Name: Scott Hadzik
        # - WSU Email: scott.hadzik@weber.edu
        name_line = re.search(r"^\s*-\s*Name:\s*(.+)\s*$", text, flags=re.MULTILINE)
        email_line = re.search(r"^\s*-\s*WSU Email:\s*(.+)\s*$", text, flags=re.MULTILINE)

        if name_line and name_line.group(1).strip() and name_line.group(1).strip() != "-":
            ok("Name field is filled in.")
        else:
            errors.append(
                "Your `- Name:` line is missing or blank.\n"
                "Fix: In `STUDENT.md`, write your name after `- Name:`"
            )

        if email_line and email_line.group(1).strip() and email_line.group(1).strip() != "-":
            ok("WSU Email field is filled in.")
        else:
            errors.append(
                "Your `- WSU Email:` line is missing or blank.\n"
                "Fix: In `STUDENT.md`, write your WSU email after `- WSU Email:`"
            )

        # ---- Reflection prompts ----
        learned_line = re.search(
            r"^\s*-\s*One thing I learned about Git or GitHub:\s*(.+)\s*$",
            text,
            flags=re.MULTILINE,
        )
        confused_line = re.search(
            r"^\s*-\s*One thing that is still confusing:\s*(.+)\s*$",
            text,
            flags=re.MULTILINE,
        )

        def is_filled(match: re.Match | None) -> bool:
            return bool(match and match.group(1).strip() and match.group(1).strip() != "-")

        if is_filled(learned_line):
            ok("Reflection: 'What I learned' is filled in.")
        else:
            errors.append(
                "Your reflection line `One thing I learned...` is missing or blank.\n"
                "Fix: Write a complete sentence after that prompt in `STUDENT.md`."
            )

        if is_filled(confused_line):
            ok("Reflection: 'What's still confusing' is filled in.")
        else:
            errors.append(
                "Your reflection line `One thing that is still confusing...` is missing or blank.\n"
                "Fix: Write a complete sentence after that prompt in `STUDENT.md`."
            )

    # ---- Optional: branch name check (friendly) ----
    # We read the branch name from environment variables set by GitHub Actions.
    # If it’s missing (running locally), we skip it.
    head_ref = (Path("/tmp/GITHUB_HEAD_REF").read_text().strip()
                if Path("/tmp/GITHUB_HEAD_REF").exists()
                else None)
    if head_ref:
        if re.fullmatch(r"[a-z]+-[a-z]+", head_ref):
            ok(f"Branch name format looks good: `{head_ref}`.")
        else:
            errors.append(
                f"Branch name `{head_ref}` does not match the required format `firstname-lastname`.\n"
                "Fix: Create a new branch named like `jane-doe`, push it, and open a PR from that branch."
            )

    # ---- Summary ----
    print("\n" + "=" * 60)
    if errors:
        print("❌ Submission checks failed. Fix the items below, then commit + push again:\n")
        for i, e in enumerate(errors, start=1):
            print(f"{i}) {e}\n")
        return 1

    print("✅ All checks passed. Your submission meets the required criteria.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
