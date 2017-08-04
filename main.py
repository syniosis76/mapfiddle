from server import api
import about
import static
import mapservice
from waitress import serve

serve(api, listen='*:8000')