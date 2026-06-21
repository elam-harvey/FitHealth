import { Mail, Lock, Eye, EyeOff } from 'lucide-react';
import { useState } from 'react';

export function LoginScreen({ onLogin }: { onLogin: () => void }) {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="min-h-screen bg-dark-bg text-white px-6 pt-20 pb-10 flex flex-col">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-neon mb-6">FitHealth</h1>
        <h2 className="text-2xl font-semibold mb-2">Welcome Back</h2>
        <p className="text-gray-400 text-sm">Enter your details to access your dashboard.</p>
      </div>

      <div className="space-y-6 flex-1">
        <div className="space-y-2">
          <label className="text-xs font-bold tracking-wider text-gray-400 uppercase">Email</label>
          <div className="relative">
            <Mail className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
            <input 
              type="email" 
              defaultValue="athlete@example.com"
              className="w-full bg-dark-card border border-dark-border rounded-xl py-4 pl-12 pr-4 outline-none focus:border-neon transition-colors"
            />
          </div>
        </div>

        <div className="space-y-2">
          <label className="text-xs font-bold tracking-wider text-gray-400 uppercase">Password</label>
          <div className="relative">
            <Lock className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
            <input 
              type={showPassword ? 'text' : 'password'} 
              defaultValue="........"
              className="w-full bg-dark-card border border-dark-border rounded-xl py-4 pl-12 pr-12 outline-none focus:border-neon transition-colors tracking-widest"
            />
            <button 
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400"
            >
              {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
            </button>
          </div>
        </div>

        <div className="flex justify-between items-center text-sm">
          <label className="flex items-center space-x-2 cursor-pointer">
            <div className="w-5 h-5 rounded border border-dark-border bg-dark-card flex items-center justify-center">
              {/* Checkmark would go here */}
            </div>
            <span className="text-gray-300">Remember me</span>
          </label>
          <button className="text-neon font-medium">Forgot Password?</button>
        </div>

        <button 
          onClick={onLogin}
          className="w-full bg-neon text-black font-bold text-lg rounded-xl py-4 flex justify-center items-center space-x-2 hover:bg-[#b0d900] transition-colors mt-8"
        >
          <span>Log In</span>
          <span className="text-xl">→</span>
        </button>

        <div className="relative py-8 flex items-center justify-center">
          <div className="absolute border-t border-dark-border w-full"></div>
          <span className="px-4 bg-dark-bg text-gray-500 text-xs font-bold uppercase z-10 tracking-widest">
            Or continue with
          </span>
        </div>

        <div className="flex space-x-4">
          <button className="flex-1 bg-dark-card border border-dark-border rounded-xl py-4 flex justify-center items-center space-x-3">
            <svg viewBox="0 0 24 24" className="w-5 h-5">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
            </svg>
            <span className="font-semibold text-sm">Google</span>
          </button>
          <button className="flex-1 bg-dark-card border border-dark-border rounded-xl py-4 flex justify-center items-center space-x-3">
            <svg viewBox="0 0 24 24" className="w-6 h-6" fill="white">
              <path d="M17.05 20.28c-.98.95-2.05.88-3.08.4-1.09-.5-2.08-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.04 2.26-.74 3.58-.71 1.73.15 2.96.83 3.75 2.04-3.14 1.81-2.62 5.76.36 6.99-.75 1.83-1.63 3.3-2.77 3.85zm-3.22-13.82c-.1-1.39.5-2.73 1.5-3.66.97-.9 2.25-1.48 3.56-1.42.15 1.5-.47 2.91-1.55 3.86-.98.92-2.3 1.45-3.51 1.22z"/>
            </svg>
            <span className="font-semibold text-sm">Apple</span>
          </button>
        </div>
      </div>

      <div className="text-center mt-6">
        <p className="text-gray-400 text-sm">
          Don't have an account? <span className="text-neon font-medium cursor-pointer">Sign up</span>
        </p>
      </div>
    </div>
  );
}
