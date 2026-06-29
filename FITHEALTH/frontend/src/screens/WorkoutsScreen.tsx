import { Search, Flame } from 'lucide-react';
import { TopBar } from '../components/TopBar';

export function WorkoutsScreen() {
  const workouts = [
    {
      title: 'Morning Yoga',
      level: 'Beginner',
      levelColor: 'text-teal-400',
      levelBg: 'bg-teal-400/10',
      time: '20 min',
      kcal: '150 kcal',
      image: 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=200&q=80'
    },
    {
      title: 'Full Body Burn',
      level: 'Intermediate',
      levelColor: 'text-purple-400',
      levelBg: 'bg-purple-400/10',
      time: '35 min',
      kcal: '300 kcal',
      image: 'https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?auto=format&fit=crop&w=200&q=80'
    },
    {
      title: 'HIIT Rush',
      level: 'Advanced',
      levelColor: 'text-red-400',
      levelBg: 'bg-red-400/10',
      time: '25 min',
      kcal: '450 kcal',
      image: 'https://images.unsplash.com/photo-1434596922112-19c563067271?auto=format&fit=crop&w=200&q=80'
    },
    {
      title: 'Dumbbell Basics',
      level: 'Beginner',
      levelColor: 'text-teal-400',
      levelBg: 'bg-teal-400/10',
      time: '30 min',
      kcal: '200 kcal',
      image: '' // Fallback to icon
    }
  ];

  return (
    <div className="min-h-screen bg-dark-bg pb-24">
      <TopBar title="Workouts" showAvatar={true} />
      
      <div className="px-4 mt-2">
        <div className="flex space-x-3 mb-6">
          <div className="flex-1 relative">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
            <input 
              type="text" 
              placeholder="Search workouts..." 
              className="w-full bg-dark-card border border-dark-border rounded-xl py-3.5 pl-12 pr-4 outline-none focus:border-neon transition-colors"
            />
          </div>
          <div className="bg-dark-card border border-dark-border rounded-xl px-4 py-2 flex flex-col justify-center items-center shrink-0">
            <span className="text-neon font-bold text-lg leading-none">7</span>
            <span className="text-xs text-gray-400 font-medium mt-1 flex items-center">
              Day Streak <Flame size={12} className="ml-1" />
            </span>
          </div>
        </div>

        <div className="flex space-x-2 overflow-x-auto pb-4 -mx-4 px-4 no-scrollbar">
          <button className="bg-neon text-black px-6 py-2 rounded-full font-bold text-sm whitespace-nowrap">
            Beginner
          </button>
          <button className="bg-dark-card border border-dark-border text-white px-6 py-2 rounded-full font-bold text-sm whitespace-nowrap">
            Weight Loss
          </button>
          <button className="bg-dark-card border border-dark-border text-white px-6 py-2 rounded-full font-bold text-sm whitespace-nowrap">
            Strength Trainin...
          </button>
        </div>

        <div className="space-y-4">
          {workouts.map((workout, idx) => (
            <div key={idx} className="bg-dark-card border border-dark-border rounded-2xl p-4 flex items-center space-x-4">
              <div className="w-20 h-20 rounded-xl bg-gray-800 overflow-hidden flex-shrink-0 flex items-center justify-center">
                {workout.image ? (
                  <img src={workout.image} alt={workout.title} className="w-full h-full object-cover" />
                ) : (
                  <div className="text-gray-600">
                     <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m6.5 6.5 11 11"/><path d="m21 21-1-1"/><path d="m3 3 1 1"/><path d="m18 22 4-4"/><path d="m2 6 4-4"/><path d="m3 10 7-7"/><path d="m14 21 7-7"/></svg>
                  </div>
                )}
              </div>
              <div className="flex-1">
                <div className="flex justify-between items-start mb-2">
                  <h3 className="font-bold text-lg">{workout.title}</h3>
                  <span className={`px-2.5 py-1 rounded-md text-[10px] font-bold uppercase tracking-wider ${workout.levelBg} ${workout.levelColor}`}>
                    {workout.level}
                  </span>
                </div>
                <div className="flex items-center text-sm text-gray-400 space-x-4">
                  <span className="flex items-center">
                    <span className="mr-1.5 opacity-70">⏱</span>
                    {workout.time}
                  </span>
                  <span className="flex items-center">
                    <span className="mr-1.5 opacity-70">🔥</span>
                    {workout.kcal}
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
