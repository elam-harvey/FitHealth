import { Bell, UserCircle2 } from 'lucide-react';

export function TopBar({ title, showAvatar = false }: { title: string, showAvatar?: boolean }) {
  return (
    <div className="flex justify-between items-center px-4 py-4 sticky top-0 bg-dark-bg z-40">
      <div className="flex items-center space-x-3">
        {showAvatar && (
          <div className="w-10 h-10 rounded-full bg-gray-700 overflow-hidden border border-gray-600">
            <img src="https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?auto=format&fit=crop&w=150&q=80" alt="Avatar" className="w-full h-full object-cover" />
          </div>
        )}
        <h1 className="text-2xl font-bold flex items-center">
          {title.includes('FITHEALTH') || title.includes('FitHealth') ? (
            <span className="text-neon">{title}</span>
          ) : (
            <span className={title === 'Workouts' || title === 'Meal Plans' ? 'text-neon' : 'text-white'}>{title}</span>
          )}
        </h1>
      </div>
      <div>
        <button className="relative p-2 text-neon">
          <Bell size={24} />
          <div className="absolute top-2 right-2 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-dark-bg"></div>
        </button>
      </div>
    </div>
  );
}
