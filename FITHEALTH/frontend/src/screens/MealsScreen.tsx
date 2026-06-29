import { TopBar } from '../components/TopBar';

export function MealsScreen() {
  return (
    <div className="min-h-screen bg-dark-bg pb-24">
      <TopBar title="Meal Plans" showAvatar={true} />
      
      <div className="px-4 mt-2 space-y-8">
        
        {/* Daily Budget */}
        <div className="bg-dark-card border border-dark-border rounded-3xl p-6">
          <p className="text-gray-400 text-sm mb-2">Daily Budget</p>
          <div className="flex items-baseline mb-4">
            <h2 className="text-5xl font-bold text-neon mr-2 tracking-tight">1,850</h2>
            <span className="text-gray-400 font-medium">/ 2,400 kcal</span>
            <div className="ml-auto text-neon font-bold text-sm bg-neon/10 px-3 py-1 rounded-lg">550 kcal left</div>
          </div>
          
          <div className="h-2 bg-gray-800 rounded-full mb-6 overflow-hidden flex">
            <div className="h-full bg-neon w-[70%] rounded-full"></div>
          </div>

          <div className="flex justify-between text-sm font-medium">
            <div>
              <span className="text-gray-400">P:</span> <span className="text-white">120g/150g</span>
            </div>
            <div>
              <span className="text-gray-400">C:</span> <span className="text-white">200g/250g</span>
            </div>
            <div>
              <span className="text-gray-400">F:</span> <span className="text-white">45g/65g</span>
            </div>
          </div>
        </div>

        {/* Meals */}
        <div className="space-y-6">
          <MealCard 
            icon="☀️" title="Breakfast"
            name="Power Oats & Berries" desc="Quick & Easy prep"
            kcal="350 kcal" macros="P: 20g | C: 45g | F: 8g"
            tag="High Protein"
            img="https://images.unsplash.com/photo-1517673132405-a56a62b18caf?auto=format&fit=crop&w=600&q=80"
          />
          <MealCard 
            icon="🔅" title="Lunch"
            name="Ugali & Sukuma Wiki Lean" desc="Added grilled chicken breast"
            kcal="650 kcal" macros="P: 45g | C: 80g | F: 12g"
            tag="Local Support"
            img="https://images.unsplash.com/photo-1548943487-a2e4142f9ed1?auto=format&fit=crop&w=600&q=80"
          />
          <MealCard 
            icon="🌙" title="Dinner"
            name="Grilled Salmon & Quinoa" desc="Rich in Omega-3"
            kcal="520 kcal" macros="P: 40g | C: 30g | F: 22g"
            tag="Low Carb" tagColor="text-blue-400" tagBorder="border-blue-400/30"
            img="https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=600&q=80"
          />
        </div>

        {/* Hydration */}
        <div className="bg-dark-card border border-dark-border rounded-2xl p-5 flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="w-12 h-12 rounded-full bg-cyan-500/10 text-cyan-500 flex items-center justify-center">
              💧
            </div>
            <div>
              <h3 className="font-bold text-lg">Hydration</h3>
              <p className="text-gray-400 text-sm">1.5L / 3.0L</p>
            </div>
          </div>
          <button className="bg-gray-800 border border-dark-border px-4 py-2 rounded-xl text-sm font-medium text-white flex items-center">
            <span className="mr-2">+</span> Add
          </button>
        </div>

      </div>
    </div>
  );
}

function MealCard({ icon, title, name, desc, kcal, macros, tag, tagColor = "text-white", tagBorder = "border-white/20", img }: any) {
  return (
    <div>
      <h3 className="text-xl font-bold mb-3 flex items-center">
        <span className="mr-2 text-2xl">{icon}</span> {title}
      </h3>
      <div className="bg-dark-card border border-dark-border rounded-2xl overflow-hidden">
        <div className="h-36 relative">
          <img src={img} alt={name} className="w-full h-full object-cover" />
          <div className="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
          <div className={`absolute top-3 left-3 px-3 py-1 rounded border bg-black/40 backdrop-blur-sm text-xs font-bold font-mono tracking-wide ${tagColor} ${tagBorder}`}>
            {tag}
          </div>
        </div>
        <div className="p-4 flex justify-between items-end">
          <div>
            <h4 className="font-bold text-lg mb-1">{name}</h4>
            <p className="text-gray-400 text-sm">{desc}</p>
          </div>
          <div className="text-right">
            <div className="text-neon font-bold text-lg mb-1">{kcal}</div>
            <p className="text-gray-400 text-[11px] font-medium">{macros}</p>
          </div>
        </div>
      </div>
    </div>
  );
}
