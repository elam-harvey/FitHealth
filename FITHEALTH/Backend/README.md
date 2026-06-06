# FITHEALTH: Diet and Fitness All-in-One System

A comprehensive mobile-first and web-based health and fitness platform designed to help users improve their physical health through personalized workout plans, meal recommendations, progress tracking, and AI-assisted health guidance.

## Project Overview

FITHEALTH is designed for beginners, students, individuals seeking weight loss, and users interested in maintaining healthy lifestyles. The platform integrates fitness management, diet planning, progress analytics, community engagement, and AI-based recommendations into a unified ecosystem.

The system supports both web and mobile platforms using a shared RESTful API architecture.

## Problem Statement

Many individuals struggle to maintain healthy lifestyles due to lack of personalized fitness guidance, poor dietary planning, limited access to affordable health coaching, and absence of localized health systems that support local foods and lifestyle conditions.

Most existing health and fitness applications are either too expensive, too complex, lack localization, or fail to provide integrated diet and workout management. FITHEALTH aims to solve these problems by providing a localized, affordable, intelligent, and user-friendly health and fitness platform.

## Key Features

### Authentication & User Management
- User registration and login
- Google Sign-In integration
- OTP verification for security
- JWT-based authentication
- User profile management with health data
- Goal setting and preferences

### Workout Management
- Comprehensive exercise library
- Workout plans by categories and difficulty levels
- Exercise demonstrations and instructions
- Workout streak tracking
- Personalized workout recommendations
- Progress tracking and completion logging

### Diet & Meal Planning
- Personalized meal recommendations
- Local meal support for regional preferences
- Calorie tracking and monitoring
- Water intake tracking
- Grocery list generation
- Meal customization and replacement options

### AI-Powered Features
- Rule-based workout recommendations
- Intelligent meal planning
- Adaptive plan adjustments based on progress
- AI chatbot coach for guidance
- Personalized recommendations based on user data

### Community & Social Features
- Community posts and interactions
- Comments and likes system
- Friend connections and challenges
- Private messaging system
- Social motivation and support

### Progress Analytics
- BMI tracking and history
- Weight tracking with visualizations
- Daily, weekly, and monthly analytics
- Progress reports and trend analysis
- Downloadable PDF reports

### Premium Subscription System
- Monthly and yearly subscription plans
- Enhanced AI recommendations
- International meal plans
- Advanced analytics and insights
- Unlimited customization options

### Notification System
- Workout and meal reminders
- Hydration tracking notifications
- Achievement badges and milestones
- Customizable notification preferences

### Admin Panel
- User management and moderation
- Exercise and content management
- Community post moderation
- Subscription management
- System analytics and reporting

## Technology Stack

### Backend
- **Framework**: Django 5.2.1 with Django REST Framework 3.16.0
- **Database**: PostgreSQL (development: SQLite)
- **Authentication**: JWT, OAuth2 (Google), OTP
- **Real-time**: Django Channels with Redis
- **Task Queue**: Celery with Redis
- **Media Storage**: Cloudinary
- **Payments**: Stripe integration
- **Documentation**: drf-yasg (Swagger/OpenAPI)

### Data Science & AI
- **Libraries**: NumPy, Pandas, Scikit-learn
- **AI Engine**: Rule-based recommendation system

### Development & Testing
- **Code Quality**: Black (formatting), Flake8 (linting)
- **Testing**: pytest, pytest-django
- **Extensions**: Django Extensions

### Deployment
- **WSGI Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Caching**: Redis

## API Architecture

