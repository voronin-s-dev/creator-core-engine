---
name: motion-producer
description: Tri-modal video production pipeline for expert Reels and Shorts. Orchestrates AI B-roll generation (Veo/Google Flow), vector data animation with Emil Kowalski spring physics in Remotion, subtitle burn-in, safe zones, and MP4 rendering.
---

# Motion Producer Skill

Autonomous video production pipeline combining generative video backgrounds, React-based vector graphics, and fluid typography.

## Tri-Modal Video Architecture

```
Layer 1: Generative B-Roll (Veo / Google Flow / Raw Video)
Layer 2: Vector UI / Motion Data (Remotion with Kowalski spring physics)
Layer 3: Subtitles & Safe Margins (Karaoke kinetic text)
```

## Production Guidelines

### 1. Aesthetic Guidelines (Dark Neo-Academic)
* **Background Atmosphere:** 9:16 vertical, moody atmospheric lighting, warm key light, subtle 35mm film grain, 24fps film cadence.
* **Palette:** Deep background (#0C0A0B / #121013), soft white text (#EFEFEF), single brand accent color.

### 2. Spring Physics (Emil Kowalski Standard)
When building Remotion templates:
* Never use linear or abrupt easing curves for UI cards.
* Use damped spring physics:
  ```typescript
  import { spring } from 'remotion';
  const scale = spring({ frame, fps, config: { damping: 12, mass: 0.5, stiffness: 100 } });
  ```

### 3. Safe Margin Verification
Ensure text overlays never overlap interface controls:
* Top clearance: 150px.
* Bottom clearance: 250px.
* Right clearance: 120px.

### 4. Generation & Export Workflow
1. Read target script from `reels-scriptwriter`.
2. Generate or select background B-roll matching script aesthetic.
3. Inject props into Remotion composition.
4. Render MP4 vertical output at 1080×1920 (30fps or 60fps).
