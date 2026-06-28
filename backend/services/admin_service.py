from sqlalchemy.orm import Session

from backend.models import (
    User,
    LoginLog,
    WeatherHistory,
    AQIHistory,
    Prediction
)

# ==========================================
# Get All Users
# ==========================================

def get_all_users(db: Session, limit: int = 100):
    return (
        db.query(User)
        .order_by(User.id.desc())
        .limit(limit)
        .all()
    )


# ==========================================
# Get User By ID
# ==========================================

def get_user_by_id(user_id: int, db: Session):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


# ==========================================
# Delete User
# ==========================================

def delete_user(user_id: int, db: Session):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        return {
            "error": "User not found"
        }

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }


# ==========================================
# Get Login Logs
# ==========================================

def get_login_logs(db: Session, limit: int = 100):
    return (
        db.query(LoginLog)
        .order_by(LoginLog.login_time.desc())
        .limit(limit)
        .all()
    )


# ==========================================
# Total Users
# ==========================================

def get_total_users(db: Session):
    return db.query(User).count()


# ==========================================
# Total Weather Searches
# ==========================================

def get_total_weather_searches(db: Session):
    return db.query(WeatherHistory).count()


# ==========================================
# Total AQI Searches
# ==========================================

def get_total_aqi_searches(db: Session):
    return db.query(AQIHistory).count()


# ==========================================
# Total Predictions
# ==========================================

def get_total_predictions(db: Session):
    return db.query(Prediction).count()


# ==========================================
# Admin Dashboard
# ==========================================

def get_admin_dashboard(db: Session):
    return {
        "total_users": get_total_users(db),
        "weather_searches": get_total_weather_searches(db),
        "aqi_searches": get_total_aqi_searches(db),
        "predictions": get_total_predictions(db)
    }