The system provides a comprehensive RESTful API with the following main endpoints:

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/google/` - Google OAuth
- `POST /api/auth/verify-otp/` - OTP verification

### Workouts
- `GET /api/workouts/` - Exercise library
- `GET /api/workouts/plans/` - Workout plans
- `POST /api/workouts/track/` - Track workout completion

### Meals & Nutrition
- `GET /api/meals/plans/` - Get meal plans
- `POST /api/meals/plans/generate/` - Generate meal plans
- `POST /api/meals/track-calories/` - Track calories
- `POST /api/meals/track-water/` - Track hydration

### AI Recommendations
- `POST /api/ai/recommend-workout/` - Workout recommendations
- `POST /api/ai/recommend-meal/` - Meal recommendations
- `POST /api/ai/chatbot/` - AI chatbot interaction

### Community
- `GET /api/community/posts/` - Community posts
- `POST /api/community/posts/create/` - Create posts
- `POST /api/community/friends/add/` - Add friends

### Progress Tracking
- `POST /api/progress/track/` - Record progress
- `GET /api/progress/analytics/` - View analytics
- `GET /api/progress/weight-history/` - Weight history

### Subscriptions
- `GET /api/subscriptions/plans/` - Subscription plans
- `POST /api/subscriptions/subscribe/` - Subscribe to premium

## System Architecture

### Development Environment
- Local media storage
- SQLite database
- Local Redis instance

### Production Environment
- PostgreSQL database
- Redis for caching and channels
- Cloudinary for media storage
- Docker containerization (planned)

### Security Features
- JWT authentication with refresh tokens
- Password hashing and encryption
- HTTPS communication
- Role-based authorization
- Input validation and sanitization
- SQL injection protection
- XSS prevention

## Target Users

### Primary Users
- **Beginners**: New to fitness and need guidance
- **Students**: Young adults seeking healthy lifestyles
- **Weight Loss Users**: Individuals focused on weight management
- **General Fitness Users**: Those maintaining healthy routines

### User Roles
- **Normal Users**: Access to workouts, meals, tracking, community
- **Premium Users**: Enhanced features, AI recommendations, advanced analytics
- **Administrators**: System management, content moderation, analytics

## Development Methodology

The project follows a **Hybrid Software Development Methodology** combining:
- Agile Scrum practices for iterative development
- Structured documentation for academic and maintenance purposes

## Prerequisites

- Python 3.8+
- PostgreSQL (production)
- Redis server
- Node.js (for frontend development)
- Flutter SDK (for mobile development)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FitHealthSys
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**
   Create `.env` file:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgresql://user:pass@localhost:5432/fithealth
   REDIS_URL=redis://localhost:6379
   STRIPE_SECRET_KEY=sk_test_...
   CLOUDINARY_URL=cloudinary://...
   GOOGLE_CLIENT_ID=...
   ```

5. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Load initial data** (if available)
   ```bash
   python manage.py loaddata initial_data.json
   ```

## Running the Application

### Development Server
```bash
python manage.py runserver
```

### With Celery (Background Tasks)
```bash
# Terminal 1: Redis server
redis-server

# Terminal 2: Celery worker
celery -A FitHealth worker -l info

# Terminal 3: Celery beat
celery -A FitHealth beat -l info

# Terminal 4: Django server
python manage.py runserver
```

### With Daphne (WebSockets)
```bash
daphne FitHealth.asgi:application
```

## API Documentation

- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`

## Testing

### Run Tests
```bash
pytest
```

### Test Coverage
```bash
pytest --cov=.
```

### Code Quality
```bash
black .  # Format code
flake8   # Lint code
```

## Deployment

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL database
- [ ] Configure Redis
- [ ] Set up Cloudinary credentials
- [ ] Configure Stripe keys
- [ ] Set up Google OAuth
- [ ] Configure email settings
- [ ] Set up SSL certificates

### Docker Deployment (Planned)
```bash
docker-compose up -d
```

### Manual Deployment
```bash
gunicorn FitHealth.wsgi:application --bind 0.0.0.0:8000
```

## Project Structure

```
FitHealthSys/
├── requirements.txt
├── README.md
├── .env.example
├── docker-compose.yml (planned)
├── FitHealth/
│   ├── manage.py
│   ├── FitHealth/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── middleware.py
│   ├── apps/
│   │   ├── authentication/
│   │   ├── users/
│   │   ├── workouts/
│   │   ├── meals/
│   │   ├── ai/
│   │   ├── community/
│   │   ├── progress/
│   │   ├── subscriptions/
│   │   ├── notifications/
│   │   └── admin/
│   ├── static/
│   ├── media/
│   └── templates/
├── frontend/ (React)
├── mobile/ (Flutter)
└── docs/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write tests for new features
- Update documentation
- Ensure code passes linting
- Use meaningful commit messages

## Testing Strategy

### Unit Testing
- Authentication logic
- Workout generation algorithms
- Meal recommendation engine
- AI rule processing
- BMI and calorie calculations

### Integration Testing
- API endpoint interactions
- Database operations
- Payment processing
- Notification systems

### System Testing
- End-to-end user workflows
- Cross-platform compatibility
- Performance under load

### User Acceptance Testing
- Usability evaluation
- Feature validation
- Mobile responsiveness

## Future Enhancements

- Wearable device integration
- Advanced machine learning models
- Real-time video consultations
- Voice assistant integration
- AI-powered image recognition for food logging
- Smartwatch companion app

## License

[Specify your license here]

## Support

For support and questions:
- Email: [contact email]
- Documentation: [link to docs]
- Issues: [GitHub issues link]

## Acknowledgments

- Django and DRF communities
- Open source contributors
- Fitness and nutrition experts consulted</content>
<parameter name="filePath">/home/elam09harvey/Desktop/FitHealthSys/README.md