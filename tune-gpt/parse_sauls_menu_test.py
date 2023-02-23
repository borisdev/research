"""
https://docs.scrapy.org/en/latest/topics/selectors.html
"""
from loguru import logger
from scrapy.selector import Selector
import json
# from pprint import pprint
# import ipdb


html = '''
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
    '''


output = []


logger.add("sauls_menu.log", format="{time} {message}")
with open("allmenus_sauls.html", "r") as f:
    sauls_html_page = f.read()
    result = Selector(text=sauls_html_page).xpath('//script/text()').get()
    result = result.strip().lstrip().replace("\n", "").replace(",}", "}")
    result = json.loads(result)
    for menu in result['hasMenu']:
        menu_name = menu['name']
        # SKIP BREAKFAST FOR NOW
        # if menu_name.lower != "dinner":
        #    continue
        menu_section = menu.get('hasMenuSection', False)
        if not menu_section:
            continue
        for section in menu_section:
            section_description = section['description']
            menu_items = section.get('hasMenuItem', False)
            if not menu_items:
                continue
            for item in menu_items:
                # print("menu name:", menu_name)
                # print("section description:", section_description)
                name = item['name']
                description = item['description']
                name = name.replace("&amp;comma;", ",")
                name = name.replace("&amp;amp;", "&")
                name = name.replace("&#39;", "'")
                description = description.replace("&amp;comma;", ",")
                description = description.replace("&#39;", "'")
                description = description.replace("&amp;amp;", "&")
                # print("name:", name)
                # print("description:", description)
                output.append({"name": name, "description": description})
                # logger.debug(f"{name} {description}")


with open('sauls_menu.json', 'w') as fp:
    json.dump(output, fp)
