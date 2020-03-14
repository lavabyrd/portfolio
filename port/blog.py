from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from port.auth import login_required
from port.db import get_db

bp = Blueprint('blog', name)