from crewai import Crew

from tasks.analyse_task import get_stock_analysis
from tasks.trade_task import trade_decision
from agents.analyst_agent import analyst_agent
from agents.trader_agent import trader_agent

stock_crew = Crew(
    agents=[analyst_agent, trader_agent],
    tasks=[get_stock_analysis, trade_decision],
    verbose=True
)