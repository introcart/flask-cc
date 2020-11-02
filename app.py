"""Flask app for dessert demo."""

from flask import Flask, request, jsonify
from models import db, connect_db, Dessert