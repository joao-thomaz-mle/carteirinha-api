import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)


def load_query_from_file(file_path: str) -> str:
    """
    Load SQL query from a text file

    Args:
        file_path: Path to the query file

    Returns:
        Query string
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        if '"""' in content:
            start = content.find('"""') + 3
            end = content.rfind('"""')
            query = content[start:end].strip()
        else:
            query = content.strip()

        return query

    except Exception as e:
        logger.error(f"❌ Error loading query from file: {e}")
        return None


def execute_query_to_df(
    db_service, query: str, fetch_limit: int = None
) -> pd.DataFrame:
    """
    Executes a query using the provided database service (OracleService or MariaDBService)
    and returns the results as a pandas DataFrame.

    Args:
        db_service: An instance of OracleService or MariaDBService (already connected).
        query (str): The SQL query to execute.
        fetch_limit (int, optional): Maximum number of rows to fetch.

    Returns:
        pd.DataFrame: DataFrame with query results, or empty DataFrame if no results.
    """
    results = db_service.execute_query(query, fetch_limit=fetch_limit)
    if results:
        return pd.DataFrame(results)
    return pd.DataFrame()
