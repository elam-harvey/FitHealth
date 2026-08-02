import { Search, Flame } from 'lucide-react';
import { TopBar } from '../components/TopBar';
import {useState, useEffect, useMemo} from 'react';
import { BASE_URL } from '../config';


  interface Workout {
    id: number;
    name: string;
    duration: number;
    category: string;
    difficulty: string;
    target_muscle: string;
    secondary_muscles: string;
    api_source_id: string;
    image: string | null;
  }
  interface WorkoutPlanItem {
    id : number;
    workout_plan: Workout;
    day_of_week: string;
    time_of_day: string;
  }

  interface PaginatedWorkouts {
    "count": number;
    "next": string | null;
    "previous": string | null;
    "results": WorkoutPlanItem[];
  }

  const DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

  export function WorkoutsScreen() {
    const [workoutItems, setWorkoutsItems] = useState<WorkoutPlanItem[]>([]);
    const [searchTerm, setSearchTerm] = useState('');

    const [error, setError] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(true);

    const planName = 'Currently Enrolled Plan';
    
    useEffect(()=> {
      const fetchWorkouts = async () => {
        // Fetch workouts from the backend
        try {
          // grab the token saved in the login screen
          const token = localStorage.getItem('access_token');

          const response = await fetch(`${BASE_URL}/api/workouts/workout-plan-items/`, {
          // Attach the token to the headers
          headers: {
            'Authorization': `Bearer ${token}`, 
            'Content-Type': 'application/json'
          }
        });
          
          if (!response.ok) {
            throw new Error(`HTTP errror! status: ${response.status}`)
          }
          const workouts = (await response.json()) as PaginatedWorkouts;
          setWorkoutsItems(workouts.results);
        } catch (err){
          setError(err instanceof Error ? err.message : 'Error fetching workouts');
        } finally {
          setIsLoading(false);
        }
      };
      fetchWorkouts();
    }, []);

    // Group workouts by day of the week
    const groupedWorkouts = useMemo(() => {
      const grouped = workoutItems.reduce((acc, item) => {
        const day = item.day_of_week.toLowerCase();
        if (!acc[day]) acc[day] = [];
        acc[day].push(item);
        return acc;
      }, {} as Record<string, WorkoutPlanItem[]>);

      // convert to an array and sort it based on the calendar based order
      return Object.entries(grouped).sort(
        ([dayA], [dayB]) => DAYS_OF_WEEK.indexOf(dayA) - DAYS_OF_WEEK.indexOf(dayB)
      );
    }, [workoutItems]);

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

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

        {/* Master Workout Plan Container */}
        <div className="bg-[#1c1c1e] rounded-3xl p-5 shadow-lg border border-dark-border">
          {/* Plan Title Header */}
          <div className="mb-6 pb-4 border-b border-gray-800">
            <h2 className="text-2xl font-black">{planName}</h2>
            <p className="text-gray-400 text-sm mt-1">{workoutItems.length} total workouts this week</p>
          </div>

          {/* Render Groups by Day */}
          {groupedWorkouts.length === 0 ? (
            <p className="text-gray-500 text-center py-4">No workouts scheduled yet.</p>
          ) : (
            <div className="space-y-8">
              {groupedWorkouts.map(([day, items]) => (
                <div key={day} className="day-section">
                  {/* Day Header */}
                  <h3 className="text-lg font-bold text-neon mb-4 capitalize flex items-center">
                    <span className="w-2 h-2 rounded-full bg-neon mr-2"></span>
                    {day}
                  </h3>

                  {/* Workouts for this Day */}
                  <div className="space-y-3">
                    {items.map((item) => {
                      const { workout } = item;
                      
                      return (
                        <div key={item.id} className="bg-dark-card border border-dark-border rounded-2xl p-3 flex items-center space-x-4 hover:border-gray-600 transition-colors">
                          <div className="w-16 h-16 rounded-xl bg-gray-800 overflow-hidden flex-shrink-0 flex items-center justify-center">
                            {workout.image ? (
                              <img src={workout.image} alt={workout.name} className="w-full h-full object-cover" />
                            ) : (
                              <div className="text-gray-600">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m6.5 6.5 11 11"/><path d="m21 21-1-1"/><path d="m3 3 1 1"/><path d="m18 22 4-4"/><path d="m2 6 4-4"/><path d="m3 10 7-7"/><path d="m14 21 7-7"/></svg>
                              </div>
                            )}
                          </div>
                          
                          <div className="flex-1">
                            <div className="flex justify-between items-start mb-1">
                              <h4 className="font-bold text-md leading-tight pr-2">{workout.name}</h4>
                              <span className="px-2 py-1 rounded bg-gray-800 text-gray-300 text-[9px] font-bold uppercase tracking-wider whitespace-nowrap">
                                {workout.target_muscle}
                              </span>
                            </div>
                            
                            <div className="flex items-center text-xs text-gray-400 space-x-3 mt-2">
                              <span className="flex items-center">
                                <span className="mr-1 opacity-70">⏱</span>
                                {workout.duration}s
                              </span>
                              <span className="flex items-center">
                                <span className="mr-1 opacity-70">🔥</span>
                                {workout.difficulty}
                              </span>
                              <span className="flex items-center capitalize">
                                <span className="mr-1 opacity-70">☀️</span>
                                {item.time_of_day}
                              </span>
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
