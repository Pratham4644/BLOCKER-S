import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Rocket, BookOpen } from "lucide-react";

const Hero = () => {
  const [currentLine, setCurrentLine] = useState(0);
  
  const codeLines = [
    "# CodeSahayak - Your AI Mentor",
    "def analyze_code(file):",
    "    errors = detect_syntax_errors(file)",
    "    complexity = calculate_complexity()",
    "    suggestions = generate_tips()",
    "    return insights",
    "",
    "# Smart scheduling integration",
    "schedule_learning_session(",
    "    topic='Binary Trees',",
    "    duration='1 hour'",
    ")",
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentLine((prev) => (prev + 1) % codeLines.length);
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <section id="home" className="min-h-screen flex items-center justify-center pt-20 px-4">
      <div className="container mx-auto">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="space-y-6 animate-fade-in">
            <div className="inline-block px-4 py-2 bg-accent/10 rounded-full border border-accent/20 text-accent text-sm">
              🏆 Hackathon Winner
            </div>
            
            <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold leading-tight">
              Your{" "}
              <span className="bg-gradient-accent bg-clip-text text-transparent">
                Marathi-English
              </span>
              <br />
              AI Coding Mentor
            </h1>
            
            <p className="text-xl text-muted-foreground max-w-lg">
              Analyze code, schedule sessions, and learn smarter with your personal AI assistant. 
              Master DSA with bilingual support and automated workflow integration.
            </p>

            <div className="flex flex-wrap gap-4">
              <Button
                size="lg"
                onClick={() => document.querySelector("#demo")?.scrollIntoView({ behavior: "smooth" })}
                className="bg-gradient-accent hover:shadow-accent-glow transition-all duration-300 group"
              >
                <Rocket className="mr-2 group-hover:animate-float" size={20} />
                Try Demo
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="border-primary/30 hover:bg-primary/10"
              >
                <BookOpen className="mr-2" size={20} />
                View Docs
              </Button>
            </div>

            <div className="flex gap-8 pt-4">
              <div>
                <div className="text-3xl font-bold text-primary">6+</div>
                <div className="text-sm text-muted-foreground">Tool Integrations</div>
              </div>
              <div>
                <div className="text-3xl font-bold text-accent">AI</div>
                <div className="text-sm text-muted-foreground">Powered</div>
              </div>
              <div>
                <div className="text-3xl font-bold text-primary-glow">24/7</div>
                <div className="text-sm text-muted-foreground">Available</div>
              </div>
            </div>
          </div>

          {/* Right Content - Code Block */}
          <div className="relative animate-fade-in" style={{ animationDelay: "0.2s" }}>
            <div className="absolute inset-0 bg-gradient-accent opacity-20 blur-3xl rounded-full" />
            <div className="relative bg-gradient-card border border-border rounded-2xl p-6 shadow-card">
              <div className="flex gap-2 mb-4">
                <div className="w-3 h-3 rounded-full bg-destructive" />
                <div className="w-3 h-3 rounded-full bg-yellow-500" />
                <div className="w-3 h-3 rounded-full bg-green-500" />
              </div>
              
              <pre className="text-sm font-mono text-foreground/90 space-y-2 min-h-[300px]">
                {codeLines.map((line, index) => (
                  <div
                    key={index}
                    className={`transition-all duration-500 ${
                      index === currentLine
                        ? "text-accent font-bold"
                        : index < currentLine
                        ? "opacity-60"
                        : "opacity-30"
                    }`}
                  >
                    {line || "\u00A0"}
                  </div>
                ))}
              </pre>

              <div className="mt-4 flex items-center gap-2 text-xs text-muted-foreground">
                <div className="w-2 h-2 bg-accent rounded-full animate-pulse-glow" />
                <span>AI Analysis in Progress...</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
