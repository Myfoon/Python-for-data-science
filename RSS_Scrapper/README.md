Task Description
For this task, you can join with an RSS reader using Python 3.10.
For the testing, you are going to isolate the parts you will work on. Namely, you are going to work only on the RSS (XML) scrapping part. Your task is to parse the RSS document and provide two formatted outputs: JSON and the standard output.
You are going to:

Command line parsing.
Receive the XML document from the web.

Because you can create your own style of formatting, it will be difficult to test you. So, we will provide you with the exact style for the format to ease the testing part.
The format of the RSS feed that you are going to parse is RSS 2.0. You can follow the link to get a full understanding of the specification. But in this task, we are asking for the following requirements:

<channel>...</channel> <!-- Required tags are <title>, <link>, <description>  but we are asking you to be able to parse <title>, <link>, <description>, <category>, <language>, <lastBuildDate>, <managingEditor>, <pubDate>, <item> -->
<item>...</item> <!-- All of the fields here are optional, but each item should have at least <title> or <description>, but for the purposes of the test we are asking to be able to parse <title>, <author>, <pubDate>, <link>, <category>, <description> -->


The order of the RSS items in all the output types should be the following:

For <channel> element:

<title>
<link>
<lastBuildDate>
<pubDate>
<language>

<category> for category in categories

<managinEditor>
<description>

<item> for item in items



For <item> element:

<title>
<author>
<pubDate>
<link>
<category>
<description>



The CLI is going to have the following interface. You can use it for testing purposes when you develop XML document parsing.

usage: rss_reader.py [-h] [--json] [--limit LIMIT]
                    source

Pure Python command-line RSS reader.

positional arguments:
 source         RSS URL

optional arguments:
 -h, --help     show this help message and exit
 --json         Print result as JSON in stdout
 --limit LIMIT  Limit news topics if this parameter is provided



Command Line Arguments

If the limit is not specified, then the user should get all available feeds.
If the limit is larger than the feed size, then the user should get all available news.
The limit argument should also affect JSON generation
In the case of using the --json argument, your utility should convert the news into the JSON format.


Console Output:

For <channel> element:


<title> is equal to Feed

<link> is equal to Link

<lastBuildDate> is equal to Last Build Date

<pubDate> is equal to Publish Date

<language> is equal to Language

<category> for category in categories is equal to Categories: category1, category2

<managinEditor> is equal to Editor

<description> is equal to Description

<item> for item in items each item is separated by a custom separator, and all items within except for the description are stuck together.


For <item> element:


<title> is equal to Title

<author> is equal to Author

<pubDate> is equal to Published

<link> is equal to Link

<category> is equal to Categories: category1, category2

<description> is on a separate line without any name.



For the console output you are looking for the order of things – channel items go first and then the other items. You should also have a space between the channel elements and items. Also, the description within the item should be on the new line, separated by space. For example:

Feed: Yahoo News - Latest News & Headlines
Link: https://news.yahoo.com/rss
Description: Yahoo news description

Title: Nestor heads into Georgia after tornados damage Florida
Published: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its march across a swath of the U.S. Southeast... <--- !!! THIS IS DESCRIPTION !!!

Title: Some Other Title
Published: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://some.other.link/some-other-news


Some other new cool information. <--- !!! THIS IS DESCRIPTION



JSON Output:
For the JSON output, you are looking for the exact names of the tags. Ask for the pretty output:

{
  "title": "Yahoo News - Latest News & Headlines",
  "link": "https://news.yahoo.com/rss",
  "description": "Yahoo news description",
  "items": [
    {
      "title": "Nestor heads into Georgia after tornados damage Florida",
      "pubDate": "Sun, 20 Oct 2019 04:21:44 +0300",
      "link": "https://some.other.link/some-other-news",
      "description": "Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its march across a swath of the U.S. Southeast..."
    },
    {
      "title": "Some other title",
      "pubDate": "Sun, 20 Oct 2019 04:21:44 +0300",
      "link": "https://some.other.link/some-other-news",
      "description": "Some other new cool information."
    }
  ]
}


You should have an indent to be equal to two spaces.


Ensure that your app has no encoding issues (meaning symbols like &#39, etc.) when printing news to stdout.
Ensure that your app has no encoding issues (meaning symbols like &#39, etc.) when printing news to stdout in JSON format.
The limit argument should also affect JSON generation.
*It is preferable to have different custom exceptions for different situations (if needed).
