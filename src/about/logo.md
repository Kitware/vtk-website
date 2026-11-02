# VTK Logo

Official VTK logos for use in presentations, publications, and websites.

<div class="logo-preview">
  <figure class="light">
    <img src="/logos/VTK-logo-medium-res.png" alt="VTK logo on a light background" />
    <figcaption>On light</figcaption>
  </figure>
  <figure class="dark">
    <img src="/logos/VTK-logo-medium-res.png" alt="VTK logo on a dark background" />
    <figcaption>On dark</figcaption>
  </figure>
</div>

## Usage Guidelines

- Use the official logos without modification
- Maintain the aspect ratio when resizing
- Ensure adequate spacing around the logo
- Do not alter the colors or proportions

## Download

The PNG files have a transparent background and work on any color. The JPEG files have a white background.

<table class="logo-downloads">
  <thead>
    <tr><th>Size</th><th>Dimensions</th><th>PNG (transparent)</th><th>JPEG (white)</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>High</td><td>1200 × 644</td>
      <td><a href="/logos/VTK-logo-high-res.png" download>Download</a></td>
      <td><a href="/logos/VTK-logo-high-res.jpg" download>Download</a></td>
    </tr>
    <tr>
      <td>Medium</td><td>763 × 409</td>
      <td><a href="/logos/VTK-logo-medium-res.png" download>Download</a></td>
      <td><a href="/logos/VTK-logo-medium-res.jpg" download>Download</a></td>
    </tr>
    <tr>
      <td>Low</td><td>300 × 161</td>
      <td><a href="/logos/VTK-logo-low-res.png" download>Download</a></td>
      <td><a href="/logos/VTK-logo-low-res.jpg" download>Download</a></td>
    </tr>
    <tr>
      <td>Tiny</td><td>91 × 49</td>
      <td><a href="/logos/VTK-logo-tiny-res.png" download>Download</a></td>
      <td><a href="/logos/VTK-logo-tiny-res.jpg" download>Download</a></td>
    </tr>
  </tbody>
</table>

<style>
.logo-preview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  margin: 24px 0;
}

.logo-preview figure {
  margin: 0;
  padding: 32px 32px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  text-align: center;
}

.logo-preview figure.light { background: #ffffff; }
.logo-preview figure.dark { background: #1b1b1f; }

.logo-preview img {
  margin: 0 auto;
  width: 100%;
  max-width: 280px;
}

.logo-preview figcaption {
  margin-top: 16px;
  font-size: 13px;
  color: #8a8a8f;
}

.logo-downloads td:nth-child(n + 3) {
  white-space: nowrap;
}
</style>
