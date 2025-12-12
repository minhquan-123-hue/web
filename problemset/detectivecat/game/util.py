import os
from typing import List, Optional
from django.conf import settings

SCENE_DIR = os.path.join(settings.BASE_DIR, "scenes")

print(f"[util] SCENE_DIR = {SCENE_DIR}")  # debug


def list_scenes() -> List[str]:
    print("[util.list_scenes] called")
    assert os.path.exists(SCENE_DIR), "[util.list_scenes] scenes directory missing!"

    _, _, files = next(os.walk(SCENE_DIR))
    print(f"[util.list_scenes] raw files = {files}")

    scenes = sorted([
        f.replace(".md", "")
        for f in files
        if f.endswith(".md")
    ])

    print(f"[util.list_scenes] scenes = {scenes}")
    return scenes


def get_scene(title: str) -> Optional[str]:
    print(f"[util.get_scene] called with title={title!r}")
    assert isinstance(title, str), "[util.get_scene] title must be string"

    path = os.path.join(SCENE_DIR, f"{title}.md")
    print(f"[util.get_scene] checking path: {path}")

    if not os.path.exists(path):
        print("[util.get_scene] file does NOT exist!")
        return None

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"[util.get_scene] content length={len(content)}")
    return content


def save_scene(title: str, content: str) -> None:
    print(f"[util.save_scene] called with title={title!r} content_len={len(content)}")
    assert isinstance(title, str), "[util.save_scene] title must be string"
    assert isinstance(content, str), "[util.save_scene] content must be string"

    path = os.path.join(SCENE_DIR, f"{title}.md")
    print(f"[util.save_scene] saving to {path}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print("[util.save_scene] save complete")
