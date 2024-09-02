from litestar import Litestar, get, MediaType

from src.static import startup_image


@get("/", media_type=MediaType.HTML)
async def project_starting_page() -> str:
    return startup_image

app = Litestar(route_handlers=[project_starting_page])

