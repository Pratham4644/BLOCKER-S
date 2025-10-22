import { Brain, Calendar, Mic, Link2 } from "lucide-react";

const Features = () => {
  const features = [
    {
      icon: Brain,
      title: "Smart Code Analysis",
      description: "Detects syntax errors, logic issues, and complexity. Get instant feedback on your code quality.",
      gradient: "from-primary to-primary-glow",
    },
    {
      icon: Calendar,
      title: "Intelligent Scheduling",
      description: "Syncs learning reminders via Google Calendar. Never miss a practice session.",
      gradient: "from-accent to-accent-glow",
    },
    {
      icon: Mic,
      title: "Marathi-English Voice Agent",
      description: "Voice-based control for coding tasks. Learn in your preferred language with bilingual support.",
      gradient: "from-purple-500 to-pink-500",
    },
    {
      icon: Link2,
      title: "Multi-tool Orchestration",
      description: "Automates GitHub, Notion, Gmail, Slack, WhatsApp. One command, multiple actions.",
      gradient: "from-blue-500 to-cyan-500",
    },
  ];

  return (
    <section id="features" className="py-20 px-4">
      <div className="container mx-auto">
        <div className="text-center mb-16 space-y-4">
          <h2 className="text-4xl md:text-5xl font-bold">
            Why Choose{" "}
            <span className="bg-gradient-accent bg-clip-text text-transparent">
              CodeSahayak?
            </span>
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            A complete AI-powered learning ecosystem designed for Indian CS students
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <div
                key={feature.title}
                className="group bg-gradient-card border border-border rounded-2xl p-6 hover:shadow-card transition-all duration-300 hover:-translate-y-2 animate-fade-in"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className={`w-14 h-14 rounded-xl bg-gradient-to-br ${feature.gradient} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300`}>
                  <Icon className="text-white" size={28} />
                </div>
                
                <h3 className="text-xl font-semibold mb-3">{feature.title}</h3>
                <p className="text-muted-foreground">{feature.description}</p>

                <div className="mt-4 h-1 w-0 bg-gradient-to-r from-primary to-accent group-hover:w-full transition-all duration-500 rounded-full" />
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Features;
