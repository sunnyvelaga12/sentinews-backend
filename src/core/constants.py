"""
Application constants.

"""

# API
API_PREFIX = "/api"
API_V1_PREFIX = "/api/v1"
API_TITLE = "SentiNews API"

# API Tags
AUTH_TAG = "Authentication"
USER_TAG = "Users"
NEWS_TAG = "News"
MARKET_TAG = "Market"
PORTFOLIO_TAG = "Portfolio"
WATCHLIST_TAG = "Watchlist"
AI_TAG = "AI"
HEALTH_TAG = "Health"

# Pagination
DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Cache
DEFAULT_CACHE_TTL = 300
NEWS_CACHE_TTL = 600
MARKET_CACHE_TTL = 60
AI_CACHE_TTL = 1800

# JWT
TOKEN_TYPE = "Bearer"
ACCESS_TOKEN_NAME = "access_token"
REFRESH_TOKEN_NAME = "refresh_token"

# HTTP
REQUEST_TIMEOUT = 20

# Market
SUPPORTED_EXCHANGES = [
    "NSE",
    "BSE",
    "NASDAQ",
    "NYSE",
]

SUPPORTED_COMMODITIES = [
    "Gold",
    "Silver",
    "Crude Oil",
]

SUPPORTED_INDICES = [
    "NIFTY 50",
    "BANK NIFTY",
    "S&P 500",
    "NASDAQ",
]

# AI
MAX_AI_PROMPT_LENGTH = 5000
MAX_AI_RESPONSE_LENGTH = 8000

# News
DEFAULT_NEWS_LIMIT = 20
MAX_NEWS_LIMIT = 100

# Health
HEALTH_STATUS = "healthy"
SERVICE_NAME = "sentinews-backend"