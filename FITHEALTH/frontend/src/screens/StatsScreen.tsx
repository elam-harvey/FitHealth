import { TopBar } from '../components/TopBar';
import { Activity, Footprints, Clock } from 'lucide-react';

export function StatsScreen() {
  return (
    <div className="min-h-screen bg-dark-bg pb-24">
      <TopBar title="FitHealth" showAvatar={true} />
      
      <div className="px-4 mt-2 space-y-8">
        
        {/* Daily Progress */}
        <div className="bg-dark-card border border-dark-border rounded-3xl p-6 pt-5">
          <h2 className="text-lg font-bold mb-6">Daily Progress</h2>
          
          <div className="relative w-48 h-48 mx-auto mb-8 flex items-center justify-center">
            {/* SVG Circle progress */}
            <svg className="absolute inset-0 w-full h-full -rotate-90">
              <circle cx="96" cy="96" r="80" fill="none" stroke="#2a2a2a" strokeWidth="12" />
              <circle cx="96" cy="96" r="80" fill="none" stroke="var(--color-neon)" strokeWidth="12" strokeDasharray="502" strokeDashoffset="120" strokeLinecap="round" />
            </svg>
            <div className="text-center mt-2">
              <FlameIcon className="w-6 h-6 text-neon mx-auto mb-1" />
              <div className="text-4xl font-bold text-neon leading-none tracking-tighter">1,850</div>
              <div className="text-[10px] font-bold text-gray-400 mt-2 tracking-widest uppercase">Kcal Burned</div>
            </div>
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-[#141414] rounded-2xl p-4 flex items-center space-x-4 border border-dark-border">
              <div className="w-8 h-8 rounded-full bg-cyan-500/10 text-cyan-500 flex items-center justify-center">
                <Footprints size={16} />
              </div>
              <div>
                <div className="text-xl font-bold">8,432</div>
                <div className="text-xs font-medium text-gray-500">Steps</div>
              </div>
            </div>
            <div className="bg-[#141414] rounded-2xl p-4 flex items-center space-x-4 border border-dark-border">
              <div className="w-8 h-8 rounded-full bg-purple-500/10 text-purple-400 flex items-center justify-center">
                <Clock size={16} />
              </div>
              <div>
                <div className="text-xl font-bold">45m</div>
                <div className="text-xs font-medium text-gray-500">Active</div>
              </div>
            </div>
          </div>
        </div>

        {/* Health Metrics */}
        <div>
          <h2 className="text-lg font-bold mb-4">Health Metrics</h2>
          <div className="bg-dark-card border border-dark-border rounded-2xl p-5 w-40 relative overflow-hidden">
            <div className="flex justify-between items-start mb-4">
              <div className="text-gray-400"><Activity size={20} /></div>
              <span className="text-neon text-xs font-bold">Normal</span>
            </div>
            <h3 className="text-3xl font-bold mb-1">22.4</h3>
            <p className="text-gray-400 text-sm">BMI Score</p>
          </div>
        </div>

        {/* Today's Plan */}
        <div>
          <h2 className="text-lg font-bold mb-4">Today's Plan</h2>
          <div className="bg-dark-card border border-dark-border rounded-2xl overflow-hidden relative">
            <div className="h-48 relative">
               <img src="https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?auto=format&fit=crop&w=600&q=80" alt="Full Body Burn" className="w-full h-full object-cover" />
               <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent"></div>
               <div className="absolute top-4 right-4 px-3 py-1 bg-black/50 border border-neon/50 text-neon text-xs font-bold rounded-lg backdrop-blur-md">
                 Intense
               </div>
               
               <div className="absolute bottom-4 left-4 right-4">
                 <h3 className="text-2xl font-bold mb-2">Full Body Burn</h3>
                 <div className="flex items-center text-sm font-medium text-gray-300 space-x-4">
                   <span className="flex items-center"><Clock size={16} className="mr-1.5" /> 45 Min</span>
                   <span className="flex items-center"><DumbbellIcon className="w-4 h-4 mr-1.5" /> Equipment</span>
                 </div>
               </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}

function FlameIcon(props: any) {
  return <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
}

function DumbbellIcon(props: any) {
  return <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}><path d="m6.5 6.5 11 11"/><path d="m21 21-1-1"/><path d="m3 3 1 1"/><path d="m18 22 4-4"/><path d="m2 6 4-4"/><path d="m3 10 7-7"/><path d="m14 21 7-7"/></svg>
}
