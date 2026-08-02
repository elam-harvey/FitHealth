import { TopBar } from '../components/TopBar';


export function HomeScreen() {

  return (
    <div className="min-h-screen bg-dark-bg pb-24">
      <div className="px-4 py-4 flex justify-between items-center sticky top-0 bg-dark-bg z-40">
        <h1 className="text-2xl font-bold tracking-widest text-white">FITHEALTH</h1>
        <div className="px-3 py-1 border border-neon text-neon text-xs font-bold rounded-full">PRO+</div>
      </div>

      <div className="px-4 space-y-8">
        {/* Motivation Card */}
        <div className="bg-dark-card rounded-2xl p-5 border border-dark-border">
          <h3 className="text-neon text-xs font-bold tracking-widest uppercase mb-3">Motivation</h3>
          <p className="text-white text-xl font-bold leading-tight mb-6">
            "Push harder than yesterday if you want a different tomorrow."
          </p>
          <div className="flex items-center space-x-3">
            <div className="flex-1 h-1.5 bg-gray-800 rounded-full overflow-hidden">
              <div className="h-full bg-neon w-[75%] rounded-full"></div>
            </div>
            <span className="text-gray-400 text-xs font-medium">75% Daily Goal</span>
          </div>
        </div>

        {/* Workout Plan */}
        <div>
          <div className="flex justify-between items-end mb-4">
            <h2 className="text-xl font-bold">Workout Plan</h2>
            <button className="text-neon text-sm font-medium">See all</button>
          </div>
          <div className="flex space-x-4 overflow-x-auto pb-4 -mx-4 px-4 snap-x">
            {/* Card 1 */}
            <div className="min-w-[200px] snap-center rounded-2xl bg-dark-card overflow-hidden border border-dark-border">
              <div className="h-32 bg-gray-800 relative">
                <img src="https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=400&q=80" className="w-full h-full object-cover opacity-80" alt="Upper Body" />
                <div className="absolute bottom-2 left-2 px-2 py-1 bg-black/60 backdrop-blur-md rounded-md text-xs font-bold text-white">
                  15 Min
                </div>
              </div>
              <div className="p-4">
                <h3 className="font-bold text-lg mb-1">Upper Body</h3>
                <p className="text-gray-400 text-sm">Strength • 4 sets</p>
              </div>
            </div>
            {/* Card 2 */}
            <div className="min-w-[200px] snap-center rounded-2xl bg-dark-card overflow-hidden border border-dark-border">
              <div className="h-32 bg-gray-800 relative">
                <img src="https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?auto=format&fit=crop&w=400&q=80" className="w-full h-full object-cover opacity-80" alt="Core Crunch" />
                <div className="absolute bottom-2 left-2 px-2 py-1 bg-black/60 backdrop-blur-md rounded-md text-xs font-bold text-white">
                  10 Min
                </div>
              </div>
              <div className="p-4">
                <h3 className="font-bold text-lg mb-1">Core Crunch</h3>
                <p className="text-gray-400 text-sm">Abs • 3 sets</p>
              </div>
            </div>
          </div>
        </div>

        {/* Meal Plan */}
        <div>
          <h2 className="text-xl font-bold mb-4">Meal Plan</h2>
          <div className="bg-dark-card rounded-2xl p-4 border border-dark-border grid grid-cols-2 gap-4">
            <div className="flex items-start space-x-3">
              <div className="w-10 h-10 rounded-xl bg-gray-800 flex flex-shrink-0 items-center justify-center text-neon">
                ☕
              </div>
              <div>
                <p className="font-medium text-sm">Morning Meal 1</p>
                <p className="text-gray-400 text-xs">Oats & Berries</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-10 h-10 rounded-xl bg-gray-800 flex flex-shrink-0 items-center justify-center text-neon">
                🥗
              </div>
              <div>
                <p className="font-medium text-sm">Afternoon Meal 2</p>
                <p className="text-gray-400 text-xs">Chicken Salad</p>
              </div>
            </div>
            <div className="flex items-start space-x-3 col-span-2 mt-2 pt-4 border-t border-dark-border border-dashed">
              <div className="w-10 h-10 rounded-xl bg-gray-800 flex flex-shrink-0 items-center justify-center text-neon">
                🐟
              </div>
              <div>
                <p className="font-medium text-sm">Evening Meal 3</p>
                <p className="text-gray-400 text-xs">Salmon & Quinoa</p>
              </div>
            </div>
          </div>
        </div>

        {/* Challenges */}
        <div>
          <h2 className="text-xl font-bold mb-4">Challenges</h2>
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-dark-card rounded-2xl p-5 border border-dark-border flex flex-col items-center">
              <div className="w-12 h-12 rounded-full bg-orange-500/20 text-orange-500 flex items-center justify-center mb-3">
                🔥
              </div>
              <h3 className="font-bold mb-1 text-center">7-Day Burn</h3>
              <p className="text-xs text-gray-400">Day 3 of 7</p>
            </div>
            <div className="bg-dark-card rounded-2xl p-5 border border-dark-border flex flex-col items-center">
              <div className="w-12 h-12 rounded-full bg-blue-500/20 text-blue-500 flex items-center justify-center mb-3">
                💧
              </div>
              <h3 className="font-bold mb-1 text-center">Hydration</h3>
              <p className="text-xs text-gray-400">2L / 3L Daily</p>
            </div>
          </div>
        </div>

        {/* Random Exercises */}
        <div>
          <h2 className="text-xl font-bold mb-4">Random Exercises</h2>
          <div className="flex space-x-3 overflow-x-auto pb-2 -mx-4 px-4">
            <div className="px-4 py-2 rounded-xl border border-dark-border whitespace-nowrap text-sm font-medium">
              1. Jumping Jacks
            </div>
            <div className="px-4 py-2 rounded-xl border border-dark-border whitespace-nowrap text-sm font-medium">
              2. Squats
            </div>
            <div className="px-4 py-2 rounded-xl border border-dark-border whitespace-nowrap text-sm font-medium">
              3. Push-ups
            </div>
          </div>
        </div>

        {/* Snacks */}
        <div>
          <h2 className="text-xl font-bold mb-4">Snacks</h2>
          <div className="bg-dark-card rounded-2xl p-4 border border-dark-border flex justify-between items-center">
            <div className="flex items-center space-x-4">
              <div className="w-12 h-12 rounded-xl bg-gray-800 flex items-center justify-center text-xl">
                🍏
              </div>
              <div>
                <h3 className="font-bold">Healthy Snacks</h3>
                <p className="text-sm text-gray-400">Almonds & Apple</p>
              </div>
            </div>
            <button className="w-8 h-8 rounded-full bg-gray-800 flex items-center justify-center text-gray-400">
              <span className="text-xl mb-0.5">+</span>
            </button>
          </div>
        </div>

      </div>
    </div>
  );
}
