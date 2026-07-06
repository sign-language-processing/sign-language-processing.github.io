const date = new Date().toISOString().substring(0, 19) + "+00:00";

console.log(`
<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

<url>
  <loc>https://rylo.com/sign/research/</loc>
  <lastmod>${date}</lastmod>
</url>

<url>
  <loc>https://rylo.com/sign/research/signmaker</loc>
  <lastmod>${date}</lastmod>
</url>

<url>
  <loc>https://rylo.com/sign/research/lessons-in-signwriting</loc>
  <lastmod>${date}</lastmod>
</url>


</urlset>`)
