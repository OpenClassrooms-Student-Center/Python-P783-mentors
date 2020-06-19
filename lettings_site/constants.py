import os


SENTRY_DSN = None
if os.environ.get('LETTINGS_SITE_SENTRY_AUTH') and os.environ.get(
        'LETTINGS_SITE_SENTRY_PROJECT_ID'):
    SENTRY_DSN = (f'https://{os.environ["LETTINGS_SITE_SENTRY_AUTH"]}@o138582.ingest.sentry.io/'
                  f'{os.environ["LETTINGS_SITE_SENTRY_PROJECT_ID"]}')
