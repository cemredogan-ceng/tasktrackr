from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.task import Task
from db import db

task_bp = Blueprint("task", __name__)

@task_bp.route("/", methods=["POST"])
@jwt_required()
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")
    completed = data.get("completed", False)
    user_id = get_jwt_identity()

    # Eğer title string değilse, hata fırlat
    if not isinstance(title, str):
        return jsonify({"msg": "Title must be a string"}), 422

    task = Task(title=title, description=description, completed=completed, user_id=user_id)
    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created", "task_id": task.id}), 201

