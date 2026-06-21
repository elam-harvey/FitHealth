import { TopBar } from '../components/TopBar';
import { User, Lock, CreditCard, FileText, Bell, Globe, HelpCircle, ChevronRight, PenSquare } from 'lucide-react';

export function ProfileScreen() {
  return (
    <div className="min-h-screen bg-dark-bg pb-24">
      <TopBar title="Profile settings" showAvatar={false} />
      
      <div className="px-4 mt-2">
        <div className="flex flex-col items-center mb-8">
          <div className="relative mb-4 mt-4">
            <div className="w-32 h-32 rounded-full p-1 border-2 border-neon">
              <img src="https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?auto=format&fit=crop&w=300&q=80" alt="Avatar" className="w-full h-full rounded-full object-cover" />
            </div>
            <button className="absolute bottom-0 right-0 w-10 h-10 bg-neon rounded-full flex items-center justify-center text-black border-4 border-dark-bg">
              <PenSquare size={18} strokeWidth={2.5} />
            </button>
          </div>
          <h2 className="text-2xl font-bold mb-1">Alex Mercer</h2>
          <p className="text-gray-400 text-sm">alex.mercer@fithealth.app</p>
        </div>

        <div className="grid grid-cols-2 gap-4 mb-8">
          <div className="bg-dark-card border border-dark-border rounded-xl p-4 flex flex-col items-center justify-center">
            <span className="text-neon text-xl font-bold mb-1">Level 12</span>
            <span className="text-gray-400 text-xs font-medium tracking-wider uppercase">Pro Athlete</span>
          </div>
          <div className="bg-dark-card border border-dark-border rounded-xl p-4 flex flex-col items-center justify-center">
            <span className="text-neon text-xl font-bold mb-1">482</span>
            <span className="text-gray-400 text-xs font-medium tracking-wider uppercase">Workouts</span>
          </div>
        </div>

        <div className="space-y-6">
          <div>
            <h3 className="text-sm font-bold text-gray-400 mb-3 px-2 tracking-widest uppercase">General</h3>
            <div className="bg-dark-card border border-dark-border rounded-2xl overflow-hidden divide-y divide-dark-border">
              <MenuRow icon={<User size={18} className="text-neon" />} label="Edit Profile" />
              <MenuRow icon={<Lock size={18} className="text-neon" />} label="Change Password" />
              <MenuRow icon={<CreditCard size={18} className="text-neon" />} label="Payment Methods" extra="Add Card" />
              <MenuRow icon={<FileText size={18} className="text-neon" />} label="Terms of Use" />
            </div>
          </div>

          <div>
            <h3 className="text-sm font-bold text-gray-400 mb-3 px-2 tracking-widest uppercase">Preferences</h3>
            <div className="bg-dark-card border border-dark-border rounded-2xl overflow-hidden divide-y divide-dark-border">
              <div className="flex items-center justify-between p-4 hover:bg-[#222] transition-colors">
                 <div className="flex items-center space-x-4">
                   <div className="w-8 flex justify-center"><Bell size={18} className="text-neon" /></div>
                   <span className="font-medium text-gray-200">Push Notifications</span>
                 </div>
                 <div className="w-12 h-6 bg-neon rounded-full flex items-center p-1 justify-end">
                   <div className="w-4 h-4 bg-black rounded-full"></div>
                 </div>
              </div>
              <MenuRow icon={<Globe size={18} className="text-neon" />} label="Language" sub="English" />
              <MenuRow icon={<HelpCircle size={18} className="text-neon" />} label="FAQ & Support" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function MenuRow({ icon, label, sub, extra }: any) {
  return (
    <button className="w-full flex items-center justify-between p-4 hover:bg-[#222] transition-colors">
      <div className="flex items-center space-x-4 text-left">
        <div className="w-8 flex justify-center">{icon}</div>
        <div>
          <div className="font-medium text-gray-200">{label}</div>
          {sub && <div className="text-xs text-gray-400">{sub}</div>}
        </div>
      </div>
      <div className="flex items-center space-x-2">
        {extra && <span className="text-sm text-gray-400">{extra}</span>}
        <ChevronRight size={18} className="text-gray-500" />
      </div>
    </button>
  );
}
