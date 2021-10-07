from webpet.conf import Configuration
from .base_response import BaseResponse
from jinja2 import Template
import aiofiles


class HTMLTemplateResponse(BaseResponse):
    def __init__(self, context: dict, template_name: str, status_code=200):
        """Render response by jinja2 template

        Args:
            context (dict): context for template
            template_name (str): template that need to be rendered
            status_code (int, optional): Return StatusCode. Defaults to 200.
        """
        self.template_name = template_name
        super(HTMLTemplateResponse, self).__init__(context, 'text/html', status_code)

    async def get_body(self):
        conf = Configuration()
        async with aiofiles.open(conf.templates_dir + self.template_name, mode='r') as f:
            contents = await f.read()

        template = Template(contents)
        return template.render(self.body).encode('utf-8')