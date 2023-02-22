"""
https://docs.scrapy.org/en/latest/topics/selectors.html
"""

from scrapy.selector import Selector
import json

html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
      <title>Saul&#39;s Deli menu - Berkeley CA 94709 - (510) 848-3354</title>
      <script type="application/ld+json">
        {
          "@context": "http://schema.org",
          "@type": "Restaurant",
        }
      </script>
    </head>
    <body>
    </body>
    </html>
    """

result = Selector(text=html).xpath('//script/text()').get()
result = result.strip().replace("\n", "").replace(" ", "").replace(",}", "}")
# print(result)
# import ipdb
# ipdb.set_trace()
result = json.loads(result)
print(result)


f = open("allmenus_sauls.html", "r")
sauls_html_page = f.read()
result = Selector(text=sauls_html_page).xpath('//script/text()').get()
# result = result.strip().replace("\n", "").replace(" ", "").replace(",}", "}")
result = result.strip().lstrip().replace("\n", "").replace(",}", "}")
result = json.loads(result)
print(result)
# print(result)
import ipdb
ipdb.set_trace()
