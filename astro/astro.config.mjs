import { defineConfig } from "astro/config";

// El sitio se publica en GitHub Pages con dominio propio. `site` hace
// falta para que el sitemap y las URL canonicas salgan absolutas.
export default defineConfig({
  site: "https://contaes.com",
  trailingSlash: "always",
  build: { format: "directory" },
  devToolbar: { enabled: false },
});
