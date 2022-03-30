import json

with open('/Users/juby/documents/comments.json') as f:
    data = json.load(f)

def as_disqus_xml(data):
    xml_head = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:dsq="http://www.disqus.com/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:wp="http://wordpress.org/export/1.0/"
>
  <channel>
    '''
    xml_tail = '''</channel>
</rss>  
    '''
    items = ''
    for i in range(len(data)):
        d = data[i]
        post_url = 'https://jubeny.com' + d['url']
        # sso = f'''
        # <dsq:remote>
        #   <dsq:id>{d['mail'] if 'mail' in d.keys() and d['mail'] != '' else 'abc@xyz.com'}</dsq:id>
        #   <dsq:avatar>{"https://www.gravatar.com/avatar/" + (d['emailHash'] if 'emailHash' in d.keys() else '0')}</dsq:avatar>
        # </dsq:remote>
        # '''
        item = f'''<item>
      <title>{d['url']}</title>
      <link>{post_url}</link>
      <content:encoded><![CDATA[{post_url}]]></content:encoded>
      <dsq:thread_identifier>{d['url']}</dsq:thread_identifier>
      <wp:post_date_gmt>2015-01-01 01:00:00</wp:post_date_gmt>
      <wp:comment_status>open</wp:comment_status>
      <wp:comment>
        <wp:comment_id>{d['objectId']}</wp:comment_id>
        <wp:comment_author>{d['nick']}</wp:comment_author>
        <wp:comment_author_email>{d['mail'] if 'mail' in d.keys() and d['mail'] != '' else 'abc@xyz.com'}</wp:comment_author_email>
        <wp:comment_author_url>{d['link'] if 'link' in d.keys() else 'https://jubeny.com'}</wp:comment_author_url>
        <wp:comment_author_IP>{d['ip'] if 'ip' in d.keys() else '127.0.0.1'}</wp:comment_author_IP>
        <wp:comment_date_gmt>{d['createdAt'][:10] + ' ' + d['createdAt'][11:19]}</wp:comment_date_gmt>
        <wp:comment_content><![CDATA[{d['comment']}]]></wp:comment_content>
        <wp:comment_approved>1</wp:comment_approved>
        <wp:comment_parent>{d['pid'] if 'pid' in d.keys() else 0}</wp:comment_parent>
      </wp:comment>
    </item>
    '''
        items += item
    return xml_head + items + xml_tail


def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()


save_to_file('valine-comments.xml', as_disqus_xml(data))
