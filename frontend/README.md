# FitHealth Frontend

Welcome to the **FitHealth** frontend repository! This is a modern, mobile-first React application designed to provide users with a comprehensive fitness and health tracking experience.

## Tech Stack

- **Framework**: [React 19](https://react.dev/)
- **Build Tool**: [Vite](https://vitejs.dev/)
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **Icons**: [Lucide React](https://lucide.dev/)
- **Animations**: [Framer Motion](https://motion.dev/)

## Project Structure

The codebase is organized to be simple, modular, and easy to maintain. The entry point of the app is `src/main.tsx`, which renders the main `App` component.

```text
frontend/
├── src/
│   ├── components/      # Reusable UI components
│   │   ├── BottomNav.tsx
│   │   └── TopBar.tsx
│   ├── screens/         # Main views/pages of the application
│   │   ├── CommunityScreen.tsx
│   │   ├── HomeScreen.tsx
│   │   ├── LoginScreen.tsx
│   │   ├── MealsScreen.tsx
│   │   ├── ProfileScreen.tsx
│   │   ├── StatsScreen.tsx
│   │   └── WorkoutsScreen.tsx
│   ├── App.tsx          # Main application logic and routing state
│   ├── index.css        # Global styles and Tailwind configuration
│   ├── main.tsx         # React DOM rendering entry point
│   └── types.ts         # Global TypeScript definitions
├── index.html           # HTML entry point
├── package.json         # Project dependencies and scripts
├── tailwind.config.js   # Tailwind configuration
├── tsconfig.json        # TypeScript configuration
└── vite.config.ts       # Vite configuration
```

## Architecture & Navigation

Currently, the app utilizes a simple state-based routing mechanism managed in `App.tsx`. 

- **Authentication**: The app starts at the `LoginScreen`. Once authenticated, the user is given access to the rest of the application.
- **Navigation**: The `BottomNav` component allows users to switch between the main tabs (`home`, `workout`, `meals`, `stats`, `community`, `profile`). The selected tab state determines which screen component is rendered.

## Getting Started

### Prerequisites

Ensure you have [Node.js](https://nodejs.org/) (version 18+ recommended) installed on your machine.

### Installation

1. Install the project dependencies:

   ```bash
   npm install
   ```

2. (Optional) Set up your environment variables. You can copy the example file:
   
   ```bash
   cp .env.example .env
   ```

### Running the App Locally

To start the local development server:

```bash
npm run dev
```

The application will be available at `http://localhost:3000` (or another port if 3000 is in use).

### Building for Production

To create a production-ready build:

```bash
npm run build
```

The optimized static files will be generated in the `dist` directory. You can preview the production build locally using:

```bash
npm run preview
```

### Linting

To run the TypeScript compiler to check for type and syntax errors:

```bash
npm run lint
```

## Development Guidelines

- **Mobile First**: The UI is optimized for a mobile form factor (`max-w-md mx-auto` container layout). Make sure to test your components at mobile viewport sizes.
- **Styling**: We use Tailwind CSS for styling. Avoid writing custom CSS in `index.css` unless necessary (e.g., custom animations or global resets). Use utility classes whenever possible.
- **Components**: Keep components modular. If a piece of UI is used in more than one screen, it belongs in `src/components/`.
