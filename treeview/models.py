from django.db import models
from urllib.parse import urljoin


class Page(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
    )

    def __str__(self) -> str:
        return self.name

    @property
    def url(self):
        return self.__get_full_url()

    def __get_full_url(self):
        if self.parent:
            parent_url = self.__format_url(self.parent.__get_full_url())
            return urljoin(
                f"/{parent_url}/", f"{self.__format_url(self.slug)}/"
            )
        elif self.slug:
            return f"/{self.__format_url(self.slug)}/"

        return "/"

    def __format_url(self, url):
        if url.startswith("/"):
            return url[1:]
        return url
