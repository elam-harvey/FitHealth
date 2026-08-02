import { TopBar } from '../components/TopBar';
import { useState, useEffect } from 'react';
import { BASE_URL } from '../config';


interface MealDetails {
  id: number;
  image: string | null;
  name: string | null;
  description: string | null;
  calories: number | null;
  category: string | null;
  importance: string | null;
}

interface MealPlanItem {
  id: number;
  meal: MealDetails;
  day_of_week: string;
  time_of_day: string;
  meal_plan: number;
}
 



export function MealsScreen() {

  const [mealItems, setMealItems] = useState<MealPlanItem[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchMeals = async () => {
      try{
        const token = localStorage.getItem('access_token');

        if (!token) {
          setError('Not logged in. Please log in.');
          setIsLoading(false);
          return;
        }

        // fetch meal items from the backend
        const response = await fetch(`${BASE_URL}/api/meals/meal-plan-items/`, {
          headers: {
            'Authorization': `Bearer ${token}`, 
            'Content-Type': 'application/json'
          }
        });
        if (!response.ok){
          throw new Error(`Failed to fetch meal items (Status Code: ' + response.status + ')`);
        }
        const data = await response.json();

        // Extract meal items from the response
        const items = Array.isArray(data) ? data : (data.results || []);
        setMealItems(items);
        setIsLoading(false);
      } catch (error) {
        setError(error.message);
        setIsLoading(false);
      }
    };
    fetchMeals();
  }, []);


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

        {/* Dynamic Meals */}
        <div className="space-y-6">
          {mealItems.length === 0 ? (
            <div className="text-center text-gray-400 py-8 bg-dark-card rounded-2xl border border-dark-border">
              No meal plans found for today.
            </div>
          ) : (
            mealItems.map((item, index) => {
              // Extract the nested meal object
              const meal = item.meal;
              
              // Map Time of Day or fallback to index logic for UI purposes
              const timeStr = item.time_of_day || (index === 0 ? "Breakfast" : index === 1 ? "Lunch" : "Dinner");
              const icon = timeStr.toLowerCase().includes("break") ? "☀️" : timeStr.toLowerCase().includes("lunch") ? "🔅" : "🌙";

              // Fallback image for meals like "Healthy Omelette" that have null images
              const defaultImage = "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=600&q=80";

              return (
                <MealCard
                  key={item.id} // using the MealPlanItem ID
                  icon={icon} 
                  title={timeStr}
                  name={meal.name} 
                  desc={meal.description}
                  kcal={`${meal.calories} kcal`} 
                  macros={meal.importance || "Standard Plan"} // Reusing importance field since macros aren't in JSON yet
                  tag={meal.category || "Plan"}
                  img={meal.image || defaultImage} 
                />
              );
            })
          )}
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
