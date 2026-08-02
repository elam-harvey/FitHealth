/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useState, useEffect } from 'react';
import { Tab } from './types';
import { BottomNav } from './components/BottomNav';
import { LoginScreen } from './screens/LoginScreen';
import { HomeScreen } from './screens/HomeScreen';
import { WorkoutsScreen } from './screens/WorkoutsScreen';
import { MealsScreen } from './screens/MealsScreen';
import { StatsScreen } from './screens/StatsScreen';
import { CommunityScreen } from './screens/CommunityScreen';
import { ProfileScreen } from './screens/ProfileScreen';

export default function App() {
  const [isLoggedin, setIsLoggedin] = useState(false);
  const [currentTab, setCurrentTab] = useState<Tab>('home');


  const renderScreen = () => {
    if (!isLoggedin) {
      return <LoginScreen onLogin={() => setIsLoggedin(true)} />;
    }
    switch (currentTab) {
      case 'home': return <HomeScreen />;
      case 'workout': return <WorkoutsScreen />;
      case 'meals': return <MealsScreen />;
      case 'stats': return <StatsScreen />;
      case 'community': return <CommunityScreen />;
      case 'profile': return <ProfileScreen />;
      default: return <HomeScreen />;
    }
  };

  return (
    <div className="min-h-screen bg-dark-bg text-white w-full max-w-md mx-auto relative overflow-x-hidden shadow-[0_0_100px_rgba(0,0,0,0.5)] sm:border-x sm:border-dark-border flex flex-col">
      {renderScreen()}
      {isLoggedin && <BottomNav currentTab={currentTab} setCurrentTab={setCurrentTab} />}
    </div>
  );
}
