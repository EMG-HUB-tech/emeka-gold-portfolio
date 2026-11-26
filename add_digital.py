from pathlib import Path
p=Path('/mnt/data/emghub_services')
# Add nav link in every main page before Resources link, and footer link before Resources.
for f in p.glob('*.html'):
    s=f.read_text(errors='ignore')
    if 'digital-portfolio.html' not in s:
        s=s.replace('<a data-page="resources" href="resources.html">Resources</a>', '<a data-page="digital-portfolio" href="digital-portfolio.html">Web &amp; Apps</a>\n<a data-page="resources" href="resources.html">Resources</a>')
        s=s.replace('<a href="resources.html">Resources</a>', '<a href="digital-portfolio.html">Web &amp; Apps</a><a href="resources.html">Resources</a>')
    f.write_text(s)
# Add two digital services into existing services page.
s=(p/'services.html').read_text()
marker='<div class="section-head"><div><h2>Client Testimonials</h2>'
block='''<section class="services" id="digital-solutions" style="padding:48px 0;background:linear-gradient(135deg,#f5f8ff,#fff);">
<div class="container">
<div class="section-head"><div><h2>Digital Solutions &amp; Technology</h2><p>Beyond research support, EMGHUB also designs digital products that help organisations serve people and grow online.</p></div></div>
<div class="grid6" style="grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;">
<a class="service" href="digital-portfolio.html#websites" style="text-align:left;padding:22px;min-height:210px;">
<div class="tile-icon c1" style="margin:0 0 14px;width:54px;height:54px;">⌘</div><h3 style="font-size:19px;">Website Design &amp; Development</h3><p style="font-size:14px;line-height:1.6;">Professional, responsive websites for businesses, organisations, consultants, schools and service providers. Explore sample website concepts and layouts.</p><b style="display:inline-block;margin-top:16px;color:#0b63f6;">Explore Website Samples →</b></a>
<a class="service" href="digital-portfolio.html#mobile-apps" style="text-align:left;padding:22px;min-height:210px;">
<div class="tile-icon c5" style="margin:0 0 14px;width:54px;height:54px;">▣</div><h3 style="font-size:19px;">Mobile Application Development</h3><p style="font-size:14px;line-height:1.6;">Mobile app concepts for bookings, learning, commerce and business operations, designed around practical user needs.</p><b style="display:inline-block;margin-top:16px;color:#0b63f6;">Explore Mobile App Samples →</b></a>
</div>
<div style="text-align:center;margin-top:22px;"><a class="btn primary" href="digital-portfolio.html">View Digital Portfolio →</a></div>
</div></section>
'''
if 'Digital Solutions &amp; Technology' not in s:
    s=s.replace(marker,block+marker)
(p/'services.html').write_text(s)
