from django.conf import settings

FRESHLY_ASSETS_ALWAYS_FRESH = getattr(settings, 'FRESHLY_ASSETS_ALWAYS_FRESH', False)

# Version control our assets, so we can tell the client when to reload our assets
FRESHLY_ASSETS_VERSION = getattr(settings, 'FRESHLY_ASSETS_VERSION', '001')

# media extensions we care about - user configurable
FRESHLY_DEFAULT_ASSETS_EXTENTIONS = [
    'jpg','jpeg','gif','css','png','js','ico',
    'pdf','doc','docx','ppt','pptx','txt','mov',
    'mp4','mpeg','mp3','swf',
]

# extensions in FRESHLY_ASSETS_EXTENTIONS will automatically get a verion number if they appear in a link
FRESHLY_ASSETS_EXTENTIONS = getattr(settings, 'FRESHLY_ASSETS_EXTENTIONS', FRESHLY_DEFAULT_ASSETS_EXTENTIONS)

# extensions in FRESHLY_ASSETS_EXTENTIONS_EXTRA will be appended to FRESHLY_ASSETS_EXTENTIONS
FRESHLY_ASSETS_EXTENTIONS_EXTRA = getattr(settings, 'FRESHLY_ASSETS_EXTENTIONS_EXTRA', [])



