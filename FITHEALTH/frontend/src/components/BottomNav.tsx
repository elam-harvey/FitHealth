import { Home, Dumbbell, Utensils, Users, User, BarChart2 } from 'lucide-react';
import { Tab } from '../types';

interface BottomNavProps {
  currentTab: Tab;
  setCurrentTab: (tab: Tab) => void;
}

export function BottomNav({ currentTab, setCurrentTab }: BottomNavProps) {
  const navItems: { id: Tab; label: string; icon: React.FC<any> }[] = [
    { id: 'home', label: 'Home', icon: Home },
    { id: 'workout', label: 'Workout', icon: Dumbbell },
    { id: 'meals', label: 'Meals', icon: Utensils },
    { id: 'stats', label: 'Stats', icon: BarChart2 },
    { id: 'community', label: 'Community', icon: Users },
    { id: 'profile', label: 'Profile', icon: User },
  ];

  return (
    <div className="fixed bottom-0 left-1/2 -translate-x-1/2 w-full max-w-md bg-dark-card border-t border-dark-border px-2 py-3 flex justify-between items-center z-50 sm:border-x sm:border-dark-border">
      {navItems.map((item) => {
        const Icon = item.icon;
        const isActive = currentTab === item.id;
        return (
          <button
            key={item.id}
            onClick={() => setCurrentTab(item.id)}
            className={`flex flex-col items-center flex-1 space-y-1 transition-colors ${
              isActive ? 'text-neon' : 'text-gray-500 hover:text-gray-300'
            }`}
          >
            <Icon size={24} strokeWidth={isActive ? 2.5 : 2} />
            <span className="text-[10px] font-medium">{item.label}</span>
          </button>
        );
      })}
    </div>
  );
}
