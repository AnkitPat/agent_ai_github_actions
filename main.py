from fastapi import FastAPI
from langserve import add_routes
from agent import agent

app =  FastAPI()
add_routes(app, agent, path="/agent")
