import os
os.makedirs('/var/folders/7f/0zdrkb3934bd1ct8s2yqkwjr0000gn/T/opencode/pdfs', exist_ok=True)
def create_html(path, content):
    with open(path, 'w') as f:
        f.write(content)

create_html('/var/folders/7f/0zdrkb3934bd1ct8s2yqkwjr0000gn/T/opencode/pdfs/grovyl-brand-identity.html', '<html><body>Brand Identity Content</body></html>')
create_html('/var/folders/7f/0zdrkb3934bd1ct8s2yqkwjr0000gn/T/opencode/pdfs/resend-email-delivery-setup.html', '<html><body>Resend Email Setup Guide Content</body></html>')
