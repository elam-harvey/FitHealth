import { TopBar } from '../components/TopBar';
import { Search, MapPin, Heart, MessageSquare, Share2, MoreHorizontal, PenSquare } from 'lucide-react';

export function CommunityScreen() {
  const posts = [
    {
      user: 'Sarah J.',
      time: '2 hours ago',
      avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=format&fit=crop&w=100&q=80',
      text: 'Just finished my first 5k! The training finally paid off. 🏃‍♀️💨 #PersonalBest #Running',
      image: 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=600&q=80',
      location: 'Central Park',
      likes: 24,
      comments: 5
    },
    {
      user: 'Marcus T.',
      time: '5 hours ago',
      avatar: 'https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?auto=format&fit=crop&w=100&q=80',
      text: 'Hit a new PR on the deadlift today. Form felt solid, moving up to 405lbs next week. 🏋️‍♂️',
      badge: { title: 'Deadlift PR', stat: '385', unit: 'lbs', icon: 'PR' },
      likes: 12,
      comments: 2
    },
    {
      user: 'Elena V.',
      time: 'Yesterday',
      avatar: 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=100&q=80',
      text: 'Rest day feels as important as training day. Active recovery with some light yoga. 🧘‍♀️✨',
      likes: 45,
      comments: 8
    }
  ];

  return (
    <div className="min-h-screen bg-dark-bg pb-24 relative">
      <TopBar title="FitHealth" showAvatar={true} />
      
      <div className="px-4 mt-2">
        <div className="relative mb-6">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
          <input 
            type="text" 
            placeholder="Find athletes or posts..." 
            className="w-full bg-dark-card border border-dark-border rounded-xl py-3.5 pl-12 pr-4 outline-none focus:border-neon transition-colors"
          />
        </div>

        <div className="space-y-4">
          {posts.map((post, i) => (
            <div key={i} className="bg-dark-card border border-dark-border rounded-2xl p-4">
              <div className="flex justify-between items-center mb-4">
                <div className="flex items-center space-x-3">
                  <img src={post.avatar} alt={post.user} className="w-10 h-10 rounded-full object-cover border border-gray-700" />
                  <div>
                    <h4 className="font-bold">{post.user}</h4>
                    <p className="text-xs text-gray-400">{post.time}</p>
                  </div>
                </div>
                <button className="text-gray-400 hover:text-white"><MoreHorizontal size={20} /></button>
              </div>
              
              <p className="text-gray-200 text-sm mb-4 leading-relaxed">{post.text}</p>
              
              {post.image && (
                <div className="relative rounded-xl overflow-hidden mb-4">
                  <img src={post.image} alt="Post media" className="w-full h-48 object-cover" />
                  {post.location && (
                     <div className="absolute bottom-2 right-2 px-3 py-1.5 bg-black/60 backdrop-blur-md rounded border border-white/10 text-xs font-bold flex items-center">
                       <MapPin size={12} className="text-neon mr-1.5" />
                       {post.location}
                     </div>
                  )}
                </div>
              )}

              {post.badge && (
                <div className="bg-[#141414] border border-dark-border rounded-xl p-4 mb-4 flex items-center justify-between">
                  <div className="flex items-center space-x-4">
                    <div className="w-12 h-12 bg-neon/10 rounded-lg flex items-center justify-center text-neon">
                      🏋️‍♂️
                    </div>
                    <div>
                      <p className="text-gray-400 text-xs font-medium">{post.badge.title}</p>
                      <p className="text-2xl font-bold text-neon">{post.badge.stat}<span className="text-sm text-gray-400 ml-1">{post.badge.unit}</span></p>
                    </div>
                  </div>
                  <div className="w-12 h-12 rounded-full border border-cyan-500/30 flex items-center justify-center">
                     <span className="text-cyan-400 font-bold text-sm tracking-widest uppercase">PR</span>
                  </div>
                </div>
              )}

              <div className="flex justify-between items-center pt-2">
                <div className="flex space-x-6 text-gray-400">
                  <button className="flex items-center space-x-2 text-neon">
                    <Heart size={20} fill="currentColor" />
                    <span className="font-medium text-sm">{post.likes}</span>
                  </button>
                  <button className="flex items-center space-x-2 hover:text-white transition-colors">
                    <MessageSquare size={20} />
                    <span className="font-medium text-sm">{post.comments}</span>
                  </button>
                </div>
                <button className="text-gray-400 hover:text-white transition-colors">
                  <Share2 size={20} />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 w-full max-w-md pointer-events-none z-40">
        <button className="absolute bottom-24 right-4 pointer-events-auto w-14 h-14 bg-neon rounded-2xl flex items-center justify-center text-black shadow-lg shadow-neon/20 hover:bg-[#b0d900] transition-colors">
          <PenSquare size={24} strokeWidth={2.5} />
        </button>
      </div>
    </div>
  );
}
